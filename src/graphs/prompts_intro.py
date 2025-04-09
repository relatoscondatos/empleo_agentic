
prompt_estilo_general = """
El texto debe ser claro, conciso y fácil de entender para el público en general.
Evita el uso de jerga técnica y asegúrate de que cualquier término especializado esté explicado de manera sencilla.
Usa un tono neutral y objetivo, evitando opiniones personales o juicios de valor.
No uses frases largas o complejas. Mantén las oraciones cortas y directas.
Usa un lenguaje inclusivo y evita estereotipos de género o culturales.
Evita frases genéricas como “panorama claro”, “visión integral” o “presentación accesible”, ya que ya se menciona el carácter divulgativo del sitio en la introducción general.

Si la informacion es clara, presentada de manera sencilla y útil para faciltar la comprensión debiera ser una interpretación del lector y no una declaración en el documento.
"""

prompt_dummy = "Solo di 'Hola Mundo'."


prompt_introduccion_general = f"""
Redacta un texto introductorio para una página web que presenta información sobre el mercado laboral en Chile entre los años 2011 y 2025.

La información está organizada en secciones que abordan distintos aspectos del empleo:
- Evolución del empleo total en Chile
- Empleo formal e informal
- Nivel educacional de las personas ocupadas
- Calificación de las ocupaciones
- Empleo a Tiempo Parcial Involuntario (TPI)
- Subempleo
- Empleo en el sector público y no público
- Personas ocupadas según nacionalidad
- Personas ocupadas según sexo

Los datos provienen de la Encuesta Nacional de Empleo (ENE), elaborada por el Instituto Nacional de Estadísticas (INE), y corresponden al trimestre diciembre-enero-febrero de cada año. Se utiliza siempre ese mismo trimestre para evitar distorsiones estacionales asociadas a vacaciones, ciclos productivos o actividades específicas de ciertos meses.

Es importante considerar que los datos del año 2020 abarcan hasta febrero de ese año, es decir, antes de la detección del primer caso de COVID-19 en Chile (reportado en marzo). Por lo tanto, en este análisis, el año 2020 se considera parte del período **prepandemia**.

El análisis se enfoca exclusivamente en las personas ocupadas, es decir, aquellas que estaban trabajando en el período de referencia. No se abordan indicadores como el desempleo o la participación laboral, sino que se explora cómo ha cambiado la **composición del empleo ocupado** en distintos contextos.

Las narrativas fueron generadas mediante un modelo de lenguaje de inteligencia artificial, procurando mantener un enfoque claro, accesible y riguroso. Este sitio tiene un carácter exploratorio y divulgativo, sin fines comerciales, y busca facilitar el acceso a datos públicos relevantes para comprender mejor la evolución del empleo en Chile.

{prompt_estilo_general}

**Importante**: El texto debe presentarse como introducción al contenido del sitio, no como una recomendación ni como una sugerencia para su desarrollo. No uses expresiones como "Aquí tienes un texto" o "Te recomiendo". Solo redacta la introducción que irá en la página.
"""

prompt_ocupados = f"""
Redacta un texto introductorio para la sección que presenta la evolución del número total de personas ocupadas a lo largo del tiempo.

Explica que permite observar cambios generales en el nivel de empleo entre los distintos períodos: prepandemia, pandemia y postpandemia.

Evita expresiones que aludan al lector o califiquen el contenido. El tono debe ser institucional, objetivo y descriptivo.

{prompt_estilo_general}
"""

prompt_informalidad = f"""
Redacta un texto introductorio para la sección que presenta datos sobre empleo formal e informal, incluyendo el total de personas ocupadas, personas en empleos formales y personas en empleos informales.

Aclara que esta información se encuentra disponible a partir del trimestre julio-agosto-septiembre de 2017 , cuando el INE comenzó a publicar esta desagregación de forma sistemática.

Incluye una breve explicación sobre qué se considera una ocupación informal:
(Según un documento del INE esta es la definición aplicada para Chile: "Son todos aquellos Asalariados o Trabajadores del Servicio Doméstico que no
cuentan con cotizaciones de salud (Isapre o Fonasa) y previsión social (AFP) por
concepto de su vínculo laboral con un Empleador. Asimismo, se consideran como
Ocupados Informales por definición a todos los Familiares no Remunerados del
Hogar, además de los Trabajadores por Cuenta Propia y Empleadores propietarios
de una unidad económica del Sector Informal")

Indica que los datos permiten analizar la evolución del empleo formal e informal en distintos contextos: prepandemia, pandemia y postpandemia.

Evita expresiones personales o dirigidas al lector. El tono debe ser institucional, claro y descriptivo.

{prompt_estilo_general}
"""

prompt_tpi = f"""
Redacta un texto introductorio para la sección que presenta datos sobre personas en empleos de Tiempo Parcial Involuntario (TPI), aquellas que no califican como TPI (porque trabajan jornada completa o parcial voluntaria), y el total de personas ocupadas.

Aclara que el TPI corresponde a personas que trabajan menos de 30 horas semanales y que desean trabajar más horas, pero no pueden hacerlo por razones ajenas a su voluntad. Este indicador se utiliza en Chile para medir el subempleo por insuficiencia horaria.

Explica que, según la definición de la Organización Internacional del Trabajo (OIT), el subempleo visible se refiere a personas ocupadas que trabajan menos horas de las que desean y están disponibles para trabajar más, lo que indica una subutilización de su capacidad laboral. Aunque la OIT no especifica un umbral de horas concreto, en el caso chileno se aplica el criterio de menos de 30 horas semanales para definir el tiempo parcial involuntario.

Señala que el análisis de este indicador permite observar situaciones de subutilización de la fuerza laboral, lo que puede reflejar rigideces en el mercado de trabajo o falta de oportunidades suficientes para empleos de jornada completa.

El texto debe tener un tono institucional, descriptivo y objetivo. Evita expresiones dirigidas al lector o juicios de valor sobre los datos.

{prompt_estilo_general}
"""

