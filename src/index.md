---

---

```js
//display(sourceDataForCharts)
```

# Evolución del empleo en Chile  de 2011 a 2025
## Análisis de datos de la Encuesta Nacional de Empleo (ENE) para el trimestre diciembre-enero-febrero.

```js
md`${introIntroduccionGeneral}`
```

## Evolución del empleo total en Chile
```js
md`${introOcupados}`
```

<div class="card">
<div>${chartOcupados}</div>
</div><!--card-->

<div class="card">
<div>${chartOcupados_diferencias}</div>
</div><!--card-->


```js
md`${narrativaOcupados}`
```

## Empleo formal e informal
```js
md`${introInformalidad}`
```
<div class="card">
<div>${chartInformalidad}</div>
</div><!--card-->

<div class="card">
<div>${chartInformalidad_porcentaje}</div>
</div><!--card-->

<div class="card">
<div>${chartInformalidad_diferencias}</div>
</div><!--card-->



```js
md`${narrativaInformalidad}`
```




## Nivel educacional de las personas ocupadas
```js
md`${introEdu}`
```
<div class="card">
<div>${chartEdu}</div>
</div><!--card-->
<div class="card">
<div>${chartEdu_porcentaje}</div>
</div><!--card-->
<div class="card">
<div>${chartEdu_diferencias}</div>
</div><!--card-->


```js
md`${narrativaEdu}`
```


## Nivel de calificación de las ocupaciones
```js
md`${introCalificacionOcupacion}`
```
<div class="card">
<div>${chartCalificacionOcupacion}</div>
</div><!--card-->
<div class="card">
<div>${chartCalificacionOcupacion_porcentaje}</div>
</div><!--card--><div class="card">
<div>${chartCalificacionOcupacion_diferencias}</div>
</div><!--card-->



```js
md`${narrativaCalificacionOcupacion}`
```


## Empleo a Tiempo Parcial Involuntario (TPI)

```js
md`${introTPI}`
```

<div class="card">
<div>${chartTPI}</div>
</div><!--card-->

<div class="card">
<div>${chartTPI_porcentaje}</div>
</div><!--card-->

<div class="card">
<div>${chartTPI_diferencias}</div>
</div><!--card-->



```js
md`${narrativaTPI}`
```

## Subempleo por competencias y/o insuficiencia horaria 
```js
md`${introSubempleoGeneral}`
```

<div class="card">
<div>${chartSubempleoGeneral}</div>
</div><!--card-->

<div class="card">
<div>${cchartSubempleoGeneral_porcentaje}</div>
</div><!--card-->
<div class="card">
<div>${chartSubempleoGeneral_diferencias}</div>
</div><!--card-->

```js
md`${narrativaSubempleoGeneral}`
```


## Empleo en el sector público y no público
```js
md`${introSectorPublico}`
```

<div class="card">
<div>${chartSectorPublico}</div>
</div><!--card-->

<div class="card">
<div>${chartSectorPublico_porcentaje}</div>
</div><!--card-->

<div class="card">
<div>${chartSectorPublico_diferencias}</div>
</div><!--card-->


```js
md`${narrativaSectorPublico}`
```


## Personas ocupadas según nacionalidad
```js
md`${introNacionalidad}`
```

<div class="card">
<div>${chartNacionalidad}</div>
</div><!--card-->
<div class="card">
<div>${chartNacionalidad_porcentaje}</div>
</div><!--card--><div class="card">
<div>${chartNacionalidad_diferencias}</div>
</div><!--card-->



```js
md`${narrativaNacionalidad}`
```


## Personas ocupadas según sexo
```js
md`${introSexo}`
```

<div class="card">
<div>${chartSexo}</div>
</div><!--card-->

<div class="card">
<div>${chartSexo_porcentaje}</div>
</div><!--card-->


<div class="card">
<div>${chartSexo_diferencias}</div>
</div><!--card-->



```js
md`${narrativaSexo}`
```

---

## Nota del autor

