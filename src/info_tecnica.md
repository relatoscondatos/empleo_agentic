# Evolución del empleo en Chile (2011–2025)  
## Información técnica

Esta página presenta entrega información técnica sobre la cosntrucción de la página [Evolución del empleo en Chile  de 2011 a 2025](.). A continuación, se detalla el origen de los datos, el procesamiento realizado y las definiciones utilizadas para construir los indicadores presentados.

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

## Variables utilizadas

Se construyen indicadores a partir de variables disponibles en los microdatos de la ENE. Las principales dimensiones consideradas son:

### Personas ocupadas  
**Criterio**: `cae_especifico` entre 1 y 7  
```
WHERE cae_especifico BETWEEN 1 AND 7
```

---

### Empleo formal e informal  
**Variable**: `ocup_form`  
- Formal: `ocup_form = 1`  
- Informal: `ocup_form = 2`  
```
SUM(CASE WHEN ocup_form = 1 THEN fact_cal ELSE 0 END) as formal
SUM(CASE WHEN ocup_form = 2 THEN fact_cal ELSE 0 END) as informal
```

---

### Subempleo por horario (TPI)  
**Variable**: `tpi`  
- TPI: `tpi = 1`  
- No TPI: `tpi = 0`  
```
SUM(CASE WHEN tpi = 1 THEN fact_cal ELSE 0 END) as tpi
SUM(CASE WHEN tpi = 0 THEN fact_cal ELSE 0 END) as no_tpi
```

---

### Nivel educacional  
**Variables**: `nivel`, `termino_nivel`  
```
-- Educación superior completa (CFT, IP, universidad, postgrados)
SUM(CASE 
    WHEN (nivel BETWEEN 7 AND 9 AND termino_nivel = 1) 
        OR (nivel BETWEEN 10 and 12)
    THEN fact_cal 
    ELSE 0 
END) AS ed_sup,

-- Educación media completa o superior incompleta
SUM(CASE 
    WHEN ((nivel BETWEEN 4 AND 6 OR nivel = 14 ) AND termino_nivel = 1) 
        OR (nivel BETWEEN 7 AND 9 AND termino_nivel <> 1) 
    THEN fact_cal 
    ELSE 0 
END) AS ed_media,
    
-- Educación básica completa o media incompleta
SUM(CASE 
    WHEN (nivel = 3 AND termino_nivel = 1) 
        OR (nivel IN (4, 5, 6, 14) AND termino_nivel <> 1)
    THEN fact_cal 
    ELSE 0 
END) AS ed_basica, 

-- Sin Educación básica completa
SUM(CASE 
    WHEN (nivel = 3 AND termino_nivel <> 1) OR (nivel NOT BETWEEN 3 AND 14)
    THEN fact_cal 
    ELSE 0 
END) AS sin_ed_basica,

```
---

### Calificación de la ocupación  
**Variables**: `b1` (CIUO-08) y `b1_ciuo88` (CIUO-88)  según el año correspondiente 
```
SUM(CASE WHEN  b1 BETWEEN 1 AND 3 THEN fact_cal else 0 END) as alta_calificacion,
SUM(CASE WHEN  b1 BETWEEN 4 AND 9 THEN fact_cal else 0 END) as calificacion_media_baja,
SUM(CASE WHEN  b1 BETWEEN 4 AND 8 THEN fact_cal else 0 END) as calificacion_media,
SUM(CASE WHEN  b1 = 9 THEN fact_cal else 0 END) as calificacion_baja,
```


---

### Sector público  
**Variable**: `categoria_ocupacion`  

```
SUM(CASE WHEN  categoria_ocupacion = 4 THEN fact_cal else 0 END) as sector_publico,
SUM(CASE WHEN  categoria_ocupacion <> 4 THEN fact_cal else 0 END) as no_sector_publico,
```

---

### Nacionalidad  
**Variable**: `nacionalidad`  
```
SUM(CASE WHEN  nacionalidad = 152 THEN fact_cal else 0 END) as nacionalidad_chilena,
SUM(CASE WHEN  nacionalidad <> 152 THEN fact_cal else 0 END) as nacionalidad_extranjera,
```

---

### Sexo  
**Variable**: `sexo`  
```
SUM(CASE WHEN  sexo = 1 THEN fact_cal else 0 END) as hombre,
SUM(CASE WHEN  sexo = 2 THEN fact_cal else 0 END) as mujer,
```

