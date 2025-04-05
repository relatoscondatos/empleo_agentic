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
<div>${chartInformalidadPorcentaje}</div>
</div><!--card-->

<div class="card">
<div>${chartInformalidad_diferencias}</div>
</div><!--card-->



```js
md`${narrativaInformalidad}`
```


## Subempleo por horario (TPI)

```js
md`${introTPI}`
```

<div class="card">
<div>${chartTPI}</div>
</div><!--card-->

<div class="card">
<div>${chartTPIPorcentaje}</div>
</div><!--card-->

<div class="card">
<div>${chartTPI_diferencias}</div>
</div><!--card-->



```js
md`${narrativaTPI}`
```


## Nivel educacional de las personas ocupadas
```js
md`${introEdSup}`
```
<div class="card">
<div>${chartEdSup}</div>
</div><!--card-->
<div class="card">
<div>${chartEdSup_diferencias}</div>
</div><!--card-->


```js
md`${narrativaEdSup}`
```


## Calificación de las ocupaciones
```js
md`${introCalificacionOcupacion}`
```
<div class="card">
<div>${chartCalificacionOcupacion}</div>
</div><!--card-->
<div class="card">
<div>${chartCalificacionOcupacion_diferencias}</div>
</div><!--card-->


```js
md`${narrativaCalificacionOcupacion}`
```


## Educación superior y calificación de la ocupación
```js
md`${introEdSupCalificacionOcupacion}`
```

<div class="card">
<div>${chartEduCalificacionOcupacion}</div>
</div><!--card-->
<div class="card">
<div>${chartEduCalificacionOcupacion_diferencias}</div>
</div><!--card-->

```js
md`${narrativaEdSupCalificacionOcupacion}`
```


## Empleo en el sector público y no público
```js
md`${introSectorPublico}`
```

<div class="card">
<div>${chartSectorPublico}</div>
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
<div>${chartSexo_diferencias}</div>
</div><!--card-->



```js
md`${narrativaSexo}`
```

```js
// Narrativas

const narrativaOcupados  = FileAttachment("graphs/generate_narrative_ocupados.md").text();
const narrativaInformalidad  = FileAttachment("graphs/generate_narrative_informalidad.md").text();
const narrativaTPI  = FileAttachment("graphs/generate_narrative_tpi.md").text();
const narrativaEdSup  = FileAttachment("graphs/generate_narrative_ed_sup.md").text();
const narrativaCalificacionOcupacion  = FileAttachment("graphs/generate_narrative_calificacion_ocupacion.md").text();
const narrativaEdSupCalificacionOcupacion  = FileAttachment("graphs/generate_narrative_ed_sup_calificacion_ocupacion.md").text();
const narrativaSectorPublico  = FileAttachment("graphs/generate_narrative_sector_publico.md").text();
const narrativaNacionalidad  = FileAttachment("graphs/generate_narrative_nacionalidad.md").text();
const narrativaSexo  = FileAttachment("graphs/generate_narrative_sexo.md").text();


```

