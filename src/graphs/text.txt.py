import sys
import os

# Set path to the "src/" folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from langgraph.graph import StateGraph, START, END
from models.state import AnalysisState
from data.fetch_data import fetch_data
from prompts.base_prompts import prompt_base, prompt_ocupacion, prompt_informalidad
from langchain_openai import ChatOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def build_narrativa_ocupacion(state: AnalysisState) -> AnalysisState:
    full_prompt = f"{prompt_base}\n\n{prompt_ocupacion}\n\nDatos:\n{json.dumps(state.data['ocupados'], indent=2)}"
    return state.model_copy(update={"narrativa_ocupacion": llm.invoke(full_prompt).content})

def build_narrativa_informalidad(state: AnalysisState) -> AnalysisState:
    full_prompt = f"{prompt_base}\n\n{prompt_informalidad}\n\nDatos:\n{json.dumps(state.data['informalidad'], indent=2)}"
    return state.model_copy(update={"narrativa_informalidad": llm.invoke(full_prompt).content})

builder = StateGraph(AnalysisState)
builder.add_node("fetch_data", fetch_data)
builder.add_node("build_narrativa_ocupacion", build_narrativa_ocupacion)

builder.add_edge(START, "fetch_data")
builder.add_edge("fetch_data", "build_narrativa_ocupacion")
builder.add_edge("build_narrativa_ocupacion", END)

graph = builder.compile()

if __name__ == "__main__":
    final_state = AnalysisState(**graph.invoke(AnalysisState().model_dump()))
    print(final_state.narrativa_ocupacion)

