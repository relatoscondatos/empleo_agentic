from graphs.state import AnalysisState
from data.transform import run_query
from data.queries import queries

archivo = "src/data/parquet/ene-01-def-agregado.parquet"

def fetch_data(state: AnalysisState) -> AnalysisState:
    try:
        data = {}
        milestones = {}

        for var, query in queries.items():
            result = run_query(query, archivo)
            if isinstance(result, str):
                return state.model_copy(update={"errors": state.errors + [result]})
            data[var] = result

            # Extract key milestones and integrate them into the top-level milestones dict
            if "key_milestones" in result:
                for var_name, year_data in result["key_milestones"].items():
                    milestones[var_name] = year_data

        # Add unified milestones to the top-level "data" object
        data["milestones"] = milestones

        return state.model_copy(update={"data": data})
    except Exception as e:
        return state.model_copy(update={"errors": state.errors + [str(e)]})
