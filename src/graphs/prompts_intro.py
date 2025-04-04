prompt_base = """Hemos construido una página web que entrega información sobre el mercado laboral en Chile. La información está organizada en secciones como ocupación, informalidad, subempleo, educación, calificación ocupacional, sector público y no público, nacionalidad y sexo.

Los datos provienen de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE), y corresponden al trimestre diciembre-enero-febrero de cada año. Las narrativas fueron generadas con un modelo de lenguaje de inteligencia artificial.

"""

prompt_estilo_general = """
El texto debe ser claro, conciso y fácil de entender para el público en general.
Evita el uso de jerga técnica y asegúrate de que cualquier término especializado esté explicado de manera sencilla.
Usa un tono neutral y objetivo, evitando opiniones personales o juicios de valor.
No uses frases largas o complejas. Mantén las oraciones cortas y directas.
Usa un lenguaje inclusivo y evita estereotipos de género o culturales.
"""

prompt_dummy = "Solo di 'Hola Mundo'."

prompt_introduccion_general = f"""
Redacta un texto introductorio para una página web que presenta información sobre el mercado laboral en Chile.

La página incluye gráficos y descripciones narrativas generadas con inteligencia artificial para distintas secciones: ocupación, informalidad, subempleo, educación, calificación ocupacional, sector público, nacionalidad y sexo.

Aclara que los datos corresponden al trimestre diciembre-enero-febrero de cada año y provienen de la Encuesta Nacional de Empleo (ENE) elaborada por el Instituto Nacional de Estadísticas (INE).

También explica que las narrativas fueron generadas con un modelo de lenguaje de inteligencia artificial y que el sitio tiene un fin divulgativo y exploratorio, sin fines comerciales.

{prompt_estilo_general}

**Importante**: El texto debe presentarse como introducción al contenido del sitio, no como una recomendación ni como una sugerencia para su desarrollo. No uses expresiones como "Aquí tienes un texto" o "Te recomiendo". Solo redacta la introducción que irá en la página.
"""


prompt_ocupados = f"""
Redacta un texto introductorio para la sección "Total de personas ocupadas" de una página web sobre el mercado laboral en Chile.

El texto debe informar que esta sección presenta la evolución del número de personas ocupadas en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que permiten observar los cambios en el empleo a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

Evita cualquier expresión que haga referencia al lector (como "encontrarás", "te presentamos", "podrás ver", etc.) o que califique el contenido ("claro", "útil", "interesante", etc.). El texto debe limitarse a describir de manera objetiva el contenido de la sección.

{prompt_estilo_general}
"""



prompt_informalidad = f"""
Redacta un texto introductorio para la sección "Informalidad" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre la evolución de la ocupación informal en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).  

Aclara que se incluyen datos del total de personas ocupadas, así como personas en ocupaciones formales e informales, y que la serie está disponible desde el año 2018 en adelante.

Menciona que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que se consideran los períodos prepandemia, pandemia y postpandemia.

No utilices expresiones que hagan referencia directa al lector (como "aquí verás", "esta sección te mostrará", "podrás comprender", etc.) ni calificativos sobre el contenido ("claro", "completo", "útil", etc.). El tono debe ser institucional, neutral y descriptivo.

{prompt_estilo_general}
"""


prompt_tpi = f"""
Redacta un texto introductorio para la sección "Proporción de Trabajadores en Tiempo Parcial Involuntario" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre las personas ocupadas en empleos de tiempo parcial involuntario (TPI), según datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).  

Aclara que se incluyen datos del total de personas ocupadas, Persona ocupada que trabajó de manera involuntaria a tiempo parcial y auqellas personas ocupadas que no están en esta condición.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que permiten observar cambios a lo largo del tiempo considerando los períodos prepandemia, pandemia y postpandemia.

Evita el uso de frases que hagan referencia directa al lector o que califiquen el contenido. El tono debe ser institucional, objetivo y descriptivo.

{prompt_estilo_general}
"""

prompt_ed_sup = f"""
Redacta un texto introductorio para la sección "Nivel educacional de las personas ocupadas" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre la participación de personas con y sin educación superior en el empleo en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen datos del total de personas ocupadas, personas con educación superior completa y personas sin educación superior o sin educación superior completa.

Menciona que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que se analizan las tendencias considerando los períodos prepandemia, pandemia y postpandemia.

No deben utilizarse frases que aludan directamente al lector ni calificativos sobre el contenido. El tono debe ser institucional, claro y descriptivo.

{prompt_estilo_general}
"""

