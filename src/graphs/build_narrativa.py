import json
import os
from langchain_openai import ChatOpenAI
from graphs.state import AnalysisState
from graphs.prompts_narrative import prompt_base, prompt_tematica

llm = ChatOpenAI(model="gpt-4o",openai_api_key=os.getenv("OPENAI_API_KEY"))

def build_narrativa(state: AnalysisState) -> AnalysisState:
    prompt = prompt_tematica.get(state.tema, "")
    datos =   state.data.get(state.tema, {})
    full_prompt = f"{prompt_base}\n\n{prompt}\n\nDatos:\n{json.dumps(datos, indent=2)}"
    return state.model_copy(update={"narrativa": llm.invoke(full_prompt).content})

