# generate_data.json.py v20250403.23.0509
# This script generates a JSON file with the data fetched from the web
import sys
import os

# Set path to the "src/" folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from langgraph.graph import StateGraph, START, END
from models.state import AnalysisState
from data.fetch_data import fetch_data
import json

builder = StateGraph(AnalysisState)
builder.add_node("fetch_data", fetch_data)
builder.add_edge(START, "fetch_data")
builder.add_edge("fetch_data", END)

graph = builder.compile()

if __name__ == "__main__":
    final_state = AnalysisState(**graph.invoke(AnalysisState().model_dump()))
    results_json = json.dumps(final_state.model_dump(), ensure_ascii=False, indent=4)
    print(results_json)


