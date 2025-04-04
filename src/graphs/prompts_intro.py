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


prompt_ocupacion = f"""
Esta sección presenta información sobre el total de personas ocupadas en Chile, utilizando datos de la Encuesta Nacional de Empleo (ENE) del Instituto Nacional de Estadísticas (INE), correspondientes al trimestre diciembre-enero-febrero de cada año.

El objetivo es mostrar cómo ha evolucionado la cantidad de personas con empleo a lo largo del tiempo. Las visualizaciones se acompañan de una narrativa generada con inteligencia artificial para facilitar la comprensión del fenómeno.

{prompt_estilo_general}
"""

prompt_informalidad = f"""
Esta sección presenta datos sobre la informalidad laboral en Chile, considerando personas ocupadas en empleos formales e informales. La información proviene de la Encuesta Nacional de Empleo (ENE) del INE y está disponible desde 2018, correspondiente al trimestre diciembre-enero-febrero.

El objetivo es facilitar la comprensión de cómo ha cambiado la participación en empleos informales a lo largo del tiempo. El contenido narrativo ha sido generado con herramientas de inteligencia artificial para apoyar la interpretación de los datos.

{prompt_estilo_general}
"""

prompt_tpi = f"""
Esta sección entrega información sobre el subempleo por horario, en particular el Tiempo Parcial Involuntario (TPI). Los datos provienen de la Encuesta Nacional de Empleo (ENE) del INE y corresponden al trimestre diciembre-enero-febrero de cada año.

Se muestran cifras sobre personas que trabajan menos de lo que quisieran por falta de opciones, así como personas que trabajan a tiempo parcial voluntariamente. Los gráficos se acompañan de un texto explicativo generado por inteligencia artificial.

{prompt_estilo_general}
"""

prompt_ed_sup = f"""
Esta sección muestra cómo se distribuyen las personas ocupadas según su nivel educacional, distinguiendo entre quienes tienen educación superior completa y quienes no. Los datos son de la ENE del INE, para el trimestre diciembre-enero-febrero de cada año.

La narrativa ha sido generada con inteligencia artificial para apoyar la interpretación de los cambios en la participación laboral según nivel educativo.

{prompt_estilo_general}
"""

prompt_calificacion_ocupacion = f"""
Esta sección analiza el nivel de calificación de las ocupaciones de las personas empleadas en Chile. Se consideran categorías como alta calificación y calificación media o baja, según la clasificación CIUO 08.CL. Los datos son de la ENE del INE, para el trimestre diciembre-enero-febrero.

El análisis narrativo ha sido generado por inteligencia artificial para facilitar la interpretación de las tendencias observadas en las ocupaciones según su nivel de calificación.

{prompt_estilo_general}
"""

prompt_ed_sup_calificacion_ocupacion = f"""
Esta sección analiza la relación entre educación superior completa y la calificación de las ocupaciones desempeñadas. Se distinguen personas con educación superior que trabajan en ocupaciones de alta calificación y aquellas en ocupaciones de calificación media o baja. 

Los datos son de la Encuesta Nacional de Empleo (ENE) del INE, correspondientes al trimestre diciembre-enero-febrero. La interpretación narrativa fue generada con inteligencia artificial para facilitar la comprensión.

{prompt_estilo_general}
"""

prompt_sector_publico = f"""
Esta sección presenta la evolución del empleo en el sector público y en el sector no público (que incluye trabajadores del sector privado, por cuenta propia, servicio doméstico y familiares no remunerados). Los datos provienen de la ENE del INE, para el trimestre diciembre-enero-febrero.

La narrativa generada con inteligencia artificial busca facilitar la interpretación de los cambios en la distribución del empleo entre estos sectores.

{prompt_estilo_general}
"""

prompt_nacionalidad = f"""
Esta sección muestra cómo ha evolucionado el empleo de personas según su nacionalidad. Se considera el número de personas ocupadas con nacionalidad chilena y extranjera. Los datos corresponden a la ENE del INE para el trimestre diciembre-enero-febrero.

La narrativa generada con inteligencia artificial permite comprender mejor los cambios en la participación laboral de personas extranjeras en Chile.

{prompt_estilo_general}
"""

prompt_sexo = f"""
Esta sección analiza la evolución del empleo según sexo, considerando personas ocupadas que se identifican como hombres y como mujeres. Los datos son oficiales de la Encuesta Nacional de Empleo (ENE) del INE, correspondientes al trimestre diciembre-enero-febrero.

Se incluye una narrativa generada por inteligencia artificial que acompaña los gráficos y ayuda a interpretar los cambios en la participación laboral por sexo.

{prompt_estilo_general}
"""

prompt_tematica = {
    "dummy": prompt_dummy,
    "introduccion_general": prompt_introduccion_general,
    "ocupacion": prompt_ocupacion,
    "informalidad": prompt_informalidad,
    "tpi": prompt_tpi,
    "ed_sup": prompt_ed_sup,
    "calificacion_ocupacion": prompt_calificacion_ocupacion,
    "ed_sup_calificacion_ocupacion": prompt_ed_sup_calificacion_ocupacion,
    "sector_publico": prompt_sector_publico,
    "nacionalidad": prompt_nacionalidad,
    "sexo": prompt_sexo,
}
