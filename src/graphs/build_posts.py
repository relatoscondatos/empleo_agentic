import json
import os
from langchain_openai import ChatOpenAI
from graphs.state import AnalysisState
from graphs.prompts_narrative import prompt_base, prompt_tematica

llm = ChatOpenAI(model="gpt-4o",openai_api_key=os.getenv("OPENAI_API_KEY"))

def build_posts(state: AnalysisState) -> AnalysisState:
    prompt = """
    Genera una serie de mensajes breves para un hilo en Twitter (max 280 chars) que resuma datos notables sobre el empleo en Chile.
    
    Para cada mensaje utiliza uno de los siguientes temas:
    - Total ocupados (ocupados)
    - Empleo informal (informal)
    - Empleo con educación superior (ed_sup)
    - Empleo en ocupaciones de alta calificación (alta_calificacion)
    - Empleo con Tiempo Parcial Involuntario (tpi)
    - Subempleo (subempleo_total)
    - Empleo con educación superior y ocupacion de alta calificación (ed_sup_competencia_alta)
    - Empleo en sector público (sector_publico)
    - Personas extranjeras (nacionalidad_extranjera)
    - Mujeres (mujer)
    
Abajo entrego un objeto JSON con los datos de todas las variables en que se incluyen los valores y respectivos porcentajes en los años 2011, 2020 y 2025 (salvo para informalidad que es 2018, 2020 y 2025).

El formato es el siguiente:
               "ocupados": {
                    "2011": {
                        "valor": 7621029.946048457,
                        "pct": null
                    },
                    "2020": {
                        "valor": 9063373.737067282,
                        "pct": null
                    },
                    "2025": {
                        "valor": 9396873.67711522,
                        "pct": null
                    }
                }

                
Para cada variable quiero un comentario breve y los datos de los años clave. Por ejemplo:
     1️⃣ El empleo informal ha bajado:
    📉 2.54M (28.9%) en 2018
    📉 2.63M (29.0%) en 2020
    📉 2.45M (26.1%) en 2025
    Menos de 3 de cada 10 personas ocupadas trabajan hoy en condiciones informales.
    """

    datos =   state.data.get(state.tema, {})
    full_prompt = f"{prompt}\n\nDatos:\n{json.dumps(datos, indent=2)}"
    return state.model_copy(update={"narrativa": llm.invoke(full_prompt).content})

