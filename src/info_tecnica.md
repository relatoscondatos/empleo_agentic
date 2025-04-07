# Evolución del empleo en Chile (2011–2025)  
## Información técnica

Este sitio presenta un análisis exploratorio sobre cómo ha cambiado la composición del empleo en Chile entre los años 2011 y 2025, utilizando datos oficiales y métodos reproducibles. A continuación, se detallan las fuentes de información, los procesos de tratamiento de datos, las definiciones utilizadas para construir los indicadores y la arquitectura técnica del sistema.

---

## Fuentes de datos

Los datos provienen de la **Encuesta Nacional de Empleo (ENE)**, elaborada por el **Instituto Nacional de Estadísticas (INE)**. Esta encuesta es la fuente oficial de estadísticas laborales en Chile y entrega información sobre personas ocupadas, desocupadas y fuera de la fuerza de trabajo.

El conjunto de datos utilizado corresponde a los microdatos publicados por el INE en su sitio web:

🔗 [Serie Ocupación y Desocupación - INE](https://www.ine.gob.cl/estadisticas/sociales/mercado-laboral/ocupacion-y-desocupacion)

---

## Periodo de análisis

El análisis se basa exclusivamente en los datos correspondientes al trimestre **diciembre–enero–febrero** de cada año. Esta elección permite comparar años completos en condiciones similares, evitando distorsiones por estacionalidad asociadas a vacaciones o ciclos productivos específicos.

Se cubre el período desde el **trimestre diciembre 2010 – febrero 2011** hasta el **trimestre diciembre 2024 – febrero 2025**.

---

## Procesamiento de datos

Los archivos CSV publicados por el INE fueron convertidos a formato Parquet para facilitar su procesamiento. Luego, se aplicaron transformaciones utilizando consultas SQL y scripts en Python para generar tablas agregadas con el número total de personas ocupadas según diversas características.

Cada fila representa una persona encuestada, y se utiliza el factor de expansión `fact_cal` para estimar la población total.

---

## Variables utilizadas

Se construyen indicadores a partir de variables disponibles en los microdatos de la ENE. Las principales dimensiones consideradas son:

### Personas ocupadas
- Criterio: `cae_especifico` entre 1 y 7  
```sql
WHERE cae_especifico BETWEEN 1 AND 7
```

### Empleo formal e informal
- Variable: `ocup_form`  
```sql
ocup_form = 1  → Formal  
ocup_form = 2  → Informal
```

### Subempleo por horario (TPI)
- Variable: `tpi`  
```sql
tpi = 1 → Tiempo parcial involuntario  
tpi = 0 → No TPI
```

### Nivel educacional
- Variables: `nivel`, `termino_nivel`  
Se definen rangos para agrupar educación básica, media, superior e incompleta.

### Calificación de la ocupación
- Variable: `b1` o `b1_ciuo88`, según el año  
```sql
b1_int = CASE WHEN ano_trimestre >= 2018 THEN b1 ELSE b1_ciuo88 END
```
- Alta calificación: grupos 1 a 3  
- Media/baja: grupos 4 a 9

### Sector público
- Variable: `categoria_ocupacion`  
```sql
categoria_ocupacion = 4 → Sector público  
categoria_ocupacion ≠ 4 → No público
```

### Nacionalidad
- Variable: `nacionalidad`  
```sql
nacionalidad = 152 → Chilena  
nacionalidad ≠ 152 → Extranjera
```

### Sexo
- Variable: `sexo`  
```sql
sexo = 1 → Hombre  
sexo = 2 → Mujer
```

---

## Indicadores combinados

Se han construido variables adicionales que permiten analizar combinaciones de dimensiones relevantes:

### Educación y calificación
- Personas con educación superior en:
  - Ocupaciones de alta calificación
  - Ocupaciones de media o baja calificación
- Mismo cruce para personas sin educación superior

### Subempleo total
Incluye a personas que presentan:
- Subempleo por competencias  
- Subempleo por insuficiencia horaria  
- Ambos tipos simultáneamente

También se consideran los grupos que no califican como subempleo, distinguiendo entre:
- Personas con educación superior en ocupaciones de alta calificación  
- Personas sin educación superior y sin subempleo

---

## Arquitectura técnica y herramientas utilizadas

Este sitio ha sido desarrollado con el framework [Observable Framework](https://observablehq.com/framework), que permite integrar visualizaciones interactivas, análisis de datos y narrativas generadas automáticamente.

### Visualizaciones  
Los gráficos fueron construidos utilizando [Plot](https://observablehq.com/plot), una herramienta del ecosistema Observable, diseñada para generar visualizaciones claras, accesibles y personalizables.

### Generación de datos  
Para cada sección, se utiliza un agente basado en [LangGraph](https://www.langgraph.dev/), que ejecuta consultas SQL específicas para seleccionar y agregar las variables correspondientes. Los datos resultantes se procesan en Python y se entregan en formato JSON mediante un módulo *data generator*, que alimenta los *data loaders* definidos en la página Observable.

### Generación de contenido  
Tanto las descripciones introductorias como las narrativas analíticas son generadas por un modelo de lenguaje (GPT-4o de OpenAI), bajo la coordinación de un agente LangGraph que orquesta la lectura de datos, el análisis de tendencias y la redacción de textos, de acuerdo con directrices específicas predefinidas para mantener consistencia, claridad y rigurosidad.