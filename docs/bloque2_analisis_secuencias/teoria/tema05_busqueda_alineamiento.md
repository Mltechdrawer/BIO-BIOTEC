# Tema 5. Búsqueda y alineamiento de secuencias

## Duración

**2 horas de teoría**

Este tema forma parte del **Bloque II. Métodos computacionales para el análisis de secuencias**.

De acuerdo con la guía docente, se estructura en tres apartados:

- **5.1. Alineamiento local y global.**
- **5.2. BLAST.**
- **5.3. Evaluación de resultados y métricas.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar qué es un alineamiento de secuencias y para qué se utiliza.
- Diferenciar entre alineamiento global y alineamiento local.
- Comprender, a nivel conceptual, cómo funcionan los algoritmos clásicos de alineamiento.
- Explicar qué problema resuelve BLAST y por qué utiliza una estrategia heurística.
- Distinguir entre los principales tipos de BLAST.
- Interpretar correctamente identidad, cobertura, puntuación y E-value.
- Reconocer cuándo un resultado es potencialmente relevante y cuándo necesita una interpretación más cuidadosa.
- Comprender que una coincidencia computacional no equivale automáticamente a una conclusión biológica.

---

# Introducción

En el tema anterior vimos que comparar secuencias exige definir criterios objetivos.

También vimos que un algoritmo debe decidir:

- qué posiciones se corresponden;
- qué diferencias son aceptables;
- dónde introducir gaps;
- y cómo valorar el resultado.

En este tema damos el siguiente paso.

Ya no preguntamos únicamente:

> **¿Qué significa comparar dos secuencias?**

Ahora nos preguntamos:

> **¿Cómo se realiza esa comparación y cómo se interpretan los resultados?**

El alineamiento constituye una de las herramientas fundamentales de la Bioinformática.

Permite estudiar:

- similitud entre secuencias;
- posibles relaciones evolutivas;
- regiones conservadas;
- variantes;
- dominios;
- posibles funciones;
- y correspondencias entre genes o proteínas.

Además, cuando una secuencia es desconocida, una estrategia habitual consiste en compararla con grandes bases de datos para localizar secuencias parecidas.

Ese es precisamente el objetivo de herramientas como **BLAST**.

---

# 5.1. Alineamiento local y global

## 5.1.1. Qué es un alineamiento

Un alineamiento coloca dos secuencias de forma que podamos establecer correspondencias entre sus posiciones.

Ejemplo:

```text
Secuencia 1: ATGCTAGC
             |||| ||||
Secuencia 2: ATGC-TAGC
```

El alineamiento puede mostrar:

- coincidencias;
- sustituciones;
- inserciones;
- deleciones.

El objetivo no es simplemente hacer que las secuencias “se parezcan” visualmente.

El objetivo es encontrar una disposición coherente de acuerdo con un sistema de puntuación.

---

## 5.1.2. ¿Por qué necesitamos alinear?

Consideremos:

```text
Secuencia 1: ATGCGTAC
Secuencia 2: GCGT
```

Si las comparamos directamente desde el primer carácter, parecerían muy diferentes.

Sin embargo, la segunda secuencia está contenida dentro de la primera:

```text
ATGCGTAC
  GCGT
```

El alineamiento permite detectar esta relación.

Por tanto, antes de interpretar similitud o identidad debemos decidir **qué partes de las secuencias estamos comparando**.

---

## 5.1.3. Alineamiento global

El **alineamiento global** intenta alinear las secuencias a lo largo de toda su longitud.

Es especialmente adecuado cuando:

- las secuencias tienen una longitud parecida;
- se espera que estén relacionadas en toda su extensión;
- y queremos comparar globalmente dos secuencias.

Ejemplo conceptual:

```text
Secuencia 1: ATGCTAGCT
             |||| ||||
Secuencia 2: ATGC-AGCT
```

Aquí se intenta explicar toda la secuencia mediante el alineamiento.

---

## 5.1.4. Cuándo utilizar un alineamiento global

Puede ser útil para comparar:

