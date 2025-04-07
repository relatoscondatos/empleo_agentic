# Evolución del empleo en Chile (2011–2025)  
## Información técnica

Esta página presenta un análisis exploratorio de cómo ha cambiado la composición del empleo en Chile entre los años 2011 y 2025, usando datos oficiales y métodos reproducibles. A continuación, se detalla el origen de los datos, el procesamiento realizado y las definiciones utilizadas para construir los indicadores presentados.

---

## Fuente de los datos

Los datos provienen de la **Encuesta Nacional de Empleo (ENE)**, elaborada por el **Instituto Nacional de Estadísticas (INE)**. Esta encuesta es la fuente oficial de estadísticas laborales en Chile y entrega información detallada sobre las personas ocupadas, desocupadas y fuera de la fuerza de trabajo.

Para este análisis, se utiliza la base de datos publicada por el INE en su sitio oficial:

🔗 [Serie Ocupación y Desocupación - INE](https://www.ine.gob.cl/estadisticas/sociales/mercado-laboral/ocupacion-y-desocupacion)

---

## Periodo y cobertura temporal

El análisis considera el trimestre **diciembre–enero–febrero** de cada año, lo que permite comparar años completos evitando distorsiones por estacionalidad. Este enfoque asegura una base homogénea para evaluar tendencias de mediano y largo plazo.

Se incluyen los datos desde el **trimestre diciembre 2010 – febrero 2011** hasta el **trimestre diciembre 2024 – febrero 2025**.

---

## Procesamiento y metodología

Los datos fueron descargados en formato CSV y convertidos a formato Parquet para facilitar su procesamiento. Luego, se aplicaron transformaciones utilizando consultas SQL y scripts en Python para obtener los indicadores agregados que se presentan en las visualizaciones.

Cada fila del conjunto de datos corresponde a una persona, y cada persona tiene asociado un factor de expansión (`fact_cal`) que permite estimar el total de la población ocupada.

---

## Variables calculadas

Se construyeron una serie de indicadores, entre ellos:

### 1. Personas ocupadas  
Suma del total de personas que declararon estar trabajando en la semana de referencia (CAES 1 a 7).

### 2. Empleo formal e informal  
- **Formal**: Personas que cotizan en salud y previsión.
- **Informal**: Personas que no cotizan, o que trabajan en sectores informales (según definición del INE).

### 3. Subempleo por horario (TPI)  
- **TPI**: Personas que trabajan menos de 30 horas semanales, desean trabajar más y están disponibles, pero no lo logran por causas ajenas a su voluntad.

### 4. Nivel educacional  
Agrupado en cuatro tramos:
- Educación superior completa (CFT, IP, universidad, postgrados)
- Educación media completa o superior incompleta
- Educación básica completa o media incompleta
- Sin educación básica completa

También se incluye un desglose más detallado dentro de la educación superior.

### 5. Calificación de las ocupaciones  
Según la **Clasificación Internacional Uniforme de Ocupaciones (CIUO)**:
- **Alta calificación**: Grupos 1 a 3 (directivos, profesionales, técnicos)
- **Media o baja**: Grupos 4 a 9  
(Grupo 10, ocupaciones no clasificadas, no se considera)

### 6. Sector público y no público  
- **Sector público**: Código 4 en la variable `categoria_ocupacion`
- **No público**: Incluye sector privado, cuenta propia, servicio doméstico, y trabajo familiar no remunerado

### 7. Nacionalidad y sexo  
- Clasificación entre personas chilenas y extranjeras  
- Clasificación entre hombres y mujeres ocupados

---

## Indicadores combinados

### Educación y calificación  
Se identifican personas con educación superior empleadas en:
- Ocupaciones de alta calificación  
- Ocupaciones de calificación media o baja

También se calcula el mismo cruce para personas sin educación superior.

### Subempleo por competencias y/o por horas  
Se construyen tres categorías mutuamente excluyentes:
- Subempleo por competencias  
- Subempleo por insuficiencia horaria  
- Personas con ambos tipos de subempleo

Se incluye también una estimación del **subempleo total** (unión de ambos).

---

## Reproducibilidad

Todo el procesamiento fue realizado con herramientas de código abierto. El código fuente está disponible en un repositorio público (si aplica), lo que permite que cualquier persona interesada pueda revisar y reproducir el análisis realizado.
