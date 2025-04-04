import os
import sys
import json
from dotenv import load_dotenv

# Preparar entorno y sys.path
load_dotenv()
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from graphs.state import AnalysisState
from langgraph.graph import StateGraph, START, END
from data.fetch_data import fetch_data
from graphs.build_narrativa import build_narrativa


def run_narrativa(tema: str, output_folder: str = "src/output", print_text: bool = True):
    # Armar grafo
    builder = StateGraph(AnalysisState)
    builder.add_node("fetch_data", fetch_data)
    builder.add_node("build_narrativa", build_narrativa)
    builder.add_edge(START, "fetch_data")
    builder.add_edge("fetch_data", "build_narrativa")
    builder.add_edge("build_narrativa", END)

    graph = builder.compile()

    # Ejecutar
    initial_state = AnalysisState(tema=tema)
    raw_state = graph.invoke(initial_state.model_dump())
    final_state = AnalysisState(**raw_state)
    return final_state.narrativa

 