- genes ortólogos;
- proteínas muy relacionadas;
- secuencias completas de longitud similar;
- dos versiones de una misma secuencia;
- variantes de una secuencia de referencia.

La pregunta que responde es aproximadamente:

> **¿Cómo se corresponden estas dos secuencias completas?**

---

## 5.1.5. Needleman-Wunsch

El algoritmo clásico asociado al alineamiento global es **Needleman-Wunsch**.

No es necesario implementar el algoritmo en este curso, pero sí comprender su idea general.

El procedimiento construye sistemáticamente posibles correspondencias entre las secuencias y utiliza:

- puntuaciones de coincidencia;
- penalizaciones por sustituciones;
- penalizaciones por gaps.

El objetivo es obtener un alineamiento óptimo según el sistema de puntuación elegido.

Este tipo de estrategia utiliza **programación dinámica**.

La programación dinámica permite dividir un problema grande en problemas más pequeños y reutilizar resultados parciales.

---

## 5.1.6. Alineamiento local

El **alineamiento local** busca las regiones más similares entre dos secuencias.

No obliga a alinear la totalidad de ambas.

Ejemplo:

```text
Secuencia 1: AATTGCGTACGGTA
                 ||||||
Secuencia 2:     GCGTAC
```

En este caso nos interesa detectar una región concreta compartida.

---

## 5.1.7. Cuándo utilizar un alineamiento local

Es especialmente útil cuando:

- las secuencias tienen longitudes muy diferentes;
- solo comparten una región;
- existe un dominio conservado;
- una proteína contiene un fragmento relacionado con otra;
- buscamos una secuencia corta dentro de otra más larga.

La pregunta sería aproximadamente:

> **¿Existe alguna región especialmente parecida entre estas secuencias?**

---

## 5.1.8. Smith-Waterman

El algoritmo clásico asociado al alineamiento local es **Smith-Waterman**.

También utiliza programación dinámica.

A diferencia del alineamiento global, no necesita continuar el alineamiento si la puntuación empeora demasiado.

Así puede localizar regiones de alta similitud dentro de secuencias más largas.

---

## 5.1.9. Global frente a local

| Característica | Global | Local |
|---|---|---|
| Compara toda la secuencia | Sí | No necesariamente |
| Busca regiones concretas | No es su objetivo principal | Sí |
| Adecuado para longitudes similares | Sí | Puede usarse con longitudes distintas |
| Algoritmo clásico | Needleman-Wunsch | Smith-Waterman |
| Uso habitual | Secuencias completas relacionadas | Dominios, fragmentos, regiones conservadas |

No existe un método universalmente mejor.

La elección depende de la pregunta biológica.

---

# 5.2. BLAST

## 5.2.1. El problema de buscar en una base de datos

Supongamos que tenemos una secuencia desconocida:

```text
ATGCGTAC...
```

y queremos averiguar qué puede ser.

Una estrategia sería compararla con todas las secuencias almacenadas en una base de datos.

Pero las bases de datos contienen millones de registros.

Aplicar un alineamiento exhaustivo contra todos ellos sería costoso.

Necesitamos un método rápido.

---

## 5.2.2. Qué es BLAST

**BLAST** significa:

**Basic Local Alignment Search Tool**

Es una herramienta diseñada para buscar regiones de similitud local entre una secuencia consulta y secuencias almacenadas en bases de datos.

Su objetivo principal es:

> **encontrar rápidamente secuencias parecidas a una secuencia de consulta**

---

## 5.2.3. Secuencia query y secuencias subject

En una búsqueda BLAST se distingue entre:

### Query

La secuencia que queremos analizar.

### Subject

Cada una de las secuencias de la base de datos contra las que se compara la query.

Conceptualmente:

```text
query → búsqueda → base de datos → resultados
```

---

## 5.2.4. BLAST como método heurístico

BLAST no intenta realizar un alineamiento exhaustivo completo contra todas las secuencias de la base de datos.

Utiliza una estrategia **heurística**.

La idea general es:

