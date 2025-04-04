---

---

# Evolución del empleo en Chile 
## Cifras de trimestre Diciembre-Enero-Febrero en años recientes
```js
md`${introGeneral}`
```

## Total de personas ocupadas
```js
md`${introOcupacion}`
```

<div class="card">
<div>${chartOcupados}</div>
</div><!--card-->


```js
md`${narrativaOcupados}`
```

## Informalidad
```js
md`${introInformalidad}`
```
<div class="card">
<div>${chartInformalidad}</div>
</div><!--card-->

<div class="card">
<div>${chartInformalidadPorcentaje}</div>
</div><!--card-->



```js
md`${narrativaInformalidad}`
```


## Subempleo por horario (Tiempo Parcial Involuntario)
```js
md`${introTPI}`
```

<div class="card">
<div>${chartTPI}</div>
</div><!--card-->

<div class="card">
<div>${chartTPIPorcentaje}</div>
</div><!--card-->



```js
md`${narrativaTPI}`
```


## Ocupados según nivel educacional (Educación Superior vs Sin Educación Superior)
```js
md`${introEdSup}`
```
<div class="card">
<div>${chartEdSup}</div>
</div><!--card-->

```js
md`${narrativaEdSup}`
```


## Ocupados según nivel de calificación asociado a la ocupación
```js
md`${introCalificacionOcupacion}`
```
<div class="card">
<div>${chartCalificacionOcupacion}</div>
</div><!--card-->


```js
md`${narrativaCalificacionOcupacion}`
```


## Tipo de empleo de personas con Educación Superior
```js
md`${introEdSupCalificacionOcupacion}`
```

<div class="card">
<div>${chartEdSupCalificacionOcupacion}</div>
</div><!--card-->

```js
md`${narrativaEdSupCalificacionOcupacion}`
```


## Ocupaciones del sector público
```js
md`${introSectorPublico}`
```

<div class="card">
<div>${chartSectorPublico}</div>
</div><!--card-->

```js
md`${narrativaSectorPublico}`
```



## Personas extranjeras
```js
md`${introNacionalidad}`
```

<div class="card">
<div>${chartNacionalidad}</div>
</div><!--card-->

```js
md`${narrativaNacionalidad}`
```


## Ocupaciones por sexo
```js
md`${introSexo}`
```

<div class="card">
<div>${chartSexo}</div>
</div><!--card-->

```js
md`${narrativaSexo}`
```

















```js
// Narrativas
/*
const narrativaOcupados  = FileAttachment("graphs/generate_narrative_ocupados.md").text();
const narrativaInformalidad  = FileAttachment("graphs/generate_narrative_informalidad.md").text();
const narrativaTPI  = FileAttachment("graphs/generate_narrative_tpi.md").text();
const narrativaEdSup  = FileAttachment("graphs/generate_narrative_ed_sup.md").text();
const narrativaCalificacionOcupacion  = FileAttachment("graphs/generate_narrative_calificacion_ocupacion.md").text();
const narrativaEdSupCalificacionOcupacion  = FileAttachment("graphs/generate_narrative_ed_sup_calificacion_ocupacion.md").text();
const narrativaSectorPublico  = FileAttachment("graphs/generate_narrative_sector_publico.md").text();
const narrativaNacionalidad  = FileAttachment("graphs/generate_narrative_nacionalidad.md").text();
const narrativaSexo  = FileAttachment("graphs/generate_narrative_sexo.md").text();

*/
```

