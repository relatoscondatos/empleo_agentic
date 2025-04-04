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


def run_narrativa(tema: str):
        # Check if we should use precomputed data
    use_precomputed = os.getenv('USE_PRECOMPUTED_DATA', 'false').lower() in ('true', '1', 'yes')

    if use_precomputed:
        # Define the path to the precomputed data file
        precomputed_file = os.path.join(BASE_DIR, f"prebuilt_content/generate_narrative_{tema}.md")
        if os.path.exists(precomputed_file):
            with open(precomputed_file, 'r', encoding='utf-8') as file:
                narrativa = json.load(file)
            if print_text:
                print(narrativa)
            return narrativa
        else:
            print(f"No precomputed data found for tema '{tema}'. Running the graph.")
            # Proceed to run the graph if precomputed data is not available


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

 