1. detectar pequeñas coincidencias prometedoras;
2. extender esas coincidencias;
3. conservar los alineamientos con puntuaciones suficientemente buenas.

Esto reduce enormemente el tiempo de cálculo.

La ventaja es la velocidad.

La consecuencia es que no garantiza explorar todas las posibilidades de la misma forma que un método exacto.

---

## 5.2.5. Idea conceptual del funcionamiento

Sin entrar en detalles matemáticos, BLAST puede entenderse como un proceso de tres fases:

### 1. Buscar pequeñas coincidencias

La query se divide conceptualmente en fragmentos.

BLAST identifica fragmentos similares en las secuencias de la base de datos.

### 2. Extender

Cuando encuentra una coincidencia prometedora, intenta extender el alineamiento hacia ambos lados.

### 3. Evaluar

Los alineamientos obtenidos se puntúan y se ordenan.

Los mejores aparecen en los primeros resultados.

---

## 5.2.6. Tipos principales de BLAST

La elección depende del tipo de secuencia de partida y del tipo de base de datos.

### BLASTn

Compara una secuencia de nucleótidos contra una base de datos de nucleótidos.

```text
ADN/ARN → ADN/ARN
```

### BLASTp

Compara una secuencia de proteína contra una base de datos de proteínas.

```text
proteína → proteína
```

### BLASTx

Traduce conceptualmente una secuencia de nucleótidos en los posibles marcos de lectura y la compara con proteínas.

```text
nucleótidos → proteínas
```

### tBLASTn

Compara una proteína contra una base de datos de nucleótidos traducidos.

```text
proteína → nucleótidos traducidos
```

### tBLASTx

Compara traducciones posibles de secuencias de nucleótidos.

Es computacionalmente más costoso y se utiliza en situaciones más específicas.

---

## 5.2.7. Elegir el tipo de BLAST

La elección debe responder a la pregunta:

> **¿Qué tengo y qué estoy buscando?**

Ejemplos:

Si tenemos una secuencia de ADN y queremos encontrar secuencias nucleotídicas parecidas:

**BLASTn**

Si tenemos una proteína y queremos buscar proteínas relacionadas:

**BLASTp**

Si tenemos ADN pero queremos detectar posibles proteínas relacionadas:

**BLASTx**

---

## 5.2.8. La base de datos importa

El resultado depende también de la base de datos seleccionada.

Podemos buscar:

- contra todas las secuencias disponibles;
- contra un organismo;
- contra proteínas revisadas;
- contra una colección específica.

Por tanto, una búsqueda BLAST no está definida únicamente por la query.

También depende de:

- base de datos;
- filtros;
- parámetros;
- versión del recurso.

Esto es importante para la reproducibilidad.

---

# 5.3. Evaluación de resultados y métricas

## 5.3.1. No basta con mirar el primer resultado

Una búsqueda BLAST devuelve una lista de coincidencias.

El primer resultado suele ser relevante, pero no debemos asumir automáticamente que es “la respuesta”.

Debemos interpretar varias métricas.

Entre las más importantes:

- porcentaje de identidad;
- cobertura;
- puntuación;
- E-value.

---

## 5.3.2. Porcentaje de identidad

Indica qué proporción de posiciones alineadas son exactamente iguales.

Ejemplo:

```text
Identidad: 95 %
```

Esto significa que, dentro de la región alineada, el 95 % de las posiciones son idénticas.

Pero hay una pregunta adicional:

> **¿Qué proporción de la secuencia total está alineada?**

Por eso necesitamos la cobertura.

---

## 5.3.3. Cobertura

La **cobertura** indica qué parte de la secuencia está incluida en el alineamiento.

Ejemplo conceptual:

Resultado A:

```text
Identidad: 99 %
Cobertura: 10 %
```

Resultado B:

```text
Identidad: 90 %
Cobertura: 95 %
```

No es evidente que el resultado A sea mejor.

Una identidad muy alta sobre una región muy corta puede ser menos informativa que una identidad algo menor sobre casi toda la secuencia.

---

## 5.3.4. Interpretar identidad y cobertura conjuntamente

