prompt_base = """El objeto a continuación contiene datos de series temporales sobre indicadores laborales en Chile, estructurados en dos formas:
- `by_variable`: permite observar la evolución temporal de cada variable.
- `by_year`: permite comparar distintas variables en un mismo año.

Los datos corresponden al trimestre diciembre-enero-febrero de cada año. Según esto:
- Los años hasta 2020 representan el período **prepandemia** (previo al primer caso de COVID-19 en Chile).
- Los años 2021 y 2022 corresponden al período **de pandemia**.
- Desde 2023, se considera un período **postpandemia**. Las cifras son oficiales del año 2025 y no incluyen estimaciones ni proyecciones.

Redacta una narrativa concisa, clara y analítica que describa las principales tendencias y patrones observados en los datos. Interpreta los cambios y continuidades considerando los tres momentos señalados.
Considera que todas las cifras son reales y no proyectadas, en particular no hacer mención a estimaciones o proyecciones.
"""

prompt_dummy = """Solo di 'Hola Mundo'.
"""

prompt_ocupacion = """El indicador a analizar es `ocupados`, que representa el total de personas empleadas en el país.

Describe las principales tendencias en la evolución del número de personas ocupadas, considerando los tres períodos definidos (prepandemia, pandemia y postpandemia). Destaca crecimientos, caídas, estancamientos u otras variaciones significativas, y si es posible, sugiere posibles explicaciones para estos cambios.
"""

prompt_informalidad = """El análisis se enfoca en la **informalidad laboral** en Chile. Se cuenta con datos del total de personas ocupadas (`ocupados`), personas en ocupaciones formales (`formal`) y en ocupaciones informales (`informal`).

Describe cómo ha evolucionado la informalidad tanto en términos absolutos como relativos (porcentaje de personas en ocupaciones informales respecto del total de ocupados).

Identifica aumentos o disminuciones importantes y relaciónalos con los tres períodos analizados (prepandemia, pandemia, postpandemia). Si es posible, interpreta causas probables de los cambios observados o sugiere hipótesis.
"""

prompt_tpi = """El análisis se enfoca en el subempleo por horario asociado al indicador Tiempo Parcial Involuntario (tpi) en Chile. Se cuenta con datos del total de personas ocupadas (`ocupados`), personas en ocupaciones de tiempo parcial involuntario (`tpi`) y en ocupaciones de tiempo parcial no involuntario (`no_tpi`).
Un alto nivel de tpi puede ser indicativo de subempleo, lo que puede afectar la calidad de vida de los trabajadores y su bienestar económico. Y también puede ser un indicador de un desempleo encubierto.
Además de los valores absolutos analiza la evolución del porcentaje de personas en ocupaciones de tiempo parcial involuntario respecto del total de ocupados.
Describe cómo ha evolucionado el subempleo por horario en Chile, considerando los tres períodos definidos (prepandemia, pandemia y postpandemia). Identifica aumentos o disminuciones importantes y relaciónalos con los tres períodos analizados. Si es posible, interpreta causas probables de los cambios observados o sugiere hipótesis.
"""
prompt_ed_sup = """El análisis se enfoca en el nivel educacional de las personas ocupadas en Chile. Se cuenta con datos del total de personas ocupadas (`ocupados`), personas con educación superior completa (`ed_sup_completa`) y personas sin educación superior (`sin_ed_sup`)."""

prompt_calificacion_ocupacion = """El análisis se enfoca en la calificación de las ocupaciones en Chile. Se cuenta con datos del total de personas ocupadas (`ocupados`), personas con alta calificación (`alta_calificacion`) y personas con calificación media o baja (`calificacion_media_baja`).
La clasificación se basa en la clasificacion chilena de ocupaciones CIUO 08.CL es la adaptación nacional de CIUO 08, que es la Clasificación Internacional Uniforme de Ocupaciones de la OIT. Esta clasificación se utiliza para categorizar las ocupaciones laborales en diferentes grupos según su nivel de calificación y tipo de trabajo.
1 Directores, gerentes y administradores 
2 Profesionales, científicos e intelectuales 
3 Técnicos y profesionales de nivel medio 
4 Personal de apoyo administrativo 
5 Trabajadores de los servicios y vendedores de comercios y mercados 
6 Agricultores y trabajadores calificados agropecuarios, forestales y pesqueros 
7 Artesanos y operarios de oficios 
8 Operadores de instalaciones, máquinas y ensambladores 
9 Ocupaciones elementales 

Los 3 primeros grupos son asociados a alta calificación.
"""

prompt_ed_sup_calificacion_ocupacion = """El análisis se enfoca en la calificación de las ocupaciones en Chile para aquellas personas con Educación Superior completa.
Se cuenta con datos de personas y en ocupaciones de alta calificación (ed_sup_competencia_alta) y educacion superior compleya en ocupaciones de calificacion media o baja. 
Estos últimos pueden ser considerados como personas con subempleo por competencias.
En el análisis se debe considerar tanto la evolución de las cifras de subempleo por competencias (educacion superior con calificacion media o baja) como la evolución de las cifras de alta calificación (educacion superior con alta calificacion).

"""
prompt_sector_publico = """El análisis se enfoca en la calificación de las ocupaciones en Chile para aquellas personas que trabajan en el sector público.
"""
prompt_nacionalidad = """El análisis se enfoca en la nacionalidad de las personas ocupadas en Chile. Se cuenta con datos del total de personas ocupadas con nacionalidad chilena (`nacionalidad_chilena`) y personas con nacionalidad extranjera (`nacionalidad_extranjera`).
"""
prompt_sexo = """El análisis se efoca en la distribución de hombres y mujeres en el mercado laboral chileno. Se cuenta con datos del total de hombres ocupados (`hombres`) y mujeres ocupadas (`mujeres`)." \
"""
prompt_tematica = {
    "base": prompt_base,
    "dummy": prompt_dummy,
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

