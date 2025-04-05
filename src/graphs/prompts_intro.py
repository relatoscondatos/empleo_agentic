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

Aclara que los datos corresponden al trimestre diciembre-enero-febrero de cada año y provienen de la Encuesta Nacional de Empleo (ENE), elaborada por el Instituto Nacional de Estadísticas (INE).

Indica que la comparación se realiza siempre para el mismo trimestre de cada año, con el fin de evitar distorsiones provocadas por factores estacionales, como vacaciones, ciclos productivos o actividades específicas de ciertos meses.

Explica que el foco del análisis está puesto en las **personas ocupadas**, es decir, quienes se encuentran trabajando durante el período de referencia. El sitio no analiza indicadores como desempleo, participación laboral ni fuerza de trabajo, sino que se concentra en cómo ha cambiado la **composición del empleo ocupado** a lo largo del tiempo.

También indica que las narrativas fueron generadas con un modelo de lenguaje de inteligencia artificial y que el sitio tiene un propósito exploratorio y divulgativo, sin fines comerciales.

{prompt_estilo_general}

**Importante**: El texto debe presentarse como introducción al contenido del sitio, no como una recomendación ni como una sugerencia para su desarrollo. No uses expresiones como "Aquí tienes un texto" o "Te recomiendo". Solo redacta la introducción que irá en la página.
"""

prompt_ocupados = f"""
Redacta un texto introductorio para la sección "Evolución del empleo total en Chile" de una página web sobre el mercado laboral.

El texto debe informar que esta sección muestra cómo ha cambiado el número total de personas ocupadas en el país a lo largo del tiempo, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que permiten identificar variaciones en el empleo considerando los períodos prepandemia, pandemia y postpandemia.

Evita expresiones que aludan al lector o califiquen el contenido. El tono debe ser institucional, objetivo y descriptivo.

{prompt_estilo_general}
"""

prompt_informalidad = f"""
Redacta un texto introductorio para la sección "Empleo formal e informal" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre la evolución del empleo formal e informal en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen datos del total de personas ocupadas, personas en ocupaciones formales y personas en ocupaciones informales, desde 2018 en adelante.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y que permiten observar cambios en el empleo por tipo de formalidad en distintos períodos: prepandemia, pandemia y postpandemia.

El tono debe ser institucional y descriptivo, sin referencias al lector ni juicios de valor.

{prompt_estilo_general}
"""

prompt_tpi = f"""
Redacta un texto introductorio para la sección "Subempleo por horario (TPI)" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre las personas ocupadas en empleos de tiempo parcial involuntario (TPI), según datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen datos de personas en TPI, personas en tiempo parcial no involuntario y el total de ocupados.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y permiten observar cómo ha variado el subempleo por horario a lo largo del tiempo, en los períodos prepandemia, pandemia y postpandemia.

El texto debe tener un tono objetivo y descriptivo, evitando expresiones dirigidas al lector.

{prompt_estilo_general}
"""

prompt_ed_sup = f"""
Redacta un texto introductorio para la sección "Nivel educacional de las personas ocupadas" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre la distribución de las personas ocupadas según su nivel educativo, con datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de personas con educación superior completa y personas sin educación superior completa.

Menciona que los datos corresponden al trimestre diciembre-enero-febrero de cada año y permiten observar cómo ha cambiado la participación de cada grupo educativo en el empleo, considerando los períodos prepandemia, pandemia y postpandemia.

El tono debe ser institucional y descriptivo, sin calificaciones ni referencias al lector.

{prompt_estilo_general}
"""

prompt_calificacion_ocupacion = f"""
Redacta un texto introductorio para la sección "Calificación de las ocupaciones" de una página web sobre el mercado laboral.

Esta sección presenta información sobre el nivel de calificación de las ocupaciones desempeñadas por las personas ocupadas en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Los datos están clasificados según la Clasificación Internacional Uniforme de Ocupaciones (CIUO), utilizada por el INE. Entre los años 2011 y 2017 se utilizó la versión CIUO-88, y desde 2018 en adelante se emplea la versión CIUO-08. En ambos casos, las ocupaciones se agrupan en 10 grandes grupos.

Para efectos del análisis, se consideran como **ocupaciones de alta calificación** aquellas pertenecientes a los grupos 1 a 3 (directivos, profesionales y técnicos). Las **ocupaciones de calificación media o baja** corresponden a los grupos 4 a 9, que incluyen empleos como personal administrativo, vendedores, trabajadores de servicios, operarios, conductores, agricultores y oficios manuales. El grupo 10, correspondiente a ocupaciones no clasificadas, no se incluye en esta sección.

Los datos corresponden al trimestre diciembre-enero-febrero de cada año, y permiten analizar cómo ha cambiado la distribución de los tipos de ocupación entre personas ocupadas, considerando los períodos prepandemia, pandemia y postpandemia.

El texto debe mantener un tono descriptivo, neutral y profesional, sin referencias al lector.

{prompt_estilo_general}
"""

prompt_edu_calificacion_ocupacion = f"""
Redacta un texto introductorio para la sección "Composición del empleo según nivel educativo y calificación del trabajo" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección muestra la relación entre el nivel educativo y la calificación de las ocupaciones, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se presentan tres grupos: 
- Personas con educación superior en ocupaciones de alta calificación.
- Personas con educación superior en ocupaciones de calificación media o baja (asociadas al subempleo por competencias).
- Personas sin educación superior.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y permiten analizar cómo ha cambiado esta distribución a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

El texto debe evitar emitir juicios de valor, centrarse en lo descriptivo, y estar alineado con el estilo institucional del sitio.

{prompt_estilo_general}
"""

prompt_sector_publico = f"""
Redacta un texto introductorio para la sección "Empleo en el sector público y no público" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre la evolución del empleo en el sector público y el sector no público, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que el sector no público incluye empleo en el sector privado, por cuenta propia, en servicio doméstico o como trabajadores familiares no remunerados.

Menciona que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y permiten analizar cómo ha cambiado la participación relativa de ambos sectores a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

Evita expresiones dirigidas al lector o calificativos sobre el contenido. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""

prompt_nacionalidad = f"""
Redacta un texto introductorio para la sección "Personas ocupadas según nacionalidad" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre la distribución del empleo según la nacionalidad de las personas, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de personas ocupadas con nacionalidad chilena y extranjera.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año, y permiten observar cómo ha evolucionado la participación de personas extranjeras en el empleo a lo largo del tiempo, considerando los períodos prepandemia, pandemia y postpandemia.

El texto debe evitar expresiones subjetivas o dirigidas al lector. El tono debe ser objetivo e institucional.

{prompt_estilo_general}
"""

prompt_sexo = f"""
Redacta un texto introductorio para la sección "Personas ocupadas según sexo" de una página web sobre el mercado laboral.

El texto debe indicar que esta sección presenta información sobre el empleo desagregado por sexo, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE).

Aclara que se incluyen cifras de hombres y mujeres ocupados.

Indica que los datos corresponden al trimestre diciembre-enero-febrero de cada año y que permiten observar cómo ha evolucionado la participación laboral de hombres y mujeres en distintos períodos: prepandemia, pandemia y postpandemia.

Evita expresiones personales, calificativas o dirigidas al lector. El tono debe ser institucional y descriptivo.

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
    "edu_calificacion_ocupacion": prompt_edu_calificacion_ocupacion,
    "sector_publico": prompt_sector_publico,
    "nacionalidad": prompt_nacionalidad,
    "sexo": prompt_sexo,
}