---

## Indicadores combinados

### Educación y calificación  
Se calcula el cruce entre nivel educacional y calificación ocupacional para distinguir:

- Personas con educación superior en ocupaciones de alta calificación  
- Personas con educación superior en ocupaciones de media o baja calificación  
- Personas sin educación superior, también clasificadas por calificación de la ocupación

```
/* Ed sup según calificación de ocupación */
SUM(CASE WHEN  ((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 and 12)) AND b1 BETWEEN 1 AND 3 THEN fact_cal else 0 END) as ed_sup_competencia_alta,
SUM(CASE WHEN  ((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 and 12)) AND b1 BETWEEN 4 AND 9 THEN fact_cal else 0 END) as ed_sup_competencia_media_baja,

/* Sin Ed sup segun calificacion de ocupacion */
SUM(CASE WHEN (NOT ((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 and 12))) AND b1 BETWEEN 1 AND 3 THEN fact_cal else 0 END) as sin_ed_sup_competencia_alta,
SUM(CASE WHEN (NOT ((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 and 12))) AND b1 BETWEEN 4 AND 9 THEN fact_cal else 0 END) assin_ed_sup_competencia_media_baja,
```

---

### Subempleo por competencias y/u horas  
Se construyen tres categorías mutuamente excluyentes:

- Subempleo por **competencias**:  
```
SUM(CASE WHEN  ((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 and 12)) AND b1 BETWEEN 4 AND 9 THEN fact_cal else 0 END) as ed_sup_competencia_media_baja,
```

- Subempleo por **horas**:  
```
SUM(CASE WHEN tpi = 1 THEN fact_cal ELSE 0 END) as tpi

```

- Subempleo combinado: personas que cumplen ambas condiciones.
```
SUM(CASE 
    WHEN (((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12)) AND b1_int BETWEEN  4 AND 9) 
    AND TPI <> 1 THEN fact_cal  
    ELSE 0 
END) as subempleo_calificaciones_excluyendo_subempleo_horas,
SUM(CASE 
    WHEN (((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12)) AND b1_int BETWEEN  4 AND 9) 
    AND TPI = 1 
    THEN fact_cal  
    ELSE 0 
END) as subempleo_calificaciones_y_subempleo_horas,
SUM(CASE 
    WHEN NOT (((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12)) AND b1_int BETWEEN  4 AND 9) 
    AND TPI = 1 
    THEN fact_cal  
    ELSE 0 
END) as subempleo_horas_excluyendo_subempleo_calificaciones,
SUM(CASE 
    WHEN  (((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12)) AND b1_int BETWEEN  1 AND 3) 
    AND TPI <> 1 
    THEN fact_cal  
    ELSE 0 
END) as ed_sup_alta_calificacion_excluyendo_subempleo_horas,
SUM(CASE 
    WHEN  (NOT((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12))) 
    AND TPI <> 1 
    THEN fact_cal  
    ELSE 0 
END) as sin_ed_sup_excluyendo_subempleo_horas,
```  
- Subempleo total: unión de todos los subempleos  
```
SUM(CASE 
    WHEN 
        (((nivel BETWEEN 7 AND 9 AND termino_nivel = 1) OR (nivel BETWEEN 10 AND 12)) AND b1_int BETWEEN  4 AND 9) 
        OR TPI = 1 
    THEN fact_cal  
    ELSE 0 
END) as subempleo_total,
```
---

## Plataforma y herramientas utilizadas

Esta página ha sido desarrollada con el **Observable Framework**, utilizando la librería de gráficos [**Plot**](https://observablehq.com/plot) para la visualización de datos.

Los datos se procesan mediante un **agente LangGraph** que ejecuta consultas SQL y transforma los resultados en archivos JSON mediante Python. Estos archivos son cargados en la página a través de *data loaders* personalizados.

Los textos introductorios y narrativas fueron generados automáticamente con el modelo de lenguaje **GPT-4o** de OpenAI, mediante otro agente LangGraph encargado de orquestar la consulta de datos y la redacción de contenido.

---

## Reproducibilidad

El proyecto utiliza herramientas de código abierto. El código de procesamiento y configuración puede ponerse a disposición para su revisión en futuras versiones. Si deseas conocer más detalles técnicos, visita la sección:  
👉 [Información técnica detallada](./info_tecnica)