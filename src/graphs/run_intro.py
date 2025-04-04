import os
import sys
import json
from dotenv import load_dotenv
from typing import Dict, Any, List
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI


# Preparar entorno y sys.path
load_dotenv()
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from graphs.prompts_intro import prompt_base, prompt_tematica

llm = ChatOpenAI(model="gpt-4o")


class AnalysisState(BaseModel):
    intro: str = ""
    tema: str = ""
    errors: List[str] = []


def build_intro(state: AnalysisState) -> AnalysisState:
    prompt = prompt_tematica.get(state.tema, "")
    full_prompt = f"{prompt_base}\n\n{prompt}"

    return state.model_copy(update={"intro": llm.invoke(full_prompt).content})


def run_intro(tema: str):
    # Armar grafo
    builder = StateGraph(AnalysisState)
    builder.add_node("build_intro", build_intro)
    builder.add_edge(START, "build_intro")
    builder.add_edge("build_intro", END)

    graph = builder.compile()

    # Ejecutar
    initial_state = AnalysisState(tema=tema)
    raw_state = graph.invoke(initial_state.model_dump())
    final_state = AnalysisState(**raw_state)
    return final_state.intro

 