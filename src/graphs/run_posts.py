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
from graphs.build_posts import build_posts


def run_posts(tema: str):

    # Armar grafo
    builder = StateGraph(AnalysisState)
    builder.add_node("fetch_data", fetch_data)
    builder.add_node("build_posts", build_posts)
    builder.add_edge(START, "fetch_data")
    builder.add_edge("fetch_data", "build_posts")
    builder.add_edge("build_posts", END)

    graph = builder.compile()

    # Ejecutar
    initial_state = AnalysisState(tema=tema)
    raw_state = graph.invoke(initial_state.model_dump())
    final_state = AnalysisState(**raw_state)
    return final_state.narrativa

 