prompt_calificacion_ocupacion = f"""
Redacta un texto introductorio para la sección "Calificación de las ocupaciones" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre el nivel de calificación de las ocupaciones desempeñadas por las personas ocupadas, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen datos del total de personas ocupadas en ocupaciones de alta calificación (`alta_calificacion`) y en ocupaciones de calificación media o baja (`calificacion_media_baja`).

Menciona que esta clasificación se basa en la CIUO 08.CL, la adaptación chilena de la Clasificación Internacional Uniforme de Ocupaciones.  
Explica que:
- Alta calificación incluye los grupos 1 a 3: directivos, profesionales y técnicos.
- Calificación media o baja corresponde a los grupos 4 a 9.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y que permiten observar cambios a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

Evita frases que califiquen el contenido o se dirijan directamente al lector. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""


prompt_ed_sup_calificacion_ocupacion = f"""
Redacta un texto introductorio para la sección "Educación superior y tipo de ocupación" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección analiza la relación entre el nivel educativo y la calificación de las ocupaciones desempeñadas por personas con educación superior completa, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen datos de personas con educación superior en ocupaciones de alta calificación y personas con educación superior en ocupaciones de calificación media o baja.

Explica que este segundo grupo puede interpretarse como casos de subempleo por competencias, en los que las personas trabajan en puestos que no requieren plenamente su nivel de formación.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y permiten observar cambios en la adecuación entre formación y tipo de ocupación, considerando los períodos prepandemia, pandemia y postpandemia.

Evita frases que califiquen el contenido o que se dirijan directamente al lector. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""

prompt_sector_publico = f"""
Redacta un texto introductorio para la sección "Ocupaciones del sector público" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre el empleo en el sector público y ocupaciones que no corresponden al sector público (a las que nos referimos como sector no público), utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de personas ocupadas en el sector público y en el sector no público.

Explica que el sector no público comprende a quienes trabajan en el sector privado, por cuenta propia, en servicio doméstico o como trabajadores familiares no remunerados.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y que permiten observar cómo ha evolucionado la participación del empleo público y no público a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

Evita cualquier saludo, uso de la primera o segunda persona ("nosotros", "ustedes", "te", "nuestro", etc.), frases promocionales, adjetivos evaluativos o juicios sobre la claridad, utilidad o calidad del contenido.

El tono debe ser neutral, institucional y descriptivo.

{prompt_estilo_general}
"""


prompt_nacionalidad = f"""
Redacta un texto introductorio para la sección "Personas ocupadas según nacionalidad" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre el empleo según la nacionalidad de las personas, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de personas ocupadas con nacionalidad chilena y con nacionalidad extranjera.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y que permiten observar la evolución de la participación de personas extranjeras en el empleo en Chile, considerando los períodos prepandemia, pandemia y postpandemia.

Evita frases que califiquen el contenido o se dirijan directamente al lector. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""

prompt_sexo = f"""
Redacta un texto introductorio para la sección "Ocupación según sexo" de una página web sobre el mercado laboral en Chile.

El texto debe indicar que esta sección presenta información sobre el empleo desagregado por sexo, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de hombres y mujeres ocupados en el país.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y que permiten observar la evolución de la participación laboral de hombres y mujeres a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

Evita frases que califiquen el contenido o se dirijan directamente al lector. El tono debe ser institucional, descriptivo y no incluir juicios de valor.

{prompt_estilo_general}
"""

prompt_tematica = {
    "dummy": prompt_dummy,
    "introduccion_general": prompt_introduccion_general,
    "ocupados": prompt_ocupados,
    "informalidad": prompt_informalidad,
    "tpi": prompt_tpi,
    "ed_sup": prompt_ed_sup,
    "calificacion_ocupacion": prompt_calificacion_ocupacion,
    "ed_sup_calificacion_ocupacion": prompt_ed_sup_calificacion_ocupacion,
    "sector_publico": prompt_sector_publico,
    "nacionalidad": prompt_nacionalidad,
    "sexo": prompt_sexo,
}
