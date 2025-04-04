prompt_base = """El objeto a continuación contiene datos de series temporales sobre indicadores laborales en Chile, organizados en distintas formas:

- `by_variable`: evolución temporal de cada variable.
- `by_year`: comparación de variables dentro de un mismo año.
- `diff_prev_year`: variaciones interanuales por variable.
- `pct_ocupados`: porcentaje de cada variable respecto al total de personas ocupadas (`ocupados`).

Los datos corresponden al trimestre diciembre-enero-febrero de cada año (el año indicado representa enero-febrero y diciembre del año anterior).

⚠️ **Importante**: No describas la estructura del objeto (`by_variable`, `raw`, etc.). Úsala internamente para redactar el análisis de contenido. El resultado debe ser una narrativa fluida, analítica y sin referencias al formato de los datos.
"""


prompt_estilo_general = """
Analiza la evolución de los datos considerando tres períodos:
- Prepandemia (hasta 2020)
- Pandemia (2021 y 2022)
- Postpandemia (desde 2023)

Incluye una sección final centrada en los cambios ocurridos entre 2024 y 2025, utilizando los datos de `diff_prev_year`. En esta sección, destaca qué variables explican en mayor medida la variación total en el empleo, e identifica aquellas que presentan cambios inusuales, significativos o en dirección contraria a la tendencia general.

⚠️ Todos los datos entregados, incluyendo los de 2024 y 2025, son reales, oficiales y observados. No se trata de estimaciones ni proyecciones.

Por lo tanto:
- No utilices expresiones como "se espera", "proyección", "posiblemente", "podría", "se prevé" o similares.
- Redacta como si todos los años tuvieran datos ciertos y validados, incluso los más recientes.

Redacta el análisis en español, de forma fluida, analítica y sin mencionar estructuras internas del objeto de datos (`by_variable`, `raw`, etc.).
"""


prompt_dummy = "Solo di 'Hola Mundo'."

prompt_ocupados = f"""
El indicador a analizar es `ocupados`, que representa el total de personas empleadas en el país.

{prompt_estilo_general}

Describe la evolución del empleo total en Chile, identificando los principales períodos de crecimiento o contracción. Menciona de forma agregada los momentos clave, como las caídas durante la pandemia o las recuperaciones posteriores.

Finaliza con un análisis específico de la variación entre 2024 y 2025. Compara este cambio con la evolución de años anteriores y considera si representa una aceleración, estabilización o reversión de la tendencia.
"""

prompt_informalidad = f"""
El análisis se enfoca en la informalidad laboral en Chile. Se cuenta con datos del total de personas ocupadas (`ocupados`), personas en ocupaciones formales (`formal`) y en ocupaciones informales (`informal`).

{prompt_estilo_general}

Describe cómo ha evolucionado la informalidad en términos absolutos (`valor`) y relativos (`pct_ocupados`). Usa las diferencias interanuales (`diff_prev_year`) para identificar aumentos o disminuciones relevantes. Interpreta posibles causas de estos cambios.
"""

prompt_tpi = f"""
El análisis se enfoca en el subempleo por horario asociado al indicador Tiempo Parcial Involuntario (`tpi`). Se consideran datos de personas en ocupaciones de tiempo parcial involuntario (`tpi`) y de tiempo parcial no involuntario (`no_tpi`).

{prompt_estilo_general}

Analiza la evolución del subempleo tanto en números absolutos (`valor`) como relativos (`pct_ocupados`), destacando aumentos o caídas a lo largo del tiempo. Usa las diferencias interanuales (`diff_prev_year`) para reforzar los patrones observados.
"""

prompt_ed_sup = f"""
El análisis se enfoca en el nivel educacional de las personas ocupadas en Chile. Se incluyen personas con educación superior completa (`ed_sup_completa`) y personas sin educación superior (`sin_ed_sup`).

{prompt_estilo_general}

Compara la evolución de ambos grupos usando valores absolutos (`valor`), diferencias interanuales (`diff_prev_year`) y porcentajes (`pct_ocupados`). Interpreta cambios importantes en la participación de cada grupo.
"""

prompt_calificacion_ocupacion = f"""
El análisis se enfoca en la calificación de las ocupaciones en Chile. Se consideran personas con alta calificación (`alta_calificacion`) y personas con calificación media o baja (`calificacion_media_baja`), según la CIUO 08.CL.

- Alta calificación: Grupos 1 a 3 (directivos, profesionales, técnicos)
- Media o baja: Grupos 4 a 9

{prompt_estilo_general}

Compara la evolución de ambos grupos en términos absolutos, relativos y diferencias interanuales. Analiza si hay cambios estructurales en la composición de la fuerza laboral según la calificación.
"""

prompt_ed_sup_calificacion_ocupacion = f"""
El análisis se enfoca en las personas con educación superior completa según la calificación de sus ocupaciones. Se incluyen personas con educación superior en ocupaciones de alta calificación (`ed_sup_competencia_alta`) y personas en ocupaciones de calificación media o baja (`ed_sup_competencia_media_baja`), consideradas como casos de subempleo por competencias.

{prompt_estilo_general}

Analiza cómo ha cambiado la distribución entre ocupaciones adecuadas e inadecuadas para este grupo. Usa `diff_prev_year` y `pct_ocupados` para identificar y explicar tendencias de subempleo por competencias.
"""

prompt_sector_publico = f"""
El análisis se enfoca en el empleo en el sector público. Se considera también el empleo en el **sector no público**, que incluye: sector privado, trabajadores por cuenta propia, servicio doméstico y trabajadores familiares no remunerados.

{prompt_estilo_general}

Compara la evolución de ambos sectores utilizando valores absolutos, diferencias interanuales (`diff_prev_year`) y proporciones (`pct_ocupados`). Interpreta los cambios observados y sugiere factores posibles detrás de los movimientos.
"""

prompt_nacionalidad = f"""
El análisis se enfoca en la nacionalidad de las personas ocupadas. Se incluye la cantidad de personas con nacionalidad chilena (`nacionalidad_chilena`) y extranjera (`nacionalidad_extranjera`).

{prompt_estilo_general}

Describe la evolución de ambos grupos. Analiza variaciones en su representación relativa (`pct_ocupados`) y los cambios interanuales (`diff_prev_year`).
"""

prompt_sexo = f"""
El análisis se enfoca en la distribución por sexo de las personas ocupadas. Se incluyen datos de hombres (`hombres`) y mujeres (`mujeres`) ocupadas.

{prompt_estilo_general}

Describe cómo ha evolucionado la participación laboral de cada grupo, en términos absolutos, relativos y con diferencias año a año.
"""

prompt_tematica = {
    "base": prompt_base,
    "dummy": prompt_dummy,
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