Por ello, identidad y cobertura deben interpretarse juntas.

Podemos pensar:

**alta identidad + alta cobertura**

suele ser más informativo que:

**alta identidad + cobertura muy baja**

La interpretación final depende del contexto.

---

## 5.3.5. Score

BLAST asigna una puntuación al alineamiento.

La puntuación depende de:

- coincidencias;
- sustituciones;
- gaps;
- matriz de sustitución;
- parámetros utilizados.

Una puntuación mayor suele indicar un alineamiento más favorable.

Sin embargo, la puntuación depende de las condiciones de la búsqueda, por lo que no debe interpretarse aisladamente.

---

## 5.3.6. Bit score

BLAST también utiliza una puntuación normalizada denominada **bit score**.

Permite comparar con mayor facilidad resultados obtenidos bajo determinadas condiciones.

En general:

> **mayor bit score → alineamiento más fuerte**

---

## 5.3.7. E-value

El **E-value** es una de las métricas más importantes de BLAST.

Expresa, de forma simplificada, cuántos resultados de calidad similar podrían esperarse por azar en una búsqueda de ese tamaño.

Ejemplo:

```text
E-value = 10
```

indica que resultados similares podrían aparecer con bastante facilidad por azar.

En cambio:

```text
E-value = 1e-50
```

indica que sería extremadamente improbable obtener un resultado así por azar.

Por tanto:

> **cuanto menor es el E-value, más significativa suele ser la coincidencia**

---

## 5.3.8. E-value igual a 0

BLAST puede mostrar:

```text
E-value = 0.0
```

Esto no significa literalmente probabilidad cero.

Significa que el valor calculado es tan pequeño que se representa como cero con la precisión utilizada.

---

## 5.3.9. El tamaño de la base de datos influye

El E-value depende del tamaño del espacio de búsqueda.

Cuanto mayor es la base de datos, mayor es la posibilidad de encontrar coincidencias por azar.

Por ello, los valores estadísticos pueden cambiar si cambia la base de datos utilizada.

Este es otro motivo para registrar:

- base de datos;
- fecha;
- versión;
- parámetros.

---

## 5.3.10. Ejemplo comparativo

Imaginemos dos resultados BLAST:

### Resultado A

```text
Identidad: 98 %
Cobertura: 12 %
E-value: 2e-5
```

### Resultado B

```text
Identidad: 91 %
Cobertura: 96 %
E-value: 3e-80
```

Aunque A tiene mayor identidad, B puede ser mucho más convincente porque:

- cubre prácticamente toda la secuencia;
- presenta un E-value mucho menor.

Este ejemplo muestra por qué no debemos interpretar una sola métrica.

---

## 5.3.11. Longitud del alineamiento

También conviene observar cuántas posiciones se han alineado.

Un resultado puede mostrar una identidad muy elevada sobre diez aminoácidos.

Ese dato puede tener poca relevancia si la proteína tiene varios cientos de aminoácidos.

La longitud del alineamiento ayuda a poner la identidad en contexto.

---

## 5.3.12. Gaps

Los gaps también aportan información.

Un alineamiento con:

- muchos gaps;
- regiones fragmentadas;
- grandes interrupciones;

puede requerir una interpretación más cuidadosa.

No significa necesariamente que el resultado sea incorrecto, pero sí que la relación puede ser más compleja.

---

# 5.4. Cómo leer un resultado BLAST

Una estrategia sencilla consiste en revisar los resultados en este orden:

## 1. Descripción del resultado

¿Qué secuencia aparece?

¿De qué organismo procede?

## 2. Cobertura

¿Qué proporción de nuestra secuencia está alineada?

## 3. Identidad

¿Qué porcentaje de posiciones alineadas coincide exactamente?

## 4. E-value

¿La coincidencia parece compatible con el azar?

## 5. Longitud y gaps

¿El alineamiento es largo y coherente?

## 6. Contexto biológico

¿El resultado tiene sentido considerando el organismo, el tipo de secuencia y la pregunta de investigación?

---

# 5.5. Un flujo típico de búsqueda