Esta página fue construida por **Ernesto Laval** ([`@elaval`](https://x.com/elaval)) con fines de divulgación pública.

El autor cuenta con experiencia en visualización y presentación de datos, pero **no es especialista en economía ni en empleo**. Aunque se ha puesto especial cuidado en el uso de fuentes oficiales y el procesamiento riguroso de los datos, es posible que el sitio contenga errores o interpretaciones mejorables. Si detectas alguna inconsistencia o tienes sugerencias para mejorar el contenido, puedes contactar al autor mediante mensaje directo en X ([@elaval](https://x.com/elaval)).

Este sitio es también un **experimento en el uso de inteligencia artificial (IA)** para generar contenidos de forma automatizada. Todas las narrativas e introducciones han sido generadas mediante modelos de lenguaje (GPT-4o de OpenAI), coordinados a través de agentes construidos con **LangGraph**. Estas herramientas permiten orquestar la ejecución de consultas de base de datos, el procesamiento de los datos y la generación de textos en lenguaje natural para cada sección.

El sitio fue desarrollado con el **Framework Observablehq**, utilizando **Plot** para la creación de gráficos. Los datos procesados se cargan dinámicamente mediante *data loaders* y se visualizan directamente en el navegador, facilitando la exploración y el análisis de las tendencias del empleo en Chile.

📄 Si te interesa conocer más sobre las fuentes de datos, las variables utilizadas y el procesamiento detrás del sitio, revisa la [página con información técnica](./info_tecnica).

<!-----
## Resumen de cambios en diemnsiones seleccionadas
-->
```js
//md`${narrativaPosts}`
```



```js
// Narrativas

const narrativaOcupados  = FileAttachment("graphs/generate_narrative_ocupados.md").text();
const narrativaInformalidad  = FileAttachment("graphs/generate_narrative_informalidad.md").text();
const narrativaTPI  = FileAttachment("graphs/generate_narrative_tpi.md").text();
const narrativaEdu  = FileAttachment("graphs/generate_narrative_edu.md").text();
const narrativaCalificacionOcupacion  = FileAttachment("graphs/generate_narrative_calificacion_ocupacion.md").text();
const narrativaSubempleoGeneral  = FileAttachment("graphs/generate_narrative_subempleo_general.md").text();
const narrativaSectorPublico  = FileAttachment("graphs/generate_narrative_sector_publico.md").text();
const narrativaNacionalidad  = FileAttachment("graphs/generate_narrative_nacionalidad.md").text();
const narrativaSexo  = FileAttachment("graphs/generate_narrative_sexo.md").text();

const narrativaPosts  = FileAttachment("graphs/generate_posts.md").text();
```

```js

// Texto introductorio
const introIntroduccionGeneral  = FileAttachment("graphs/generate_intro_introduccion_general.md").text();
const introOcupados  = FileAttachment("graphs/generate_intro_ocupados.md").text();
const introInformalidad  = FileAttachment("graphs/generate_intro_informalidad.md").text();
const introTPI  = FileAttachment("graphs/generate_intro_tpi.md").text();
const introEdu  = FileAttachment("graphs/generate_intro_edu.md").text();
const introCalificacionOcupacion = FileAttachment("graphs/generate_intro_calificacion_ocupacion.md").text();
const introSubempleoGeneral = FileAttachment("graphs/generate_intro_subempleo_general.md").text();

const introSectorPublico = FileAttachment("graphs/generate_intro_sector_publico.md").text();
const introNacionalidad = FileAttachment("graphs/generate_intro_nacionalidad.md").text();
const introSexo = FileAttachment("graphs/generate_intro_sexo.md").text();


```

```js
const sourceDataForCharts  = FileAttachment("graphs/generate_data.json").json();
```


```js
const chartOcupados = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ocupados)
  return buildChart({
    data:dataPlot,
    title: "Total de personas ocupadas",
    labelAliases: labelAliases
    })
})()

const chartOcupados_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.ocupados).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    //referenceVariable:"ocupados"
    })
})()


const chartInformalidad = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.informalidad)
  return buildChart({
    data:dataPlot,
    title: "Personas con ocupación formal e informal",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases

  })
})()

const chartInformalidad_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.informalidad)
  return buildChart({
    data:dataPlot.filter(d => d.variable == "informal"), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas con ocupación informal",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    labelY: "% del total de personas ocupadas",
    marginLeft:60,

    })

})()

const chartInformalidad_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.informalidad).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas con ocupación formal e informal - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()

const chartTPI = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.tpi)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas con Tiempo Parcial Involuntario (TPI)",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    referenceVariable:"ocupados"

    })
})()

const chartTPI_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.tpi)
  return buildChart({
    data:dataPlot.filter(d=> d.variable !== "no_tpi"), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas ocupadas a Tiempo Parcial Involuntario",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    labelY: "% del total de personas ocupadas",
    marginLeft:60,
    })

})()

const chartTPI_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.tpi).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas con TPI - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()

const chartEdu = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.edu)
  return buildChart({
    data:dataPlot.filter(d => d.variable !== 'ocupados'),
    title: "Personas ocupadas según nivel educacional",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginRight:160,
    referenceVariable:"ocupados"
    })
})()

const chartEdu_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.edu).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas según nivel educacional - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()

const chartEdu_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.edu)
  return buildChart({
    data:dataPlot, 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas ocupadas según nivel educacional",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    labelY: "% del total de personas ocupadas",
    marginLeft:60,
    })

})()

const chartCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.calificacion_ocupacion)
  return buildChart({
    data:dataPlot.filter(d => d.variable !== 'ocupados'),
    title: "Ocupación según nivel de calificación requerido para la ocupación",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginRight:200,
    referenceVariable:"ocupados"

    })
})()

const chartCalificacionOcupacion_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.calificacion_ocupacion)
  return buildChart({
    data:dataPlot, 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas según calificación de la ocupación",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    marginRight:200,
    labelY: "% del total de personas ocupadas",
    marginLeft:60,
    })

})()

const chartCalificacionOcupacion_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.calificacion_ocupacion).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Nivel de calificación de la ocupación – Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()


const chartSubempleoGeneral = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.subempleo_general).filter(d => d.variable !== "ocupados")
  return buildChart({
    data:dataPlot,
    title: "Personas subempleadas por competencia y/o insuficiencia horaria",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginRight:300
    })
})()

const cchartSubempleoGeneral_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.subempleo_general)
  return buildChart({
    data:dataPlot.filter(d => !d.variable.match(/subempleo_calificaciones/)), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas con subempleo y sin subempleo",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    marginLeft:60,
    marginRight:270,
    labelY: "% del total de personas ocupadas"
    })

})()


const chartSubempleoGeneral_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.subempleo_general).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Diferencia anual según situación de subempleo (2025 vs 2024)",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:300,
    referenceVariable:"ocupados"
    })
})()



const chartSectorPublico = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sector_publico)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas en el sector público",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    referenceVariable:"ocupados"
    })
})()

const chartSectorPublico_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.sector_publico)
  return buildChart({
    data:dataPlot.filter(d => d.variable !== "no_sector_publico"), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas en sector público",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    marginLeft:60,
    marginRight:150,
    labelY: "% del total de personas ocupadas"
    })

})()


const chartSectorPublico_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.sector_publico).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas en sector público - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    referenceVariable:"ocupados"
    })
})()

const chartNacionalidad = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.nacionalidad)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas según nacionalidad (Chilena / Extranjera)",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    referenceVariable:"ocupados"
    })
})()

const chartNacionalidad_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.nacionalidad)
  return buildChart({
    data:dataPlot.filter(d => !d.variable.match(/chilena/)), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de personas extranjeras ocupadas",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    marginLeft:60,
    marginRight:150,
    labelY: "% del total de personas ocupadas"
    })

})()

const chartNacionalidad_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.nacionalidad).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas según nacionalidad - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    referenceVariable:"ocupados"
    })
})()


const chartSexo = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sexo)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas según sexo",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    referenceVariable:"ocupados"
    })
})()

const chartSexo_porcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.sexo)
  return buildChart({
    data:dataPlot.filter(d => !d.variable.match(/hombre/)), 
    format:".2%", 
    formatAxis:".1%",
    title: "Porcentaje de mujeres ocupadas",
    subtitle: "Trimestre diciembre-enero-febrero",
    zero:"no",
    labelAliases: labelAliases,
    marginLeft:60,
    marginRight:150,
    labelY: "% del total de personas ocupadas"
    })

})()

const chartSexo_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.sexo).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas según sexo - Diferencia 2025 vs 2024",
    subtitle: "Trimestre diciembre-enero-febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    referenceVariable:"ocupados"
    })
})()

```


```js
const labelAliases = {
  "ocupados": "Personas Ocupadas",

  "formal": "Ocupación Formal",
  "informal": "Ocupación Informal",

  "tpi": "TPI",
  "no_tpi": "No TPI",

  "ed_sup": "Ed. Superior",
  "ed_media": "Ed. Media",
  "ed_basica": "Ed. Basica",
  "sin_ed_basica": "Sin Ed. Basica completa",

  "ed_sup_completa": "Ed. Superior Completa",
  "sin_ed_sup": "Sin Ed. Superior Completa",

  "calificacion_media_baja": "Ocup. de Calificación Media/Baja",
  "calificacion_baja": "Ocup. de Calificación Baja",
  "calificacion_media": "Ocup. de Calificación Media",
  "alta_calificacion": "Ocup. de Calificación Alta",

  "ed_sup_competencia_alta": "Ed Sup & Alta Calificación",
  "ed_sup_competencia_media_baja": "Ed Sup & Calificación Media/Baja",  
  "sin_ed_sup_competencia_alta": "Sin Ed Sup & Alta Calificación",
  "sin_ed_sup_competencia_media_baja": "Sin Ed Sup & Calificación Media/Baja",

  "subempleo_total":"Subempleo Total",
  "subempleo_calificaciones_excluyendo_subempleo_horas":"Subempleo Competencias (excl. Subempleo horas)",
  "subempleo_calificaciones_y_subempleo_horas":"Subempleo por competencias y horas",
  "subempleo_horas_excluyendo_subempleo_calificaciones":"Subempleo Horas (excl. Subempleo competencias)",
  "ed_sup_alta_calificacion_excluyendo_subempleo_horas":"Ed Sup y altas calificaciones (sin subempleo)",
  "sin_ed_sup_excluyendo_subempleo_horas": "Sin Educación Superior (sin subempleo)",

  "sector_publico": "Sector Público",
  "no_sector_publico": "No en Sector Público",

  "nacionalidad_chilena": "Nacionalidad Chilena",
  "nacionalidad_extranjera": "Nacionalidad Extranjera",

  "hombre": "Hombre",
  "mujer": "Mujer",

}
```


```js
const Markdown = new markdownit({html: true});

function md(strings) {
  let string = strings[0];
  for (let i = 1; i < arguments.length; ++i) {
    string += String(arguments[i]);
    string += strings[i];
  }
  const template = document.createElement("template");
  template.innerHTML = Markdown.render(string);
  return template.content.cloneNode(true);
}
```

```js
function convertDataToPlot(sourceData) {
  const variables = _.keys(sourceData.by_variable)
  return _.chain(sourceData.by_year)
  .map((d,year) => variables.map(variable => ({
    año: year,
    variable: variable,
    valor: d[variable]
  })))
  .flatten()
  .value()
}
```

```js
function convertDataToPlotPorcentajes(sourceData) {
  return _.chain(sourceData.pct_ocupados)
  .map((items,variable) => _.map(items,(valor, año) => ({
    año: año,
    variable: variable,
    valor: valor
  })))
  .flatten()
  .value()
}
```

```js
function convertDataToPlotDiferencia(sourceData) {
  return _.chain(sourceData.diff_prev_year)
  .map((items,variable) => _.map(items,(valor, año) => ({
    año: año,
    variable: variable,
    valor: valor
  })))
  .flatten()
  .value()
}
```

```js
const fuentes= "Bases de Datos de Ocupación y Desocupación, Instituto Nacional de Estadísticas (INE)"
```

```js
function buildChart(options) {
  const dataPlot = options.data;
  const title = options && options.title || "";
  const subtitle = options && options.subtitle || "";
  const zero = options && options.zero == "no" ? false : true
  const format = options && options.format || ".3s"
  const formatAxis = options && options.format || "s"
  const labelY = options && options.labelY || "Personas"
  const labelAliases =  options && options.labelAliases || {}
  const width =  options && options.width || 1000
  const height =  options && options.height || width*0.4
  const marginLeft =  options && options.marginLeft || 50
  const marginRight =  options && options.marginRight || 150
  const referenceKey = options.referenceVariable || null;
  const keys = _.chain(dataPlot).map((d) => d.variable).uniq().filter((d) => d !== referenceKey).value();
  const años = _.chain(dataPlot).map(d => d.año).uniq().value()
  const minAño = _.chain(dataPlot).map(d => d.año).min().value()
  const maxAño = _.chain(dataPlot).map(d => d.año).max().value()

  function label(label) {
    return labelAliases[label] || label
  }

  const colorDomain = (referenceKey ? _.concat(referenceKey, keys) : keys).map(d => label(d))

  return Plot.plot({
    title,
    subtitle,
    caption:`Fuente de datos: ${fuentes}\nElaborado por @elaval`,
    width,
    height,
    marginLeft: marginLeft,
    marginRight: marginRight,
    style:{fontSize:12},
    y: { 
      tickFormat: formatAxis,
      zero:zero,
      label: labelY
     },
    x: { domain: [minAño-1, maxAño], ticks: años.length , tickFormat:"d", grid:true,      
    label:"Año"
    },
    color: {
      legend: true,
      domain: colorDomain,
      range: referenceKey ? _.concat("lightgrey", d3.schemeObservable10) : d3.schemeObservable10,
    },

     marks: [
      //Plot.ruleY([0]),
      Plot.lineY(dataPlot, {
        x: "año",
        y: "valor",
        stroke: d => label(d.variable)
      }),
      Plot.dot(dataPlot, {
        x: "año",
        y: "valor",
        fill: d => label(d.variable)
      }),
      Plot.text(dataPlot, {
        x: "año",
        y: "valor",
        text: (d) => d3.format(format)(d["valor"]),
        dy: -10
      }),
      Plot.text(
        dataPlot,
        Plot.selectLast({
          x: "año",
          y: "valor",
          text: d => label(d.variable),
          textAnchor: "start",
          dx: 10,
          z: d => label(d.variable)
        })
      )
 
    ]
 
    
  })
}
```

```js

function buildChartDiferencia(options) {
  const dataPlot = options.data;
  const title = options && options.title || "";
  const subtitle = options && options.subtitle || "";
  const zero = options && options.zero == "no" ? false : true
  const format = options && options.format || ".3s"
  const formatAxis = options && options.format || "s"
  const labelY = options && options.labelY || "Personas"
  const labelAliases =  options && options.labelAliases || {}
  const width =  options && options.width || 1000
  const height =  options && options.height || width*0.3
  const marginLeft =  options && options.marginLeft || 150
  const marginRight =  options && options.marginRight || 20
  const referenceKey = options.referenceVariable || null;
  const keys = _.chain(dataPlot).map((d) => d.variable).uniq().filter((d) => d !== referenceKey).value();
  const años = _.chain(dataPlot).map(d => d.año).uniq().value()
  const minAño = _.chain(dataPlot).map(d => d.año).min().value()
  const maxAño = _.chain(dataPlot).map(d => d.año).max().value()

  const maxValue = _.chain(dataPlot).map(d => d.valor).max().value()
  const minValue = _.chain(dataPlot).map(d => d.valor).min().value()

  const valueRange = minValue < 0 && maxValue > 0 ? maxValue - minValue : _.max(Math.abs(maxValue), Math.abs(minValue))


  function smallBar(value) {
    const plotWidth = width - marginLeft - marginRight;
    const barSize = plotWidth * Math.abs(value) / valueRange;
    return barSize < 40;
  }
  

  function label(label) {
    return labelAliases[label] || label
  }

  const colorDomain = (referenceKey ? _.concat(referenceKey, keys) : keys).map(d => label(d))  //return dataPlot

  //return colorDomain
  return Plot.plot({
    title,
    subtitle,
    caption:`Fuente de datos: ${fuentes}\nElaborado por @elaval`,
    width,
    height,
    marginLeft: marginLeft,
    marginRight: marginRight,
    marginBottom: 40,
    style:{fontSize:12},
    x: { 
      tickFormat: formatAxis,
      label: "Variación 2025 vs 2024 (en número de personas)"
     },
    
    y: {domain:colorDomain},
    marks: [
   
      Plot.barX(dataPlot, {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => d["variable"] == referenceKey ? "lightgrey" : d3.schemeObservable10[0]
      }),     
      
      Plot.text(dataPlot.filter(d => !smallBar(d.valor) && d.valor > 0), {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => d["variable"] == referenceKey ? "black" : smallBar(d.valor) ? "black" : "white", 
        text: d =>  `+${d3.format(".3s")(d.valor)}` ,
        textAnchor: "end",
        dx:-5
      }),
      
      Plot.text(dataPlot.filter(d => !smallBar(d.valor) && d.valor < 0), {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => d["variable"] == referenceKey ? "black" : smallBar(d.valor) ? "black" : "white", 
        text: d =>  d3.format(".3s")(d.valor) ,
        textAnchor: "start",
        dx:5
      }),

      Plot.text(dataPlot.filter(d => smallBar(d.valor)), {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => "black",
        text: d =>  d.valor > 0 ? `+${d3.format(".3s")(d.valor)}` : `${d3.format(".3s")(d.valor)}` ,
        textAnchor: "start",
        dx:5
      })
    ]
  })
}
```


```js
//display(sourceDataForCharts)
```






```js
// Import required modules and configurations
import moment from 'npm:moment'
import markdownit from "npm:markdown-it";

```