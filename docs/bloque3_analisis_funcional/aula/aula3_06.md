# Actividad práctica · Tema 8: integración y enriquecimiento funcional

**Asignatura:** Bioinformática · 2.º del Grado en Biotecnología  
**Modalidad:** trabajo en parejas  
**Duración:** 60 minutos presenciales + comparación posterior entre parejas  
**Caso biológico general:** respuesta de *Saccharomyces cerevisiae* a variaciones de glucosa, temperatura y pH.

## 1. Contexto y propósito

En los bloques anteriores de la asignatura hemos trabajado con bases de datos biológicas, secuencias y relaciones evolutivas. En esta actividad damos el paso hacia la **interpretación funcional de datos experimentales**: partiendo de una lista de genes de interés de un experimento real, combinaremos información de diferentes recursos para investigar qué procesos biológicos aparecen sobrerrepresentados, cómo interpretar los resultados y qué conclusiones están justificadas.

Cada pareja recibe **una única condición experimental** y trabaja únicamente sobre ella. Todas las parejas realizan el mismo procedimiento, pero con conjuntos de entrada distintos. **Desde el comienzo se conoce que habrá una fase posterior de comparación** con otra pareja que haya estudiado un factor ambiental diferente.

La finalidad no es obtener necesariamente resultados significativos ni confirmar una hipótesis: también son científicamente válidos los análisis sin términos enriquecidos, siempre que se documente el procedimiento y las limitaciones.

## 2. Pregunta científica

Cada pareja trabaja con una pregunta particular según el factor y la condición asignados:

| Factor | Pregunta marco | Estudio GEO |
|---|---|---|
| Glucosa | ¿Qué procesos funcionales se relacionan con la respuesta de la levadura a un pulso de glucosa durante el cultivo con galactosa? | [GSE4158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE4158) |
| Temperatura | ¿Qué procesos funcionales se relacionan con la respuesta al cambio de 25 a 37 °C? | [GSE24484](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE24484) |
| pH | ¿Qué procesos funcionales se relacionan con la respuesta al cambio de pH 5,5 a 8,0? | [GSE58051](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58051) |

Las condiciones específicas propuestas son:

| Código | Factor | Comparación o condición | Origen |
|---|---|---|---|
| G1 | Glucosa | Pulso de 2 g/L, 20 min, respecto al tiempo 0 | GSE4158 |
| G2 | Glucosa | Pulso de 2 g/L, 45 min, respecto al tiempo 0 | GSE4158 |
| G3 | Glucosa | Pulso de 0,2 g/L, 45 min, respecto al tiempo 0 | GSE4158 |
| T1 | Temperatura | 37 °C, 4 min, respecto a 25 °C inicial | GSE24484 |
| T2 | Temperatura | 37 °C, 11 min, respecto a 25 °C inicial | GSE24484 |
| T3 | Temperatura | 37 °C, 26 min, respecto a 25 °C inicial | GSE24484 |
| P1 | pH | pH 8,0, 6 min, respecto a pH 5,5 inicial | GSE58051 |
| P2 | pH | pH 8,0, 20 min, respecto a pH 5,5 inicial | GSE58051 |
| P3 | pH | pH 8,0, 40 min, respecto a pH 5,5 inicial | GSE58051 |

> **Datos preparados:** las nueve listas se han derivado de matrices GEO reales y sus plataformas de anotación. Los genes se han seleccionado mediante un umbral exploratorio de cambio de expresión, no mediante pruebas de expresión diferencial. Deben consultar la ficha del conjunto asignado.

## 3. Material entregado a cada pareja

- `genes_<codigo>.csv`: una fila por gen de interés; identificador estable de *S. cerevisiae*, nombre, dirección del cambio cuando pueda justificarse, valor descriptivo/estadístico disponible y referencia a la muestra.
- `background_<codigo>.csv`: conjunto de genes que podían entrar en la selección, identificado con el **mismo sistema de IDs** que el archivo anterior.
- `ficha_<codigo>.md`: descripción de la condición, muestras, comparación, procedencia, criterio de selección de genes, filtrados, fecha y versión de anotaciones.
- Este enunciado que es común para todos.

**Descarga:** sección **9. Archivos de datos** al final del enunciado, basta descargar únicamente el ZIP del código asignado. Los ficheros `.txt` contienen solo identificadores y pueden copiarse en herramientas de enriquecimiento que admitan listas de IDs. Deben comprobar que la herramienta permite establecer un background personalizado; si no lo permite, no deben sustituir el universo de referencia.

