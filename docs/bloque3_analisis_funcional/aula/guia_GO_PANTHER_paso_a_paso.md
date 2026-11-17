# Guía práctica: enriquecimiento GO con Gene Ontology y PANTHER

**Asignatura:** Bioinformática · 2.º de Biotecnología  
**Actividad:** tema 8 · análisis de sobrerrepresentación de procesos biológicos  
**Modalidad:** trabajo en parejas · exclusivamente mediante navegador web, sin programación ni instalaciones.

> **Objetivo:** analizar una lista real de genes de *Saccharomyces cerevisiae* en comparación con su conjunto de referencia (*background*), identificar términos **GO Biological Process** sobrerrepresentados y documentar los resultados. **No deben cambiar la configuración para obtener resultados significativos**: que no aparezcan términos significativos también es un resultado válido.

## Antes de comenzar: archivos y conceptos

1. Deben descargar en el [enunciado de la práctica](./aula3_06.md#9-archivos-de-datos-para-descargar) el ZIP de otra pareja (G1–G3, T1–T3 o P1–P3) y **descomprimirlo**.
2. Abrir la ficha `ficha_<código>.md` y anotadr el estudio GEO, la condición y cómo se seleccionaron los genes.
3. Identificar los dos ficheros **de texto**: `genes_<código>.txt` (genes de interés) y `background_<código>.txt` (universo). Ambos tienen **un ID de levadura por línea**; ejemplo: `YAL003W`. No deben introducir las columnas del CSV ni intercambiar archivos de códigos diferentes.
4. Tengan presente que las listas fueron seleccionadas por un **criterio exploratorio de cambio de expresión**, no por una prueba de expresión diferencial con FDR. El FDR que calcularemos ahora corresponde al **enriquecimiento GO**, no al cambio de expresión.

## Parte A. Preparar la consulta en Gene Ontology

1. Entren en **[Gene Ontology: herramienta de enriquecimiento](https://geneontology.org/)**. En la página principal deben buscar **Enrichment analysis / GO enrichment analysis**.
2. Localizar el campo donde introducir los genes. Abrir `genes_<código>.txt`, seleccionar **todo el texto** y pegar los identificadores (uno por línea). La guía oficial admite identificadores de organismo modelo, pero **no garantiza que se reconozca la totalidad** de nuestra lista: comprobádlo al visualizar los resultados.
3. En **GO aspect**, escojan **Biological Process (BP)**. No seleccionéis Molecular Function ni Cellular Component en esta primera ejecución.
4. En **Species / Organism**, escojan ***Saccharomyces cerevisiae***, comprobando que no permanece *Homo sapiens* (valor predeterminado en la guía oficial).
5. Pulsen **Submit / Submit query**. Se abrirá el análisis en **PANTHER**, el servicio enlazado desde Gene Ontology.

**Importante:** este primer resultado suele utilizar **todos los genes de la especie** como referencia. **No lo interpretéis como resultado final**, porque nuestra práctica requiere el background experimental incluido en el ZIP.

## Parte B. Sustituir obligatoriamente el background

6. En la pantalla de resultados de PANTHER, localicen la sección **Analysis Summary** y la línea **Reference list**. Pulsen **Change** junto a *Reference list*.
7. En la pantalla para cambiar la referencia, escojan la opción de **subir una lista de referencia propia (custom reference list / Upload Reference List)**. Seleccionen *S. cerevisiae* si lo solicita.
8. Deben cargar **`background_<código>.txt`**, o pegar su contenido completo si la página ofrece un área para introducir IDs. **No carguéis `genes_<código>.txt` en este paso**. En el selector de tipo de lista, utilicen la opción para identificadores de genes/proteínas, si aparece.
9. Acepten la carga y pulsen **Launch analysis** (o el control equivalente de volver a ejecutar). Confirmen que la línea **Reference list** ahora identifica la referencia cargada y no el genoma completo.
10. Si PANTHER rechaza la lista o no muestra una referencia personalizada, **detengan la interpretación**, conserven el aviso y comuniquenlo al profesorado. No deben sustituir el background por uno distinto sin autorización.

## Parte C. Verificar los parámetros de análisis

11. En **Analysis Summary**, verifiquen o ajusten los siguientes parámetros, conservándolos iguales para todas las parejas:

| Parámetro | Valor obligatorio |
|---|---|
| Organismo | *Saccharomyces cerevisiae* |
| Lista analizada | `genes_<código>.txt` |
| Reference list | `background_<código>.txt` **cargado por la pareja** |
| Analysis Type | **PANTHER Overrepresentation Test** (no *Statistical Enrichment Test*) |
| Annotation Data Set | **GO biological process complete** (si figura esa opción; en todo caso, Biological Process, no GO-slim) |
| Test Type | **Fisher's Exact** |
| Correction | **False Discovery Rate (FDR)** |
| Criterio de selección en el informe | **FDR < 0,05** |

12. Si han cambiado algún parámetro, pulsen **Launch analysis / Re-run** para recalcular. Comprueben de nuevo **Reference list**.
13. Observen si PANTHER avisa sobre identificadores **no reconocidos**. Registren el número si se muestra. El total efectivo de genes reconocidos puede ser inferior al total del TXT; no lo oculten ni reemplacen genes por aproximación.

## Parte D. Leer e interpretar la tabla

14. Localicen la **tabla de resultados de sobrerrepresentación**. Puede incluir tanto categorías sobrerrepresentadas (`+`) como infrarrepresentadas (`−`); **para esta práctica examinen las sobrerrepresentadas**.
15. Para cada término seleccionado registren: **identificador GO, nombre del proceso, número de genes en la lista asociado a ese término, frecuencia en el background, número esperado, fold enrichment y FDR**, según los campos que muestre la interfaz. Si falta un campo, deben escribir «no mostrado».
16. **Seleccionen hasta cinco términos GO:BP representativos** con FDR < 0,05, si existen. Eviten elegir cinco términos casi idénticos sin explicar su jerarquía. Si no hay ninguno, registren «ningún término GO:BP significativo con FDR < 0,05» y explíquenlo.
17. Consulten el identificador de algún término en la ontología, comprueben su definición y revisen **qué genes de la lista contribuyen** al resultado. No deduzcan activación, inhibición ni causalidad únicamente del enriquecimiento.
18. **Guarden la tabla** con la opción de descarga/exportación que ofrezca la página. Guarden también una captura o registro de **Analysis Summary** que muestre el background y los parámetros. Si la interfaz no permite exportar, documenten al menos cinco filas en la tabla y guarden capturas.

| GO ID | Proceso biológico (BP) | Genes observados | Esperados | Fold enrichment | FDR | Comentario |
|---|---|---:|---:|---:|---:|---|
| … | … | … | … | … | … | … |

## Parte E. Verificación y problemas frecuentes

Antes de interpretar, comprueben que: (a) la especie sea *S. cerevisiae*; (b) los dos TXT pertenezcan al mismo código; (c) la referencia no sea el genoma completo; (d) el análisis sea **Overrepresentation Test**, no otro tipo de análisis; (e) se usen **GO biological process**, **Fisher** y **FDR**; y (f) comprueben que han documentado la cantidad de IDs reconocidos así como la fecha.

| Situación | Qué hacer |
|---|---|
| Resultados iniciales con todos los genes del genoma como referencia | Ir a **Reference list → Change**, cargar el TXT de background y volver a ejecutar. |
| Aparece *Homo sapiens* | Seleccionar ***Saccharomyces cerevisiae***, repetir y comprobar los genes reconocidos. |
| Se ha seleccionado **Statistical Enrichment Test** | Cambiar a **Overrepresentation Test**; las listas no son un ranking con puntuaciones para ese otro procedimiento. |
| Aparece GO-slim o Molecular Function | Seleccionar **GO biological process complete** para el análisis común. |
| No hay términos con FDR < 0,05 | Mantener los parámetros y reportar la ausencia de significación. |
| Hay identificadores desconocidos | Documentarlos; no inventar correspondencias ni completar con otros genes. |
| PANTHER cambia sus controles o no acepta la referencia | Consultar la guía oficial y comunicar el problema; no improvisar un análisis diferente. |

## Qué hay que entregar de esta etapa

Una tabla de hasta cinco términos BP, el archivo o captura de resultados, el resumen de parámetros, el número de genes reconocidos (si consta), una interpretación breve y una nota sobre las limitaciones. Deben integrar ese material en el informe solicitado por el enunciado general.

## Referencias oficiales

- [Gene Ontology — GO enrichment analysis](https://geneontology.org/docs/go-enrichment-analysis/): **referencia principal** de la secuencia de pantallas, incluida **Reference list → Change → Launch analysis**.
- [PANTHER — Overrepresentation Test](https://pantherdb.org/webservices/go/overrep.jsp): plataforma de análisis enlazada desde Gene Ontology.
- [PANTHER — documentación de ayuda](https://pantherdb.org/help/PANTHERhelp.jsp): detalles de tipos de análisis, identificadores y parámetros.

