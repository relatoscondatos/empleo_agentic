from graphs.state import AnalysisState
from data.transform import run_query
from data.queries import queries

archivo = "src/data/parquet/ene-01-def-agregado.parquet"

def fetch_data(state: AnalysisState) -> AnalysisState:
    try:
        data = {}
        for var, query in queries.items():
            result = run_query(query, archivo)
            if isinstance(result, str):
                return state.model_copy(update={"errors": state.errors + [result]})
            data[var] = result
        return state.model_copy(update={"data": data})
    except Exception as e:
        return state.model_copy(update={"errors": state.errors + [str(e)]})
