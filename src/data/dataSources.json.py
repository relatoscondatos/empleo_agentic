import json
import pandas as pd
import duckdb
from typing import Dict, Any, List
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END


# ==== MODELO DE ESTADO ====

class AnalysisState(BaseModel):
    data: Dict[str, Any] = {}
    errors: list = []

# ==== CONFIGURACIÓN ====

archivo_parquet = "src/data/ene-01-def-agregado.parquet"

queries = {
    "ocupados": """
        SELECT datos.*
        FROM parquet_scan(?) AS datos
        WHERE variable = 'ocupados'
        ORDER BY año
    """,
    "informalidad": """
        SELECT año, variable, valor
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'formal', 'informal') AND año >= 2018
        ORDER BY variable, año
    """
}

# ==== TRANSFORMACIONES DE DATOS ====

def pivot_by_variable(df: pd.DataFrame) -> Dict[str, Dict[int, float]]:
    return {
        var: group.set_index("año")["valor"].to_dict()
        for var, group in df.groupby("variable")
    }

def pivot_by_year(df: pd.DataFrame) -> Dict[int, Dict[str, float]]:
    result = {}
    for _, row in df.iterrows():
        year = int(row["año"])
        var = row["variable"]
        val = float(row["valor"])
        if year not in result:
            result[year] = {}
        result[year][var] = val
    return result

def data_run_query(query: str) -> dict or str:
    con = duckdb.connect()
    result = con.execute(query, [archivo_parquet]).fetchdf()
    if result.empty:
        return "No data found for the query."
    return {
        "by_variable": pivot_by_variable(result),
        "by_year": pivot_by_year(result)
    }

# ==== NODOS ====


def fetch_data(state: AnalysisState) -> AnalysisState:
    try:
        data_ocupados = data_run_query(queries["ocupados"])
        data_informalidad = data_run_query(queries["informalidad"])
        
        if isinstance(data_ocupados, str):
            return state.model_copy(update={"errors": state.errors + [data_ocupados]})
        if isinstance(data_informalidad, str):
            return state.model_copy(update={"errors": state.errors + [data_informalidad]})

        updated_data = state.data.copy()
        updated_data["ocupados"] = data_ocupados
        updated_data["informalidad"] = data_informalidad

        return state.model_copy(update={"data": updated_data})
    except Exception as e:
        return state.model_copy(update={"errors": state.errors + [f"Data retrieval failed: {str(e)}"]})



# ==== GRAFO LANGGRAPH ====

builder = StateGraph(AnalysisState)
builder.add_node("fetch_data", fetch_data)


builder.add_edge(START, "fetch_data")
builder.add_edge("fetch_data", END)

graph = builder.compile()

# ==== EJECUCIÓN ====

if __name__ == "__main__":
    initial_state = AnalysisState().model_dump()
    raw_state = graph.invoke(initial_state, {"debug": True})
    final_state = AnalysisState(**raw_state)

    results_json = json.dumps(final_state.model_dump(), ensure_ascii=False, indent=4)
    print(results_json)