```js

// Texto introductorio
const introIntroduccionGeneral  = FileAttachment("graphs/generate_intro_introduccion_general.md").text();
const introOcupados  = FileAttachment("graphs/generate_intro_ocupados.md").text();
const introInformalidad  = FileAttachment("graphs/generate_intro_informalidad.md").text();
const introTPI  = FileAttachment("graphs/generate_intro_tpi.md").text();
const introEdSup  = FileAttachment("graphs/generate_intro_ed_sup.md").text();
const introCalificacionOcupacion = FileAttachment("graphs/generate_intro_calificacion_ocupacion.md").text();
const introEdSupCalificacionOcupacion = FileAttachment("graphs/generate_intro_ed_sup_calificacion_ocupacion.md").text();
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
    subtitle: "Trimestre Diciembre Enero Febrero",
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
    title: "Personas con ocupacion formal / informal",
    labelAliases: labelAliases

  })
})()

const chartInformalidad_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.informalidad).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Ocupación formal / informal - Diferencia 2025 vs 2024",
    subtitle: "Trimestre Diciembre Enero Febrero",
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
    subtitle: "Subempleo por horario",
    labelAliases: labelAliases

    })
})()

const chartTPI_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.tpi).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas con TPI - Diferencia 2025 vs 2024",
    subtitle: "Trimestre Diciembre Enero Febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()

const chartEdSup = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ed_sup)
  return buildChart({
    data:dataPlot,
    title: "Personas con Educación Superior Completa",
    labelAliases: labelAliases,
    marginRight:160
    })
})()

const chartEdSup_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.ed_sup).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Educación Superior - Diferencia 2025 vs 2024",
    subtitle: "Trimestre Diciembre Enero Febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()

const chartCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.calificacion_ocupacion)
  return buildChart({
    data:dataPlot,
    title: "Ocupados según nivel de calificación requerido para la ocupación",
    labelAliases: labelAliases,
    marginRight:200

    })
})()

const chartCalificacionOcupacion_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.calificacion_ocupacion).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Tipo calificación de la ocupación - Diferencia 2025 vs 2024",
    subtitle: "Trimestre Diciembre Enero Febrero",
    labelAliases: labelAliases,
    marginLeft:200,
    height: 150,
    referenceVariable:"ocupados"
    })
})()


const chartEdSupCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ed_sup_calificacion_ocupacion)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas según nivel educacional y calificación de la ocupación",
    subtitle: "Cuando la calificación es media o baja hablamos de subempleo por competencias",
    labelAliases: labelAliases,
        marginRight:200

    })
})()


const chartEduCalificacionOcupacion_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.edu_calificacion_ocupacion).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Cambio anual en la ocupación según nivel educativo y calificación (2025 vs. 2024)",
    labelAliases: labelAliases,
    marginLeft:200,
    referenceVariable:"ocupados"
    })
})()



const chartEduCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.edu_calificacion_ocupacion).filter(d => d.variable !== "ocupados")
  return buildChart({
    data:dataPlot,
    title: "Educación superior y calificación de la ocupación",
    title: "Personas ocupadas según nivel educacional y nivel de calificación de la ocupación",
    subtitle: "Personas con Educación Superior y ocupaciones con calificación media o baja se pueden considerar subempleo por competencias",
    labelAliases: labelAliases,
    marginRight:200
    })
})()



const chartSectorPublico = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sector_publico)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas en el sector público",
    labelAliases: labelAliases
    })
})()

const chartSectorPublico_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.sector_publico).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas en sector público - Diferencia 2025 vs 2024",
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
    labelAliases: labelAliases
    })
})()

const chartNacionalidad_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.nacionalidad).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas según nacionalidad - Diferencia 2025 vs 2024",
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
    labelAliases: labelAliases
    })
})()

const chartSexo_diferencias = (() => {
  const dataPlot = convertDataToPlotDiferencia(sourceDataForCharts.data.sexo).filter(d => d.año == 2025)
  return buildChartDiferencia({
    data:dataPlot,
    title: "Personas ocupadas según sexo - Diferencia 2025 vs 2024",
    labelAliases: labelAliases,
    marginLeft:200,
    referenceVariable:"ocupados"
    })
})()


const chartTPIPorcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.tpi)
  return buildChart({
    data:dataPlot, 
    format:".2%", 
    formatAxis:".1%",
    title: "Personas ocupadas a Tiempo Parcial Involuntario (% de ocupación total)",
    zero:"no",
    labelAliases: labelAliases,
    labelY: "% del total de personas ocupadas"
    })

})()

const chartInformalidadPorcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.informalidad)
  return buildChart({
    data:dataPlot.filter(d => d.variable == "informal"), 
    format:".2%", 
    formatAxis:".1%",
    title: "Personas con empleo informal (% de ocupación total)",
    zero:"no",
    labelAliases: labelAliases,
    labelY: "% del total de personas ocupadas"
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
  "ed_sup_completa": "Ed. Superior Completa",
  "sin_ed_sup": "Sin Ed. Superior Completa",
  "calificacion_media_baja": "Ocup. de Calificación Media/Baja",
  "alta_calificacion": "Ocup. de Alta Calificación",
  "ed_sup_competencia_alta": "Ed Sup & Alta Calificación",
  "ed_sup_competencia_media_baja": "Ed Sup & Calificación Media/Baja",
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
    marginLeft: 50,
    marginRight: marginRight,
    style:{fontSize:12},
    y: { 
      tickFormat: formatAxis,
      zero:zero,
      label: labelY
     },
    x: { domain: [minAño-1, maxAño], ticks: años.length , tickFormat:"d", grid:true},
    color: {
      legend: true,
      domain: colorDomain,
      range: referenceKey ? _.concat("lightgrey", d3.schemeObservable10) : d3.schemeObservable10,
      label:"Año"
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
  const referenceKey = options.referenceVariable || null;
  const keys = _.chain(dataPlot).map((d) => d.variable).uniq().filter((d) => d !== referenceKey).value();
  const años = _.chain(dataPlot).map(d => d.año).uniq().value()
  const minAño = _.chain(dataPlot).map(d => d.año).min().value()
  const maxAño = _.chain(dataPlot).map(d => d.año).max().value()

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
    marginRight: 20,
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
      
      Plot.text(dataPlot, {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => d["variable"] == referenceKey ? "black" : "white",
        text: d => d.valor > 0 ? `+${d3.format(".3s")(d.valor)}` : "",
        textAnchor: "end",
        dx:-5
      }),
      
      Plot.text(dataPlot, {
        x: "valor",
        y: d => label(d["variable"]),
        fill: d => d["variable"] == referenceKey ? "black" : "white",
        text: d => d.valor < 0 ? d3.format(".3s")(d.valor) : "",
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