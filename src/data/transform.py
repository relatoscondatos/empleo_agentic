import pandas as pd
from typing import Dict
import duckdb

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
        result.setdefault(year, {})[var] = val
    return result

def run_query(query: str, archivo_parquet: str) -> dict or str:
    con = duckdb.connect()
    result = con.execute(query, [archivo_parquet]).fetchdf()
    if result.empty:
        return "No data found."
    return {
        "by_variable": pivot_by_variable(result),
        "by_year": pivot_by_year(result)
    }
