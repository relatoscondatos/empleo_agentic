---
sql:
  ene_resumen: data/parquet/ene-01-def-agregado.parquet
---
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
const sourceDataForCharts  = FileAttachment("graphs/generate_data.json").json();
```

```js
display(sourceDataForCharts)
```

## Total de personas ocupadas v20240402.1458
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ocupados)

  //return [...data_formalidad]
  //return dataPlot
  return buildChart({data:dataPlot})
})()
```
```js
md`${narrativaOcupados}`
```

## Informalidad
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.informalidad)

  //return [...data_formalidad]
  //return dataPlot
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaInformalidad}`
```


## Subempleo por horario (Tiempo Parcial Involuntario)
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.tpi)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaTPI}`
```


## Ocupados según nivel educacional (Educación Superior vs Sin Educación Superior)
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ed_sup)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaEdSup}`
```


## Ocupados según nivel de calificación asociado a la ocupación
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.calificacion_ocupacion)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaCalificacionOcupacion}`
```


## Tipo de empleo de personas con Educación Superior
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.ed_sup_calificacion_ocupacion)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaEdSupCalificacionOcupacion}`
```


## Ocupaciones del sector público
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sector_publico)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaSectorPublico}`
```



## Personas extranjeras
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.nacionalidad)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaNacionalidad}`
```


## Ocupaciones por sexo
```js
(() => {
  const dataPlot = convertDataToPlot(sourceDataForCharts.data.sexo)
  return buildChart({data:dataPlot})
})()
```

```js
md`${narrativaSexo}`
```

























```sql display
SELECT *
FROM ene_resumen
```





```sql id=data_sector_publico 
SELECT 
  año,
  variable,
  valor,
  valor - LAG(valor) OVER (PARTITION BY variable ORDER BY año) AS diferencia
FROM ene_resumen
WHERE variable = 'sector_publico' OR variable = 'no_sector_publico'
ORDER BY variable, año

```

```sql id=data_nacionalidad 
SELECT 
  año,
  variable,
  valor,
  valor - LAG(valor) OVER (PARTITION BY variable ORDER BY año) AS diferencia
FROM ene_resumen
WHERE variable = 'nacionalidad_chilena' OR variable = 'nacionalidad_extranjera'
ORDER BY variable, año

```

```sql id=data_sexo 
SELECT 
  año,
  variable,
  valor,
  valor - LAG(valor) OVER (PARTITION BY variable ORDER BY año) AS diferencia
FROM ene_resumen
WHERE variable = 'hombre' OR variable = 'mujer'
ORDER BY variable, año

```





```js
(() => {
  const dataPlot = [...data_ed_sup_calificacion_ocupación]

  return buildChart({data:dataPlot})
})()
```
```js
(() => {
  const dataPlot = [...data_calificacion_ocupación]

  return buildChart({data:dataPlot})
})()
```

```js
(() => {
  const dataPlot = [...data_sector_publico]

  return buildChart({data:dataPlot})
})()
```


```js
(() => {
  const dataPlot = [...data_nacionalidad]

  return buildChart({data:dataPlot})
})()
```

```js
(() => {
  const dataPlot = [...data_nacionalidad].filter(d => d.año >= 2012 && (d.variable == "nacionalidad_extranjera"))

  return buildChartDiferencia({data:dataPlot})
})()
```


```js
(() => {
  const dataPlot = [...data_sexo]

  return buildChart({data:dataPlot})
})()
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
function buildChart(options) {
  const dataPlot = options.data;
  const format = options && options.format || ".3s"
  const formatAxis = options && options.format || "s"

  const referenceKey = options.referenceVariable || null;
  const keys = dataPlot.map((d) => d.variable).filter((d) => d !== referenceKey);
  const minAño = _.chain(dataPlot).map(d => d.año).min().value()
  const maxAño = _.chain(dataPlot).map(d => d.año).max().value()

  return Plot.plot({
    width,
    marginLeft: 50,
    marginRight: 150,
    y: { tickFormat: formatAxis },
    x: { domain: [minAño-1, maxAño] },
    color: {
      legend: true,
      domain: referenceKey ? _.concat(referenceKey, keys) : keys,
      range: referenceKey ? _.concat("lightgrey", d3.schemeObservable10) : d3.schemeObservable10
    },

     marks: [
      Plot.ruleY([0]),
      Plot.lineY(dataPlot, {
        x: "año",
        y: "valor",
        stroke: "variable"
      }),
      Plot.dot(dataPlot, {
        x: "año",
        y: "valor",
        fill: "variable"
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
          text: "variable",
          textAnchor: "start",
          dx: 10,
          z: "variable"
        })
      )
 
    ]
 
    
  })
}
```



```js
// Import required modules and configurations
import moment from 'npm:moment'
import markdownit from "npm:markdown-it";



```