Supongamos que obtenemos una secuencia desconocida.

Podríamos seguir:

```text
1. Determinar si es ADN o proteína
        ↓
2. Elegir el tipo de BLAST
        ↓
3. Elegir una base de datos
        ↓
4. Ejecutar la búsqueda
        ↓
5. Revisar los primeros resultados
        ↓
6. Comparar identidad, cobertura y E-value
        ↓
7. Examinar el alineamiento
        ↓
8. Consultar el registro asociado
        ↓
9. Interpretar biológicamente
```

BLAST es una herramienta de búsqueda.

No sustituye la interpretación.

---

# 5.6. Errores frecuentes

## Elegir el primer resultado sin analizarlo

El primer resultado puede ser adecuado, pero debe evaluarse.

## Fijarse únicamente en la identidad

Una identidad alta con cobertura baja puede ser engañosa.

## Interpretar el E-value como porcentaje de identidad

Son métricas completamente distintas.

## Considerar que E-value bajo demuestra función idéntica

Indica significación estadística de la coincidencia, no equivalencia funcional.

## No comprobar el organismo

Una secuencia muy parecida puede pertenecer a otra especie.

## Ignorar el tipo de base de datos

Los resultados dependen de dónde se busca.

## No registrar parámetros

Sin base de datos, fecha y parámetros, la búsqueda es difícil de reproducir.

---

# 5.7. Alineamiento y búsqueda no son exactamente lo mismo

Conviene distinguir:

### Alineamiento

Compara secuencias concretas y establece correspondencias entre ellas.

### Búsqueda

Intenta localizar, dentro de una base de datos, secuencias que puedan ser relevantes para nuestra query.

BLAST utiliza alineamientos locales como parte del proceso de búsqueda, pero su objetivo principal es encontrar candidatos relevantes de forma rápida.

---

# 5.8. Cuestiones guía

1. ¿Cuándo utilizarías un alineamiento global?
2. ¿Cuándo sería más adecuado un alineamiento local?
3. ¿Qué diferencia conceptual existe entre Needleman-Wunsch y Smith-Waterman?
4. ¿Por qué BLAST utiliza una estrategia heurística?
5. ¿Qué diferencia existe entre BLASTn y BLASTp?
6. ¿Qué significa que un resultado tenga 98 % de identidad pero 10 % de cobertura?
7. ¿Por qué un E-value pequeño suele ser preferible?
8. ¿Qué significa un E-value de 0.0?
9. ¿Por qué la base de datos utilizada afecta a los resultados?
10. ¿Por qué no debemos interpretar una única métrica de forma aislada?
11. ¿Qué información adicional revisarías antes de asignar una función a una secuencia?
12. ¿Por qué es importante registrar los parámetros de una búsqueda BLAST?

---

# Ideas clave

- El alineamiento establece correspondencias entre secuencias.
- El alineamiento global compara las secuencias completas.
- El alineamiento local busca regiones de similitud.
- Needleman-Wunsch es un algoritmo clásico de alineamiento global.
- Smith-Waterman es un algoritmo clásico de alineamiento local.
- BLAST busca rápidamente similitudes locales en grandes bases de datos.
- BLAST utiliza una estrategia heurística.
- Existen distintos tipos de BLAST según la naturaleza de la query y de la base de datos.
- Identidad y cobertura deben interpretarse conjuntamente.
- Un E-value pequeño indica que una coincidencia similar sería poco probable por azar.
- La interpretación de un resultado requiere considerar varias métricas y el contexto biológico.
- Una coincidencia computacional no implica automáticamente identidad funcional.

---

# Conexión con el siguiente tema

En este tema hemos aprendido a comparar secuencias y a buscar secuencias similares en bases de datos.

El siguiente paso consiste en comparar **más de dos secuencias simultáneamente** y utilizar esas comparaciones para estudiar relaciones evolutivas.

En el **Tema 6. Análisis filogenético asistido por ordenador** trabajaremos:

- alineamiento múltiple;
- construcción computacional de árboles;
- e interpretación de relaciones evolutivas.