**Comprobación previa:** el conjunto de genes de interés debe estar incluido en el background, sin duplicados y con un identificador reconocible por la herramienta de enriquecimiento. Si no ocurre, debe comunicarse, no deben corregirlo.

## 4. Actividades

### Actividad 1. Comprender la comparación y formular una hipótesis (8 min)

Deben leer la ficha de condición y responder brevemente: ¿qué se ha modificado en el cultivo?, ¿respecto a qué condición se interpreta el resultado?, ¿qué representan los genes seleccionados? Deben formular una **pregunta específica** y una **hipótesis provisional y contrastable**. No deben asumir que será confirmada.

**Entregable:** 1 pregunta científica, 1 hipótesis y una descripción de la comparación en 2–3 frases.

### Actividad 2. Integrar información funcional (12 min)

Deben elegir **tres genes** de la lista (si la ficha no propone otros, seleccionadlos justificando el criterio). Consultad sus registros y relacionen información de [UniProt](https://www.uniprot.org/), [Gene Ontology](https://geneontology.org/), [InterPro](https://www.ebi.ac.uk/interpro/) y, cuando existan rutas pertinentes, [Reactome](https://reactome.org/).

Elaboren una tabla con identificador, nombre del producto, función conocida o propuesta, un término GO con su identificador y categoría (MF/BP/CC), fuente y **evidencia** de al menos una anotación. No es obligatorio encontrar información en todos los recursos: documenten los campos ausentes y no inventen asociaciones.

**Entregable:** tabla integrada de 3 genes y un párrafo sobre el valor de conectar recursos mediante identificadores.

### Actividad 3. Analizar el enriquecimiento funcional con Gene Ontology/PANTHER (15 min)

Todas las parejas utilizarán **la misma plataforma web**, sin programar ni instalar herramientas: [Gene Ontology](https://geneontology.org/), cuyo análisis se abre en **PANTHER**. Sigan la **[guía paso a paso específica de esta actividad](./guia_GO_PANTHER_paso_a_paso.md)**. La [guía oficial de Gene Ontology](https://geneontology.org/docs/go-enrichment-analysis/) sirve como referencia adicional, pero no sustituye las instrucciones de nuestra práctica.

**Configuración obligatoria:** organismo *Saccharomyces cerevisiae*; anotaciones **GO Biological Process (complete)**; lista `genes_<código>.txt`; **background personalizado** `background_<código>.txt` mediante **Reference list → Change**; **PANTHER Overrepresentation Test**, prueba exacta de **Fisher** y corrección **FDR**; criterio de interpretación **FDR < 0,05**. La primera ejecución con la referencia genómica por defecto **no es el resultado final**.

**Entregable:** archivo de resultados y una tabla con hasta cinco términos GO:BP (ID, nombre, FDR, genes asociados y, si está disponible, fold enrichment). Si ningún término alcanza FDR < 0,05, indicadlo expresamente. Deben registrar los genes no reconocidos y la fecha y versión de la herramienta.

### Actividad 4. Interpretar los resultados (10 min)

Deben explicar qué procesos aparecen sobrerrepresentados y cuáles superan el criterio de significación. Identificar posibles términos jerárquicamente relacionados o redundantes; comprobar los genes que sustentan las principales categorías. Separar **sobrerrepresentación descriptiva**, **evidencia estadística** e **interpretación biológica**.

**Entregable:** interpretación de 100–150 palabras, o una explicación razonada de por qué no puede afirmarse enriquecimiento significativo.

### Actividad 5. Contrastar la hipótesis y auditar la conclusión (15 min)

Deben volver a la hipótesis inicial. Indicar si los resultados la **respaldan**, la **contradicen** o son **insuficientes** para evaluarla. Formular una conclusión prudente basada en evidencias y revisar: procedencia de los datos, criterios de selección, IDs y duplicados, background, corrección por comparaciones múltiples, anotaciones y su evidencia, redundancia, límites del estudio y posibles sesgos. Eviten afirmar que un proceso «se activa» o que es «causado» por un factor únicamente a partir del enriquecimiento.

**Entregable:** conclusión de 3–5 frases y una auditoría de 4–6 puntos documentados.

## 5. Segunda fase: comparación entre parejas (trabajo posterior)

Deben intercambiar el informe que han generado con una pareja que haya trabajado **otro factor ambiental**. Cada pareja redactará una comparación breve que responda:

1. ¿Qué términos o procesos aparecen en ambos resultados y cuáles son específicos de cada análisis?
2. ¿Qué genes sustentan esos procesos y existe coincidencia real o solo coincidencia de etiquetas GO?
3. ¿Qué límites dificultan la comparación directa (estudio, cepa, plataforma, tiempos, controles, umbrales, número de genes y background)?

**Entregable adicional:** 150–200 palabras. La comparación es **cualitativa y crítica**, no un metaanálisis estadístico. La ausencia de una categoría entre los resultados significativos no demuestra su ausencia biológica.

## 6. Producto final y criterios de evaluación

Deben entregar un informe breve (aprox. 2–3 páginas, sin contar tablas extensas) con pregunta e hipótesis, tabla integrada, análisis de enriquecimiento, interpretación, conclusión y auditoría. Adjuntar el archivo/captura de resultados. La comparación con otra pareja se incorpora como anexo posterior.

Se valorará especialmente la **trazabilidad** de la información, la corrección del background, la interpretación del FDR, la prudencia de las afirmaciones y la coherencia entre hipótesis, evidencias y conclusiones. **No se otorgará más valor por obtener un mayor número de términos significativos.**

### Procedencia y preparación de los conjuntos

Se han procesado los archivos de expresión y anotación GEO originales, con correspondencia de sondas a identificadores sistemáticos de levadura. Cada pareja recibe la lista de interés y el universo de referencia del mismo código, además de una ficha metodológica.

Las listas se han generado mediante un criterio **exploratorio** de cambio absoluto log₂ ≥ 1, no mediante pruebas de expresión diferencial. Para glucosa se utiliza el log₂ ratio procesado; para temperatura la razón de medias de intensidad entre tiempos con filtros de calidad, y para pH las columnas RA normalizadas agregadas. **No deben confundirse genes seleccionados por cambio descriptivo con genes diferencialmente expresados con FDR significativo.**

Estas diferencias obligan a interpretar con prudencia los resultados, especialmente al comparar factores ambientales.

### Fuentes

- [GSE4158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE4158) y [GPL3415](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL3415)
- [GSE24484](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE24484) y [GPL4566](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL4566)
- [GSE58051](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE58051) y [GPL13620](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL13620)


## 8. Guía de enriquecimiento GO:BP con PANTHER

Para evitar configuraciones distintas entre parejas, utilizaremos una sola guía específica y reproducible:

**[Abrir la guía de Gene Ontology/PANTHER, paso a paso](./guia_GO_PANTHER_paso_a_paso.md)**.

La guía explica cómo cargar `genes_<código>.txt`, cambiar la lista de referencia por `background_<código>.txt`, seleccionar **Biological Process**, realizar el **Overrepresentation Test** con **Fisher** y **FDR**, interpretar los resultados y conservar evidencias de la configuración. No se requiere programación. Como apoyo externo, puede consultarse la [guía oficial de Gene Ontology](https://geneontology.org/docs/go-enrichment-analysis/).

---

## 9. Archivos de datos para descargar

Cada pareja debe descargar **solo el conjunto asignado**, descomprimirlo y leer su `ficha_<codigo>.md` antes de comenzar. Cada ZIP contiene cinco archivos: `genes_<codigo>.csv`, `genes_<codigo>.txt`, `background_<codigo>.csv`, `background_<codigo>.txt` y `ficha_<codigo>.md`. Los CSV conservan los campos documentados; los TXT facilitan copiar los identificadores a los servicios de análisis.

| Factor | Código | Condición | Descarga |
|---|---|---|---|
| Glucosa | G1 | 2 g/L, 20 min | [Conjunto G1](./datos/conjunto_G1.zip) |
| Glucosa | G2 | 2 g/L, 45 min | [Conjunto G2](./datos/conjunto_G2.zip) |
| Glucosa | G3 | 0,2 g/L, 45 min | [Conjunto G3](./datos/conjunto_G3.zip) |
| Temperatura | T1 | 37 °C, 4 min | [Conjunto T1](./datos/conjunto_T1.zip) |
| Temperatura | T2 | 37 °C, 11 min | [Conjunto T2](./datos/conjunto_T2.zip) |
| Temperatura | T3 | 37 °C, 26 min | [Conjunto T3](./datos/conjunto_T3.zip) |
| pH | P1 | pH 8,0, 6 min | [Conjunto P1](./datos/conjunto_P1.zip) |
| pH | P2 | pH 8,0, 20 min | [Conjunto P2](./datos/conjunto_P2.zip) |
| pH | P3 | pH 8,0, 40 min | [Conjunto P3](./datos/conjunto_P3.zip) |