```js
/*
// Texto introductorio
const introGeneral  = FileAttachment("graphs/generate_intro_general.md").text();
const introOcupacion  = FileAttachment("graphs/generate_intro_ocupacion.md").text();
const introInformalidad  = FileAttachment("graphs/generate_intro_informalidad.md").text();
const introTPI  = FileAttachment("graphs/generate_intro_tpi.md").text();
const introEdSup  = FileAttachment("graphs/generate_intro_ed_sup.md").text();
const introCalificacionOcupacion = FileAttachment("graphs/generate_intro_calificacion_ocupacion.md").text();
const introEdSupCalificacionOcupacion = FileAttachment("graphs/generate_intro_ed_sup_calificacion_ocupacion.md").text();
const introSectorPublico = FileAttachment("graphs/generate_intro_sector_publico.md").text();
const introNacionalidad = FileAttachment("graphs/generate_intro_nacionalidad.md").text();
const introSexo = FileAttachment("graphs/generate_intro_sexo.md").text();

*/
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

const chartInformalidad = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.informalidad)
  return buildChart({
    data:dataPlot,
    title: "Personas con ocupacion formal / informal",
    labelAliases: labelAliases

  })
})()

const chartTPI = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.tpi)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas con Tiempo Parcial Invonultario (TPI)",
    subtitle: "Subempleo por horario",
    labelAliases: labelAliases

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

const chartCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.calificacion_ocupacion)
  return buildChart({
    data:dataPlot,
    title: "Ocupados según nivel de calificación requerido para la ocupación",
    labelAliases: labelAliases,
    marginRight:200

    })
})()


const chartEdSupCalificacionOcupacion = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ed_sup_calificacion_ocupacion)
  return buildChart({
    data:dataPlot,
    title: "Ocupados con Educación Superior según nivel de calificación de la ocupación",
    subtitle: "Cuando la calificación es media o baja hablamos de subempleo por competencias",
    labelAliases: labelAliases,
        marginRight:200

    })
})()


const chartSectorPublico = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sector_publico)
  return buildChart({
    data:dataPlot,
    title: "Ocupados con en el sector público",
    labelAliases: labelAliases
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


const chartSexo = (() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sexo)
  return buildChart({
    data:dataPlot,
    title: "Personas ocupadas según sexo",
    labelAliases: labelAliases
    })
})()

const chartTPIPorcentaje = (() => {
  const dataPlot = convertDataToPlotPorcentajes(sourceDataForCharts.data.tpi)
  return buildChart({
    data:dataPlot, 
    format:".2%", 
    formatAxis:".1%",
    title: "Personas ocupadas a Tiempo Parcial Involuntario (% de opacion total)",
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
    title: "Personas con empleo informal (% de opacion total)",
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
function buildChartDiferencia(options) {
  const dataPlot = options.data;
  const format = options && options.format || ".3s"
  const formatAxis = options && options.format || "s"

  const referenceKey = options.referenceVariable || null;
  const keys = dataPlot.map((d) => d.variable).filter((d) => d !== referenceKey);
  const minValue = _.chain(dataPlot).map(d => d.diferencia).min().value()
  const maxValue = _.chain(dataPlot).map(d => d.diferencia).max().value()


  return Plot.plot({
    width,
    marginLeft: 50,
    marginRight: 150,
    y: { tickFormat: formatAxis, domain: [minValue * 1.1, maxValue] },


     marks: [
   
      Plot.barY(dataPlot, {
        x: "año",
        y: "diferencia",
        fill: "variable"
      }),

      Plot.text(dataPlot, {
        x: "año",
        y: "diferencia",
        text: d => d["diferencia"] > 0 ? d3.format(format)(d["diferencia"]): null,
        fill:"black",
        stroke:"white",
        dy: -10
      }),      
      Plot.text(dataPlot, {
        x: "año",
        y: "diferencia",
        text: d => d["diferencia"] < 0 ? d3.format(format)(d["diferencia"]): null,
        fill:"black",
        stroke:"white",
        dy: 10
      }),
 
    ]
 
    
  })
}
```
```js
const fuentes= "Bases de Datos de Ocupación y Desocupación, Inistituto Nacional de Estadísticas (INE)"
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
    title:title,
    subtitle:subtitle,
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
//display(sourceDataForCharts)
```






```js
// Import required modules and configurations
import moment from 'npm:moment'
import markdownit from "npm:markdown-it";

```