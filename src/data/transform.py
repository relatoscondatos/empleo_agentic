import pandas as pd
from typing import Dict, Any
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

def compute_diff(df: pd.DataFrame) -> Dict[str, Dict[int, float]]:
    diffs = {}
    for var, group in df.groupby("variable"):
        group_sorted = group.sort_values("año")
        diff_vals = group_sorted["valor"].diff().fillna(0).tolist()
        diffs[var] = dict(zip(group_sorted["año"], diff_vals))
    return diffs

def compute_pct_ocupados(df: pd.DataFrame) -> Dict[str, Dict[int, float]]:
    df_ocupados = df[df["variable"] == "ocupados"].set_index("año")["valor"]
    result = {}
    for var, group in df.groupby("variable"):
        if var == "ocupados":
            continue
        pct = {}
        for _, row in group.iterrows():
            año = int(row["año"])
            total = df_ocupados.get(año)
            if total and total > 0:
                pct[año] = row["valor"] / total
            else:
                pct[año] = None
        result[var] = pct
    return result

def compute_key_milestones(df: pd.DataFrame) -> Dict[str, Dict[int, Dict[str, float]]]:
    df_ocupados = df[df["variable"] == "ocupados"].set_index("año")["valor"]
    milestones = {}

    for var, group in df.groupby("variable"):
        # Determinar años relevantes
        if var == "informal":
            years = [2018, 2020, 2025]
        else:
            years = [2011, 2020, 2025]

        # Extraer datos para esos años si están disponibles
        vals = {}
        for _, row in group.iterrows():
            año = int(row["año"])
            if año in years:
                valor = float(row["valor"])
                pct = None
                if var != "ocupados":
                    total = df_ocupados.get(año)
                    if total and total > 0:
                        pct = valor / total
                vals[año] = {
                    "valor": valor,
                    "pct": pct
                }

        if vals:
            milestones[var] = vals

    return milestones


def run_query(query: str, archivo_parquet: str) -> Dict[str, Any] or str:
    con = duckdb.connect()
    df = con.execute(query, [archivo_parquet]).fetchdf()

    if df.empty:
        return "No data found."

    return {
        "raw": df.to_dict(orient="records"),  # optionally keep raw
        "by_variable": pivot_by_variable(df),
        "by_year": pivot_by_year(df),
        "diff_prev_year": compute_diff(df),
        "pct_ocupados": compute_pct_ocupados(df),
        "key_milestones": compute_key_milestones(df)

    }
