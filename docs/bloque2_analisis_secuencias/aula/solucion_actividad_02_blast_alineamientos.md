# Solución de la actividad 2. Una secuencia muy parecida, ¿la misma especie?

**Asignatura:** Bioinformática (Grado en Biotecnología)  
**Tema:** 5. Búsqueda y alineamiento de secuencias  
**Documento:** guía de corrección para el profesorado

## 1. Ejecución de referencia

Esta solución utiliza los resultados **observados el 11 de octubre de 2026** en la búsqueda de la primera actividad. Se reutiliza esa ejecución para examinar dos alineamientos; no se presenta como una segunda búsqueda independiente.

- **Consulta:** `muestra_01_fragmento_ADN`, 189 nucleótidos, FASTA de la primera actividad.
- **Base de datos:** Reference RNA sequences (`refseq_rna`).
- **Algoritmo:** megablast, sin restricción de organismo ni exclusión de modelos XM.
- **RID:** `CRH6UC2H014`.
- **Registro humano:** `NM_000518.5`.
- **Registro de Pan paniscus:** `XM_003819029.5`.

| Resultado | Longitud de referencia | Query | Sbjct | Identidades | Gaps | Cobertura de consulta | Identidad en Descriptions | E-value |
|---|---:|---|---|---|---|---:|---:|---|
| Homo sapiens, HBB | 628 nt | 1–189 | 51–239 | 189/189 | 0/189 | 100 % | 100,00 % | 2e-92 |
| Pan paniscus, beta-globina | 643 nt | 1–189 | 66–254 | 188/189 | 0/189 | 100 % | 99,47 % | 7e-91 |

Estos valores corresponden a los accesos y la ejecución indicados. Las futuras búsquedas pueden devolver otros registros, orden o métricas.

## 2. Respuestas a las preguntas

### Pregunta 1. Leer el alineamiento humano

**Query:** desde 1 hasta 189.  
**Sbjct:** desde 51 hasta 239.  
**Identities:** 189/189 (100 %).  
**Longitud del transcrito:** 628 nucleótidos.

Todas las posiciones de la consulta coinciden con una región interna del transcrito. Las barras verticales señalan esas coincidencias. No se han introducido huecos: **Gaps = 0/189 (0 %)**.

### Pregunta 2. Interpretar la cobertura

**No:** una cobertura de la consulta del 100 % no significa haber alineado todo el transcrito de referencia. Se han cubierto los **189 nucleótidos de Query**, alineados con las posiciones 51–239 de Sbjct. La referencia completa mide 628 nucleótidos.

Como comprobación adicional para el profesorado, la región alineada representa aproximadamente **189/628 × 100 = 30,10 %** de la referencia. Este cálculo no es el valor de la columna **Query Cover** ni es necesario exigirlo al alumnado.

### Pregunta 3. Localizar la diferencia

La diferencia aparece en la **posición 9 de Query**: la consulta contiene **T** y la referencia de Pan paniscus contiene **C**. Corresponde a la posición **74 de Sbjct**, porque el alineamiento comienza en la posición 66 de esa referencia.

- Consulta, primeras 12 bases: `ATGGTGCATCTG`.
- Referencia, región correspondiente: `ATGGTGCACCTG`.

Se alinean **189 posiciones**, de las cuales **188 son idénticas**. Hay una discrepancia y ningún hueco. En este caso, la diferencia es una sustitución, no una inserción o una deleción. Esta observación no permite deducir por sí sola un efecto funcional.

### Pregunta 4. Calcular e interpretar el porcentaje

**188/189 × 100 = 99,470899… %**, que se expresa como **99,47 %** al redondear a dos decimales.

En esta ejecución, **Descriptions** muestra `99.47%`, mientras que el panel **Alignments** muestra `188/189 (99%)`. Es el mismo cociente con diferente precisión de presentación. No hay una contradicción entre los resultados.

La cobertura de la consulta sigue siendo del **100 %**: la posición diferente está alineada y cuenta para la cobertura, aunque no sea idéntica.

### Pregunta 5. Identidad y especie

**No podemos asegurarlo únicamente con ese porcentaje.** La consulta coincide exactamente con HBB humano, pero también presenta un **99,47 % de identidad con cobertura completa frente a Pan paniscus**, otra especie. Una región conservada puede ser muy parecida entre especies distintas.

La identificación prevista en la primera actividad se apoya en la coincidencia exacta humana, la anotación del registro y la comparación de alternativas. BLAST muestra similitud; un umbral de identidad aislado no constituye una identificación inequívoca de especie.

## 3. Solución de la puesta en común

**Sí, es compatible.** Un alineamiento local busca regiones similares sin obligar a alinear la totalidad de ambas secuencias. En este caso, la región encontrada contiene toda la consulta de 189 nucleótidos, pero solo una parte del transcrito humano de 628 nucleótidos.

Por tanto, **100 % de cobertura de Query no convierte el resultado en un alineamiento global de ambas secuencias completas**.

## 4. Orientaciones para corregir

Valorar que el alumnado distinga Query de Sbjct, ubique la discrepancia, explique el cálculo de identidad y razone por qué cobertura e identidad son diferentes. No es necesario exigir la posición 74 de la referencia ni el cálculo del 30,10 %.

Si se utiliza otra ejecución, comprobar sus accesos y capturas antes de aplicar los valores numéricos de esta guía. Aceptar valores diferentes cuando estén documentados y correctamente interpretados. Si no se dispone del registro previsto, facilitar el Word con las imágenes de referencia.

## 5. Fuentes y trazabilidad

- [NCBI BLAST, ejecución CRH6UC2H014](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Get&RID=CRH6UC2H014). Enlace temporal; la evidencia se conserva en el Word.
- [NCBI RefSeq, HBB humano NM_000518.5](https://www.ncbi.nlm.nih.gov/nuccore/NM_000518.5).
- [NCBI RefSeq, Pan paniscus XM_003819029.5](https://www.ncbi.nlm.nih.gov/nuccore/XM_003819029.5).
- [NCBI BLAST Help](https://blast.ncbi.nlm.nih.gov/doc/blast-help/).
- [Tema 5 de la asignatura](https://mltechdrawer.github.io/BIO-BIOTEC/bloque2_analisis_secuencias/teoria/tema05_busqueda_alineamiento/).

**Confianza: 99 %** en la transcripción e interpretación de la ejecución documentada. La duración de la actividad es una estimación didáctica.
