# Solución de la actividad guiada: identificación de una secuencia mediante BLAST

**Asignatura:** Bioinformática (Grado en Biotecnología)  
**Tema:** 5. Búsqueda y alineamiento de secuencias  
**Documento:** guía de corrección para el profesorado

> **Nota:** Esta solución corresponde a la secuencia FASTA de 189 nucleótidos del archivo `actividad_blast_fasta.md`, con identificador `muestra_01_fragmento_ADN`. La identificación se ha contrastado con el registro de referencia de NCBI.

## 1. Identificación de la secuencia

La secuencia utilizada corresponde a un fragmento inicial de la **región codificante del gen HBB** de **_Homo sapiens_** (ser humano), que codifica la **subunidad beta de la hemoglobina**.

Referencia de NCBI: **NM_000518.5** — *Homo sapiens hemoglobin subunit beta (HBB), mRNA*.

- Registro: https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5
- Herramienta: https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch

## 2. Respuestas orientativas a las preguntas guiadas

### Pregunta 1. Primera coincidencia

**Respuesta esperada:** una secuencia anotada como **_Homo sapiens_**, asociada al **gen HBB**, por ejemplo una entrada descrita como *Homo sapiens hemoglobin subunit beta (HBB), mRNA*.

**Interpretación:** la coincidencia permite identificar el fragmento como perteneciente a la beta-globina humana. Debe aceptarse otra descripción equivalente si el resultado identifica correctamente el organismo y el gen.

**Precaución:** no se debe exigir que un acceso específico ocupe siempre la primera posición; varios registros pueden presentar alineamientos excelentes y el orden depende de la base de datos y de sus actualizaciones.

### Pregunta 2. Porcentaje de identidad (Per. Ident)

**Valor esperado para una coincidencia exacta:** **100 %**.

**Interpretación:** todas las posiciones de la región alineada coinciden entre la consulta y la secuencia encontrada. Un 100 % de identidad **no significa** necesariamente que ambas secuencias tengan la misma longitud total: la consulta puede ser solo un fragmento de un transcrito más largo.

**Criterio de corrección:** el alumnado debe transcribir el valor del resultado que haya seleccionado e interpretarlo correctamente. Si selecciona otra coincidencia, su identidad puede ser inferior al 100 %.

### Pregunta 3. Cobertura (Query Cover)

**Valor esperado para una coincidencia que abarque íntegramente el fragmento:** **100 %**.

**Interpretación:** el alineamiento cubre los **189 nucleótidos de la secuencia consultada**. No implica que se haya cubierto el 100 % de la secuencia de referencia encontrada, que puede ser considerablemente más larga.

**Ejemplo didáctico:** una secuencia de referencia de varios cientos de nucleótidos puede mostrar **100 % de cobertura de la consulta** cuando contiene completamente los 189 nucleótidos del ejercicio.

### Pregunta 4. E-value

**Respuesta esperada:** un **E-value muy pequeño**, indicativo de que un alineamiento de esa puntuación difícilmente se produciría por azar en la base de datos consultada.

**No se fija aquí un valor numérico**, porque depende de la ejecución concreta, del tamaño de la base de datos y de la configuración de BLAST. El alumnado debe copiar el valor mostrado en su propia búsqueda.

**Interpretación correcta:** el E-value estima el **número esperado de alineamientos de puntuación igual o superior obtenidos por azar**, dadas las condiciones de búsqueda. **No es la probabilidad de que la identificación biológica sea incorrecta**. Si aparece `0.0`, es un valor redondeado por la herramienta, no una probabilidad matemática literalmente nula.

### Pregunta 5. Comparación entre coincidencias

**Respuesta esperada:** **no necesariamente** todas las coincidencias corresponden a la misma especie ni tienen identidad del 100 %.

Es posible encontrar registros de HBB de la especie humana y secuencias relacionadas de otras especies, así como variantes o secuencias con sustituciones. La composición exacta de la lista depende de las secuencias existentes en la base de datos elegida (**RefSeq RNA**) y del orden de los resultados.

**Criterio de corrección:** aceptar una respuesta argumentada mediante dos o más coincidencias reales. Si las primeras filas solo contienen secuencias humanas, el alumnado **no debe afirmar** por ello que todas las coincidencias de la búsqueda pertenecen a la misma especie; puede examinar otras filas.

## 3. Solución de la puesta en común

**Pregunta:** Si dos secuencias presentan un 99 % de identidad, ¿podemos asegurar que pertenecen a la misma especie?

**Respuesta: no.** El porcentaje de identidad cuantifica la similitud de las posiciones alineadas, pero no determina por sí solo la pertenencia a una especie. Dos especies pueden conservar regiones muy similares de determinados genes; también existen variantes dentro de una misma especie. Deben considerarse la cobertura, la longitud alineada, las alternativas y el contexto biológico.

## 4. Completar la conclusión

> BLAST nos permite **comparar** una secuencia desconocida con otras registradas en bases de datos. Para valorar una coincidencia hemos observado **el porcentaje de identidad**, **la cobertura de la consulta** y **el E-value**.

## 5. Aspectos importantes a tener en cuenta

- **Identidad y cobertura son medidas distintas:** 100 % de identidad puede corresponder a un alineamiento que cubra solo una parte de la consulta.
- **Un E-value menor es estadísticamente más significativo**, pero no demuestra por sí solo la función biológica ni la especie.
- **La primera fila no tiene por qué ser siempre el mismo registro:** lo relevante es justificar la interpretación con los datos de la búsqueda.
- **RefSeq RNA contiene transcritos de referencia:** la secuencia de consulta se escribe con letras A, C, G y T, aunque la base elegida contenga registros de ARN mensajero representados como secuencias de nucleótidos.
- **Evitar la sobreinterpretación:** BLAST identifica similitud entre secuencias; la identidad del organismo se infiere considerando la anotación y la evidencia disponible.

## 6. Fuentes

1. NCBI. **Homo sapiens hemoglobin subunit beta (HBB), mRNA**, RefSeq NM_000518.5: https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5
2. NCBI. **Nucleotide BLAST**: https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch
3. NCBI. **BLAST Help**: https://blast.ncbi.nlm.nih.gov/doc/blast-help/