prompt_edu = f"""
Redacta un texto introductorio para la sección que compara personas ocupadas según su nivel de educación (superior, media, básica o sin educación básica completa).

El tono debe ser institucional y descriptivo, sin calificaciones ni referencias al lector.

{prompt_estilo_general}
"""

prompt_calificacion_ocupacion = f"""
Redacta un texto introductorio para la sección que analiza la calificación de las ocupaciones según la Clasificación Internacional Uniforme de Ocupaciones (CIUO), usada por el INE.

Entre los años 2011 y 2017 se utilizó la versión CIUO-88, y desde 2018 en adelante se emplea la versión CIUO-08. En ambos casos, las ocupaciones se agrupan en 10 grandes grupos.

Para efectos de este análisis, se ha realizado una **agrupación simplificada en tres niveles de calificación**:
- **Alta calificación**: Grupos 1 a 3 (directivos, profesionales y técnicos).
- **Calificación media**: Grupos 4 a 8, que incluyen empleos como personal administrativo, vendedores, trabajadores de servicios, operarios, conductores y agricultores.
- **Calificación baja**: Grupo 9, correspondiente a ocupaciones elementales.

El grupo 10, correspondiente a ocupaciones no clasificadas, no se incluye en el análisis, ya que representa una proporción menor al 1% de los casos.

⚠️ Dado que se utilizan dos versiones distintas de la CIUO en la serie temporal, es importante advertir que **pueden existir diferencias en la codificación entre CIUO-88 y CIUO-08**, lo que podría afectar la comparabilidad directa de algunos grupos entre los años anteriores y posteriores a 2018. Además, la división en tres niveles de calificación **no forma parte de la estructura oficial de la CIUO**, sino que corresponde a una simplificación adoptada exclusivamente para facilitar el análisis.

El texto debe mantener un tono descriptivo, neutral y profesional.

{prompt_estilo_general}
"""

prompt_subempleo_general = f"""
Redacta un texto introductorio para una sección que analiza el subempleo en el mercado laboral chileno desde una perspectiva integral, considerando dos dimensiones complementarias:

1. El **subempleo por insuficiencia de horas**, medido a través del indicador de Tiempo Parcial Involuntario (TPI), que identifica a personas ocupadas que trabajan menos de 30 horas semanales y desean trabajar más, pero no pueden hacerlo por motivos ajenos a su voluntad.

2. El **subempleo por competencias**, que corresponde a personas con educación superior que están empleadas en ocupaciones de calificación media o baja, es decir, en trabajos que no requieren el nivel formativo que poseen.

Ambas dimensiones conforman el **subempleo total**, entendido como la suma de personas que enfrentan limitaciones tanto en la cantidad de horas trabajadas como en la adecuación entre su nivel educativo y el tipo de ocupación.

Aclara que el concepto de subempleo por competencias ha sido difundido en Chile por el economista Juan Bravo, actual investigador del Observatorio del Contexto Económico de la Universidad Diego Portales (OCEC UDP) y exmiembro de Clapes UC. Si bien esta noción no forma parte de los indicadores oficiales del Instituto Nacional de Estadísticas (INE), ha sido utilizada en diversos análisis académicos y de política pública. En este caso, su uso es exploratorio y se basa en datos públicos disponibles.

Indica además que el análisis incluye a personas ocupadas que **no presentan condiciones de subempleo**, diferenciando entre quienes tienen educación superior y desempeñan ocupaciones de alta calificación, y quienes no tienen educación superior. Esta comparación permite observar cómo ha evolucionado la estructura del empleo más allá del subempleo, aportando una visión más completa sobre la transformación del mercado laboral chileno.

El tono del texto debe ser institucional, claro y descriptivo. No deben incluirse juicios de valor, recomendaciones ni expresiones dirigidas al lector.

{prompt_estilo_general}
"""

prompt_sector_publico = f"""
Redacta un texto introductorio para la sección que presenta la evolución del empleo en el sector público y en el sector no público.

Aclara que el sector no público incluye empleo en el sector privado, por cuenta propia, en servicio doméstico y en trabajos familiares no remunerados.

Evita expresiones dirigidas al lector o calificativos sobre el contenido. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""

prompt_nacionalidad = f"""
Redacta un texto introductorio para la sección que presenta la distribución de personas ocupadas según su nacionalidad (chilena o extranjera).

El texto debe evitar expresiones subjetivas o dirigidas al lector. El tono debe ser objetivo e institucional.

{prompt_estilo_general}
"""

prompt_sexo = f"""
Redacta un texto introductorio para la sección que presenta la evolución del empleo según sexo, con cifras de hombres y mujeres ocupadas.

Evita expresiones personales, calificativas o dirigidas al lector. El tono debe ser institucional y descriptivo.

{prompt_estilo_general}
"""

prompt_tematica = {
    "dummy": prompt_dummy,
    "introduccion_general": prompt_introduccion_general,
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
