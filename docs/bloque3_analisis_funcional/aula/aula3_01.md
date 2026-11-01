# Práctica · Anotación computacional de proteínas

## 1. Planteamiento

Un equipo de investigación ha obtenido una secuencia de aminoácidos sin identificar. Tu tarea es proponer una **anotación funcional razonada**: qué proteína puede ser, qué actividad desempeña y qué evidencias sustentan esa conclusión. No basta con copiar la descripción de una base de datos: hay que explicar el camino seguido y el grado de confianza de cada afirmación.

## 2. Objetivos de aprendizaje

- Reconocer las etapas básicas de un flujo de anotación funcional.
- Interpretar resultados de similitud (identidad, cobertura, E-value) sin equiparar similitud con demostración de función.
- Relacionar dominios y familias de proteínas con posibles funciones biológicas.
- Diferenciar anotaciones revisadas, predicciones computacionales y evidencia experimental.
- Redactar una anotación funcional trazable, con referencias y limitaciones.

## 3. Material de partida

Disponen de la siguiente secuencia de aminoácidos en formato FASTA. El identificador es deliberadamente neutro para realizar primero el análisis sin conocer su identidad. **No deben modificar la secuencia.**

```fasta
>PROTEINA_X | muestra para anotación
MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTRA
TNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRD
PQGIRAWVAWRNRCQNRDVRQYVQGCGV
```

Deben utilizar **NCBI Protein BLAST (BLASTp)**, **InterPro** y **UniProtKB**. Conserven los identificadores y enlaces de todos los registros consultados.

## 4. Actividades

### Actividad 1 · Revisión inicial de la secuencia

1. Guardar la secuencia en un archivo FASTA. Comprobar que el alfabeto corresponde a una proteína y anota su longitud.
2. Antes de consultar bases de datos, deben explicar por qué la secuencia por sí sola no permite asegurar su función biológica.

### Actividad 2 · Búsqueda por similitud con BLASTp

1. Buscar la secuencia mediante BLASTp en una base de datos de proteínas apropiada. Indicar la base de datos seleccionada y la fecha de consulta.
2. Recoger **tres coincidencias relevantes**: identificador, organismo, descripción, identidad, cobertura de la consulta y E-value.
3. Proponer una primera hipótesis de identidad o familia de proteína y explica qué resultados la apoyan. ¿Qué no puede demostrarse solamente con BLASTp?

### Actividad 3 · Dominios y familias con InterPro

1. Analizar la secuencia en InterPro, mediante búsqueda de secuencia si el servicio está disponible o a partir de un identificador de proteína obtenido anteriormente.
2. Anotar la familia o firmas identificadas y, cuando proceda, sus posiciones aproximadas en la secuencia. Distingue **dominio, familia y motivo** si aparecen resultados de distintos tipos.
3. Explicar si el análisis de InterPro respalda, matiza o contradice la hipótesis obtenida con BLASTp.

### Actividad 4 · Contraste de anotaciones con UniProtKB

1. Localizar el registro de UniProtKB que mejor corresponda a la secuencia. Indica su accesión, organismo, nombre recomendado y estado de revisión.
2. Recoger la función, actividad molecular, localización y alguna característica relevante que conste en el registro. Para cada afirmación principal identifica, cuando figure, si procede de literatura/experimentos, inferencia o anotación automática.
3. Comparar el registro principal con otro resultado relacionado o no revisado, si está disponible. Describe una diferencia en la precisión de la anotación o en la evidencia disponible; si no encuentras uno apropiado, justifícalo.

### Actividad 5 · Informe de anotación funcional

1. Redactar una **anotación final de 5–8 líneas** que incluya: nombre propuesto, función, familia o rasgo de secuencia que la sustenta, localización si está respaldada, fuentes consultadas y grado de certeza.
2. Indicar **dos limitaciones concretas** del procedimiento y una comprobación adicional que permitiría aumentar la confianza en la anotación.
3. Responder brevemente: **¿por qué no es correcto afirmar que la función está demostrada experimentalmente solo porque BLASTp devuelve una coincidencia con E-value muy bajo?**

## 5. Entrega 

Deben entregar **un archivo PDF** con el informe (2–3 páginas), una tabla de coincidencias BLASTp y las referencias o URL de las entradas utilizadas. Las capturas de pantalla son opcionales.

## 6. Recursos

- [Tema 7. Anotación computacional de genes y proteínas](https://mltechdrawer.github.io/BIO-BIOTEC/bloque3_analisis_funcional/teoria/tema07_anotacion_computacional/)
- [NCBI BLASTp](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins)
- [InterPro](https://www.ebi.ac.uk/interpro/)
- [UniProtKB](https://www.uniprot.org/uniprotkb)
