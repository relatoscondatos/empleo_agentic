prompt_base = """El objeto a continuación contiene datos de series temporales sobre indicadores laborales en Chile, organizados en distintas formas:

- `by_variable`: evolución temporal de cada variable.
- `by_year`: comparación de variables dentro de un mismo año.
- `diff_prev_year`: variaciones interanuales por variable.
- `pct_ocupados`: porcentaje de cada variable respecto al total de personas ocupadas (`ocupados`).

Los datos corresponden al trimestre diciembre-enero-febrero de cada año (el año indicado representa enero-febrero y diciembre del año anterior).

⚠️ **Importante**: No describas la estructura del objeto (`by_variable`, `raw`, etc.). Úsala internamente para redactar el análisis de contenido. El resultado debe ser una narrativa fluida, analítica y sin referencias al formato de los datos.
"""


prompt_estilo_general = """
Analiza la evolución de los datos considerando cuatro bloques temporales, siguiendo esta estructura:

1. **Período Prepandemia (hasta 2020)**  
   Describe la evolución de las variables antes del inicio de la pandemia de COVID-19. Identifica tendencias generales (crecimiento, estancamiento, retroceso) sin detallar año por año. Resume los principales cambios de forma agregada.  
   Aclara que los datos del año 2020 corresponden al trimestre diciembre–enero–febrero, por lo que **representan un período anterior a la pandemia en Chile**.

2. **Período Pandemia (2021 y 2022)**  
   Describe los efectos de la pandemia en el empleo y cómo se manifestaron en los datos. Menciona caídas abruptas, recuperaciones parciales o transformaciones del mercado laboral. Relaciona con el contexto de restricciones sanitarias o cambios en la actividad económica.

3. **Período Postpandemia (desde 2023 a 2025)**  
   Analiza si las tendencias anteriores se mantienen, revierten o cambian. Señala indicios de recuperación, estabilización o transformación estructural. Considera los primeros años postpandemia como una etapa de ajuste.

4. **Cambios entre 2024 y 2025**  
   Incluye una sección específica para los cambios interanuales más recientes. Usa los datos de `diff_prev_year` para señalar las variaciones de cada variable entre 2024 y 2025 (recondeando de manera consistente con las otras secciones). Comenta qué variables contribuyen más al cambio total y contextualiza su importancia relativa usando `pct_ocupados` cuando sea pertinente.

Todos los datos entregados, incluyendo los años 2024 y 2025, son reales, oficiales y observados.  
No se trata de estimaciones ni proyecciones. Por lo tanto:

- **No utilices** expresiones como “se espera que”, “proyección”, “estimación”, “posiblemente”, “podría”, “se prevé” u otras similares.
- Redacta como si todos los años tuvieran datos definitivos y validados.

Cuando se utilicen porcentajes (`pct_ocupados`), recuerda que se refieren a la proporción respecto del total de personas ocupadas (`ocupados`).

Para mejorar la legibilidad, **varía la redacción inicial de cada bloque temporal**. Evita comenzar todos los párrafos con la misma estructura.

El tono debe ser profesional, explicativo y objetivo, similar al de una publicación institucional.  
**No incluyas títulos explícitos** como “Período Prepandemia” o “Cambios 2024–2025” dentro del texto. La narrativa debe fluir de forma natural, sin encabezados.  
**No te dirijas al lector** con frases como “en esta sección encontrarás” ni uses expresiones personales o promocionales.

**Evita expresiones poco comunes o marcadamente técnicas** que puedan dificultar la comprensión por parte del público general en Chile. Por ejemplo, **no uses el adjetivo “acusado” para describir cambios**. Prefiere términos más accesibles como “notable”, “marcado”, “significativo”, “claro” o similares. Puedes usar también adjetivos como “leve”, “moderado” o “considerable” cuando corresponda.

**Formato de números y cantidades**:

- Todos los valores deben ser tratados como cifras absolutas.  
Sobre 1.000.000 personas, usa la forma redondeada aproximado a la decena de miles:
9,45 millones
13,33 millones

Entre 100.000 y 1.000.000 personas, usa la forma redondeada aproximando a la decena de mil:
530 mil
270 mil (evita "270.300")

Entre 10.000 y 100.000 personas, usa la forma redondeada aproximando a los miles:
87 mil (evita "87.266" o "87.000")
13 mil

Entre 1.000 y 10.000 personas, usa la forma redondeada aproximando a la centena:
8900
1200

Bajo 1.000 usa cifras exactas
837
24


Para porcentajes usa un decimal
34,5%
9,7%

Puedes mencionar 330 mil personas, pero evita figuras como  234.567 personas.

- Usa el punto como separador miles y la coma como separador decimal.

- Siempre evita notación científica y expresiones como “aproximadamente 0.42 millones”.

- Para porcentajes, indica claramente que corresponden al total de personas ocupadas.

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
El análisis se enfoca en el subempleo por horario en Chile, a partir del indicador de Tiempo Parcial Involuntario. Se cuenta con datos sobre el total de personas ocupadas, el total de personas en empleos clasificados como tiempo parcial involuntario y el total de personas que no se encuentran en esa categoría.

Ten presente que las personas "no clasificadas como tiempo parcial involuntario" pueden incluir tanto personas con jornada completa como personas con tiempo parcial voluntario. Por lo tanto, **no deben ser interpretadas como un grupo homogéneo ni como equivalentes a empleos de tiempo parcial voluntario**.

{prompt_estilo_general}

Analiza cómo ha evolucionado el subempleo por horario a lo largo del tiempo, prestando atención a:

- La evolución del número de personas en empleos de tiempo parcial involuntario (subempleo por horas)
- La proporción de este grupo respecto del total de ocupados
- Las diferencias interanuales (`diff_prev_year`) y los porcentajes (`pct_ocupados`) disponibles en los datos
- Cambios notables en el último año (2024–2025)

Evita usar directamente etiquetas como `tpi` o `no_tpi` en la narrativa. En su lugar, utiliza descripciones comprensibles como "tiempo parcial involuntario" o "personas fuera de esa categoría".
"""

