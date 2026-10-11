# Actividad guiada: identificación de una secuencia mediante BLAST

**Asignatura:** Bioinformática (Grado en Biotecnología)  
**Tema:** 5. Búsqueda y alineamiento de secuencias  
**Duración estimada:** 20–25 minutos  
**Modalidad:** actividad individual o por parejas  
**Nivel:** introductorio

## 1. Planteamiento

En una muestra biológica se ha identificado un fragmento de una secuencia de nucleótidos. No conocemos inicialmente a qué organismo pertenece ni qué gen representa. Utilizaremos **BLAST** para buscar secuencias similares en las bases de datos de NCBI y formular una identificación razonada.

**Objetivo:** aprender a ejecutar una búsqueda *Nucleotide BLAST* con una secuencia en formato FASTA e interpretar las coincidencias a partir de la descripción, el porcentaje de identidad, la cobertura y el E-value.

## 2. Secuencia de partida

Copia **todo** el siguiente bloque, incluida la primera línea que comienza por `>`:

```fasta
>muestra_01_fragmento_ADN
ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTG
GATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTC
TTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCT
```

**¿Qué es FASTA?** Es un formato de texto sencillo: la primera línea contiene un identificador precedido por `>` y las líneas siguientes contienen la secuencia. El identificador `muestra_01_fragmento_ADN` se ha asignado únicamente para este ejercicio.

## 3. Ejecutar la búsqueda

1. Abre [NCBI Nucleotide BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch).
2. En **Enter Query Sequence**, pega la secuencia FASTA completa del apartado 2.
3. En **Database**, selecciona **RefSeq RNA** si aparece disponible. La secuencia del ejercicio pertenece a la región codificante de un transcrito, por lo que es una elección adecuada para esta primera búsqueda.
4. Deja **Organism** vacío: queremos que BLAST pueda encontrar coincidencias de diferentes especies.
5. En **Program Selection**, selecciona **Highly similar sequences (megablast)**.
6. Mantén el resto de parámetros con sus valores predeterminados y pulsa **BLAST**.
7. Una vez termine la búsqueda, abre la sección **Descriptions** y examina las primeras coincidencias.

> **Importante:** los nombres de algunas opciones pueden variar ligeramente según la versión de la interfaz de NCBI. Si no encuentras «RefSeq RNA», consulta al profesorado antes de sustituirla por otra base de datos.

## 4. Interpretar los resultados

En la tabla de resultados, identifica estas columnas:

| Columna | Interpretación inicial |
|---|---|
| **Description** | Nombre o descripción de la secuencia encontrada. |
| **Query Cover** | Porcentaje de la secuencia consultada que queda cubierto por el alineamiento. |
| **Per. Ident** | Porcentaje de posiciones idénticas dentro de la región alineada. |
| **E-value** | Número esperado de alineamientos con una puntuación igual o mejor que podrían aparecer por azar en una búsqueda de ese tamaño. Cuanto menor, mayor significación estadística. |

No es necesario modificar los parámetros avanzados ni interpretar todos los valores de BLAST.

## 5. Preguntas guiadas

Anota tus respuestas a partir de los resultados **reales de tu búsqueda**:

1. **Primera coincidencia:** ¿Qué organismo y qué gen aparecen en la primera coincidencia? Copia su descripción.

   **Respuesta:**

2. **Identidad:** ¿Cuál es su valor de **Per. Ident**? ¿Qué nos indica?

   **Respuesta:**

3. **Cobertura:** ¿Cuál es su **Query Cover**? ¿A qué se refiere este porcentaje?

   **Respuesta:**

4. **Significación estadística:** ¿Qué **E-value** presenta? ¿Sugiere una coincidencia que difícilmente se debe al azar?

   **Respuesta:**

5. **Comparación:** Examina alguna de las siguientes coincidencias. ¿Todas corresponden necesariamente a la misma especie? ¿Tienen todas un 100 % de identidad?

   **Respuesta:**

## 6. Puesta en común

**Pregunta para debatir:** Si dos secuencias presentan un 99 % de identidad, ¿podemos asegurar que pertenecen a la misma especie?

Una identidad elevada indica una gran similitud en la región alineada, pero **no permite, por sí sola, identificar inequívocamente la especie**. Es necesario considerar también la cobertura, las alternativas encontradas y el contexto biológico de la secuencia.

## 7. Conclusión

Completa la siguiente frase:

> BLAST nos permite ______________________ una secuencia desconocida con otras registradas en bases de datos. Para valorar una coincidencia hemos observado ______________________, ______________________ y ______________________.

---

## Referencias y procedencia de la secuencia

- [NCBI Nucleotide BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch)
- [NCBI: formatos admitidos para la consulta, incluido FASTA](https://www.ncbi.nlm.nih.gov/blast/fasta.shtml)
- [NCBI: registro de referencia NM_000518.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5)
- [Alliance of Genome Resources: HBB, secuencia codificante de referencia](https://www.alliancegenome.org/gene/HGNC%3A4827)

**Nota para el profesorado (retirar antes de entregar, si se desea mantener la incógnita):** el fragmento corresponde al comienzo de la secuencia codificante del gen **HBB** (*hemoglobin subunit beta*) de *Homo sapiens*, tomada de la presentación de secuencia del transcrito ENST00000335295.4 en Alliance of Genome Resources. Se ha ocultado su identidad en la cabecera FASTA para que el alumnado la investigue. La coincidencia concreta y sus métricas deben verificarse con la búsqueda de BLAST al realizar la actividad; pueden variar con las actualizaciones de bases de datos y de la interfaz.
