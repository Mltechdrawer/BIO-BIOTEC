# Actividad 2. Una secuencia muy parecida, ¿la misma especie?

**Asignatura:** Bioinformática (Grado en Biotecnología)  
**Tema:** 5. Búsqueda y alineamiento de secuencias  
**Duración estimada:** 8–10 minutos  
**Modalidad:** individual o por parejas  
**Requisito:** haber completado la actividad de identificación con BLAST y conservar sus resultados abiertos.

## 1. Planteamiento

En la primera actividad hemos buscado un fragmento de 189 nucleótidos en formato FASTA utilizando **Nucleotide BLAST**, **RefSeq RNA** y **megablast**, sin restringir el organismo. Ahora examinaremos cómo se corresponden las posiciones de la consulta con dos secuencias encontradas.

**Objetivo:** leer un alineamiento, relacionar sus posiciones con la identidad y la cobertura, y valorar si una identidad muy elevada permite identificar por sí sola una especie.

No necesitas modificar el FASTA ni ejecutar otra búsqueda si mantienes abiertos los resultados. Si han caducado, repite la búsqueda de la primera actividad con su misma secuencia y configuración.

## 2. Leer el alineamiento humano

1. En **Descriptions**, localiza el resultado **Homo sapiens hemoglobin subunit beta (HBB), mRNA**, con acceso **NM_000518.5**. No te guíes únicamente por su posición en la lista.
2. Pulsa su descripción para abrir el alineamiento en **Alignments**.
3. Identifica los elementos siguientes:

| Elemento | Qué representa |
|---|---|
| **Query** | La secuencia de 189 nucleótidos que introdujiste en FASTA. |
| **Sbjct** | La secuencia de referencia encontrada en la base de datos. |
| Barras verticales entre las secuencias | Posiciones con nucleótidos idénticos. |
| **Identities** | Número de posiciones idénticas respecto al total de posiciones alineadas. |
| **Gaps** | Huecos introducidos en el alineamiento. |
| **Length**, junto al acceso | Longitud completa de la secuencia de referencia. |

Los números que flanquean cada línea indican las posiciones en cada secuencia. La consulta y la referencia pueden comenzar en posiciones diferentes.

**Pregunta 1.** Anota las posiciones inicial y final de **Query** y de **Sbjct**, el valor de **Identities** y la longitud completa del transcrito humano.

**Respuesta:**

**Pregunta 2.** El resultado humano muestra una cobertura de la consulta del 100 %. ¿Significa que hemos alineado todo el transcrito de referencia? Explica qué secuencia queda cubierta completamente.

**Respuesta:**

## 3. Examinar una coincidencia de otra especie

4. Regresa a **Descriptions** y localiza **Pan paniscus**, preferentemente el acceso **XM_003819029.5**. Pulsa su descripción para abrir su alineamiento.
5. Compara el primer bloque de **Query** y **Sbjct**. Busca una posición sin barra vertical y comprueba qué letra aparece en cada secuencia.
6. Anota el valor de **Identities**, los **Gaps** y, en la tabla Descriptions, **Query Cover** y **Per. Ident**.

**Pregunta 3.** ¿En qué posición de la consulta aparece la diferencia? ¿Qué nucleótido contiene la consulta y cuál la referencia? ¿Cuántas posiciones coinciden y cuántas se han alineado?

**Respuesta:**

7. Calcula el porcentaje de identidad: **posiciones idénticas / posiciones alineadas × 100**. Puedes utilizar una calculadora.

**Pregunta 4.** ¿Qué porcentaje obtienes? Compáralo con **Per. Ident** en Descriptions y con el porcentaje que aparece junto a **Identities** en Alignments. Si difieren ligeramente, ¿puede explicarse por el redondeo?

**Respuesta:**

> **Si no encuentras el acceso indicado:** consulta al profesorado. Las bases de datos se actualizan; no inventes valores ni asumas que otra coincidencia tendrá exactamente las mismas diferencias. El profesorado puede facilitar las capturas documentadas para completar esta comparación.

## 4. Interpretar la evidencia

8. Redacta una conclusión de dos o tres frases apoyándote en los resultados humano y de Pan paniscus.

**Pregunta 5.** ¿Podemos asegurar que dos secuencias proceden de la misma especie solo porque superan el 99 % de identidad? Justifica tu respuesta con las coincidencias examinadas.

**Respuesta:**

## 5. Puesta en común

Comenta con el grupo: **BLAST realiza alineamientos locales. ¿Es compatible con que el alineamiento humano cubra el 100 % de nuestra consulta?** Ten en cuenta que la consulta es un fragmento y la referencia un transcrito más largo.

## 6. Entrega breve

Entrega las cinco respuestas. Identifica los dos accesos examinados y añade la fecha de la búsqueda. Una captura de cada alineamiento es opcional si lo indica el profesorado.

## Fuentes

- [Tema 5. Búsqueda y alineamiento de secuencias](https://mltechdrawer.github.io/BIO-BIOTEC/bloque2_analisis_secuencias/teoria/tema05_busqueda_alineamiento/)
- [NCBI Nucleotide BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch)
- [NCBI BLAST Help](https://blast.ncbi.nlm.nih.gov/doc/blast-help/)