prompt_edu = f"""
El análisis se enfoca en el nivel educacional de las personas ocupadas en Chile. Se incluyen personas con educación superior completa (`ed_sup`), personas con educación media ('ed_media'), personas con educación básica (ed_básica) y personas sin educación básica completa (sin_ed_basica).

{prompt_estilo_general}

Compara la evolución de ambos grupos usando valores absolutos (`valor`), diferencias interanuales (`diff_prev_year`) y porcentajes (`pct_ocupados`). Interpreta cambios importantes en la participación de cada grupo.
"""

prompt_calificacion_ocupacion = f"""
El análisis se enfoca en la calificación de las ocupaciones en Chile. Se consideran personas con alta calificación (`alta_calificacion`), personas con calificación media (`calificacion_media`) y personas con calificación baja (`calificacion_baja`), según la CIUO 08.CL.

- Alta calificación: Grupos 1 a 3 (directivos, profesionales, técnicos)
- Calificación Media: Grupos 4 a 8 (personal administrativo, vendedores, trabajadores de servicios, operarios, conductores, agricultores)
- Calificación Baja: Grupoo 9 (ocupaciones elementales)

{prompt_estilo_general}

Compara la evolución de ambos grupos en términos absolutos, relativos y diferencias interanuales. Analiza si hay cambios estructurales en la composición de la fuerza laboral según la calificación.
"""

prompt_subempleo_general = f"""
El análisis se enfoca en el subempleo total en Chile. Este concepto agrupa dos fenómenos laborales que ya han sido abordados en secciones anteriores:

- El **subempleo por insuficiencia horaria**, también conocido como Tiempo Parcial Involuntario (TPI), que corresponde a personas que trabajan menos de 30 horas semanales y desean trabajar más horas, pero no encuentran una oportunidad para hacerlo.

- El **subempleo por competencias**, que corresponde a personas con educación superior empleadas en ocupaciones de calificación media o baja, es decir, en trabajos que no requieren el nivel educativo que poseen.

La suma de ambos grupos permite observar la evolución del **subempleo total**, que está disponible como variable agregada en los datos (`subempleo_total`).

Analiza cómo ha evolucionado este indicador en los tres períodos definidos (prepandemia, pandemia y postpandemia), e incluye una descripción específica de los cambios más recientes entre los años 2024 y 2025. Utiliza tanto los valores absolutos como las diferencias interanuales (`diff_prev_year`) y las proporciones respecto al total de personas ocupadas (`pct_ocupados`) para contextualizar los cambios observados.

🔍 Además, incorpora una sección final que describa los cambios más recientes en los grupos **que no califican como subempleo**, en particular:
- Personas con educación superior en ocupaciones de alta calificación (`ed_sup_alta_calificacion_excluyendo_subempleo_horas`)
- Personas sin educación superior sin subempleo (`sin_ed_sup_excluyendo_subempleo_horas`)


Este análisis complementario debe mostrar si ha habido aumentos o disminuciones en estos grupos entre 2024 y 2025 (indicar la cifras absolutas de cambio). La intención es proporcionar un contexto más amplio que permita interpretar de manera más completa el cambio neto en el empleo, considerando tanto el subempleo como otras formas de ocupación.

Evita interpretaciones simplistas del tipo "todo el empleo nuevo es subempleo", y no emitas juicios de valor ni conclusiones categóricas. El objetivo es entregar una descripción clara, equilibrada y basada en evidencia sobre cómo ha cambiado el empleo en su conjunto.

{prompt_estilo_general}
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
    "edu": prompt_edu,
    "calificacion_ocupacion": prompt_calificacion_ocupacion,
    "subempleo_general": prompt_subempleo_general,
    "sector_publico": prompt_sector_publico,
    "nacionalidad": prompt_nacionalidad,
    "sexo": prompt_sexo,
}
