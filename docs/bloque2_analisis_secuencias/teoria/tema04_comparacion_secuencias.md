# Tema 4. Fundamentos computacionales de la comparación de secuencias

## Duración

**1 hora de teoría**

Este tema abre el **Bloque II. Métodos computacionales para el análisis de secuencias**.

De acuerdo con la guía docente, se trabajan dos apartados:

- **4.1. Similitud, identidad y homología.**
- **4.2. Principios algorítmicos básicos.**

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar por qué la comparación de secuencias es una tarea central en Bioinformática.
- Diferenciar correctamente identidad, similitud y homología.
- Comprender qué significa alinear dos secuencias.
- Reconocer coincidencias, sustituciones e inserciones/deleciones.
- Comprender el papel de los sistemas de puntuación.
- Distinguir conceptualmente entre estrategias exactas y heurísticas.
- Interpretar un resultado computacional como evidencia que necesita contexto biológico.

# Introducción

Una de las preguntas más frecuentes en Bioinformática es aparentemente sencilla:

> **¿Se parecen estas dos secuencias?**

Responder correctamente no es tan trivial como parece.

Dos secuencias pueden parecerse porque pertenecen al mismo gen en especies diferentes, codifican proteínas relacionadas, comparten un dominio funcional, proceden de un ancestro común o simplemente contienen algunas regiones parecidas por azar.

Por ello, comparar secuencias no consiste únicamente en observarlas visualmente. Es necesario definir qué significa que dos posiciones coincidan, cómo se tratan las diferencias, qué regiones se comparan y cómo se cuantifica el resultado.

La comparación de secuencias constituye la base de muchas tareas posteriores: identificación de genes y proteínas, búsqueda en bases de datos, inferencia funcional, detección de variantes, alineamiento y análisis filogenético.

# 4.1. Similitud, identidad y homología

## 4.1.1. Comparar secuencias

Consideremos dos secuencias de ADN:

```text
Secuencia 1: ATGCTAGC
Secuencia 2: ATGTTAGC
```

A simple vista observamos que son muy parecidas.

Solo existe una diferencia:

```text
ATGCTAGC
ATGTTAGC
   ^
```

Pero para describir esa relación necesitamos utilizar términos precisos: **identidad**, **similitud** y **homología**.

## 4.1.2. Identidad

La **identidad** describe posiciones en las que dos secuencias presentan exactamente el mismo símbolo.

En ADN, una posición es idéntica cuando contiene el mismo nucleótido. En proteínas ocurre lo mismo: existe identidad cuando aparece exactamente el mismo aminoácido en la misma posición del alineamiento.

La identidad puede expresarse como porcentaje.

> **Porcentaje de identidad = proporción de posiciones exactamente iguales en el alineamiento.**

No basta con contar coincidencias: también debemos saber sobre qué longitud se está calculando.

Una identidad elevada no implica automáticamente que dos secuencias tengan exactamente la misma función. Es una medida descriptiva de la comparación.

## 4.1.3. Similitud

La **similitud** es un concepto más amplio.

En secuencias de proteínas, dos aminoácidos diferentes pueden considerarse similares si poseen propiedades físico-químicas parecidas. Una sustitución entre aminoácidos de tamaño, carga o comportamiento químico semejante puede afectar menos a la estructura o función de una proteína que una sustitución radical.

Por ello, una comparación de proteínas puede distinguir entre:

- aminoácidos idénticos;
- aminoácidos diferentes pero similares;
- aminoácidos claramente diferentes.

La similitud depende del criterio utilizado para valorar las sustituciones.

## 4.1.4. Homología

La **homología** tiene un significado diferente.

Dos secuencias son homólogas cuando comparten un **origen evolutivo común**.

La homología expresa una relación histórica. Conceptualmente:

> **dos secuencias son homólogas o no lo son**

Por ello, no es correcto hablar estrictamente de “70 % de homología”. Lo correcto sería indicar, por ejemplo, “70 % de identidad” y, a partir del conjunto de evidencias disponibles, considerar que las secuencias pueden ser homólogas.

La diferencia esencial es:

**Identidad** → describe lo que observamos al comparar secuencias.

**Homología** → describe una hipótesis sobre su historia evolutiva.

## 4.1.5. Ortólogos y parálogos

Dentro de las secuencias homólogas pueden distinguirse diferentes situaciones.

### Ortólogos

Son secuencias relacionadas por un proceso de especiación.

Por ejemplo, un mismo gen presente en humano y ratón puede tener genes ortólogos.

### Parálogos

Son secuencias relacionadas por un proceso de duplicación génica.

Una duplicación puede generar dos copias de un gen dentro de un genoma. Con el tiempo, ambas copias pueden divergir y adquirir funciones diferentes.

# 4.2. Principios algorítmicos básicos

## 4.2.1. El problema computacional

Para una persona es fácil comparar visualmente dos secuencias cortas:

```text
ATGCTA
ATGATA
```

Pero las secuencias reales pueden contener cientos, miles o millones de símbolos, y las bases de datos contienen millones de secuencias.

Por tanto, necesitamos algoritmos que automaticen la comparación.

## 4.2.2. Coincidencias y sustituciones

La estrategia más sencilla consiste en colocar dos secuencias una debajo de otra y recorrerlas posición a posición.

En cada posición podemos encontrar una coincidencia:

```text
A
A
```

o una sustitución:

```text
C
T
```

Esta estrategia funciona únicamente si ambas secuencias pueden compararse directamente en las mismas posiciones.

## 4.2.3. Inserciones, deleciones y gaps

Consideremos:

```text
Secuencia 1: ATGCTAGC
Secuencia 2: ATGCTTAGC
```

La segunda secuencia contiene un nucleótido adicional.

Si introducimos un espacio:

```text
ATGCT-AGC
ATGCTTAGC
```

observamos que las secuencias son mucho más parecidas.

Ese espacio se denomina **gap** y puede representar un acontecimiento de inserción o deleción. Estos eventos se denominan frecuentemente **indels**.

## 4.2.4. Qué es un alineamiento

Un **alineamiento** es una forma de disponer dos o más secuencias para establecer correspondencias entre sus posiciones.

El objetivo es representar de forma razonable:

- coincidencias;
- sustituciones;
- inserciones;
- deleciones.

La comparación de secuencias está, por tanto, estrechamente relacionada con el problema del alineamiento.

## 4.2.5. No existe una única forma de alinear

Dos secuencias pueden admitir distintos alineamientos posibles.

Un programa necesita decidir cuál representa mejor la relación entre ellas.

Para ello se utiliza un sistema de **puntuación**.

Conceptualmente podemos asignar:

- una recompensa a las coincidencias;
- una penalización a las sustituciones;
- una penalización a los gaps.

El algoritmo busca entonces un alineamiento con una puntuación favorable.

## 4.2.6. Matrices de sustitución

En proteínas no todas las sustituciones tienen el mismo significado.

Por ello, los algoritmos pueden utilizar **matrices de sustitución**.

Dos familias conocidas son:

- **PAM**
- **BLOSUM**

No es necesario memorizar sus valores. Lo importante es comprender que asignan puntuaciones diferentes según qué aminoácidos se sustituyan.

## 4.2.7. Penalización de gaps

Introducir un gap puede mejorar un alineamiento, pero no debería hacerse sin coste.

Si introducir espacios fuera gratuito, podríamos crear alineamientos artificialmente buenos añadiendo muchos gaps.

Por ello, los algoritmos aplican una penalización. Habitualmente se distingue entre:

- abrir un nuevo gap;
- prolongar uno ya existente.

## 4.2.8. El espacio de soluciones

A medida que aumenta la longitud de las secuencias, el número de alineamientos posibles crece enormemente.

El problema computacional consiste en encontrar una buena solución sin probar ingenuamente todas las combinaciones posibles.

Aquí aparece la importancia de los algoritmos.

## 4.2.9. Estrategias exactas y heurísticas

Las herramientas bioinformáticas pueden seguir estrategias diferentes.

### Métodos exactos

Buscan sistemáticamente una solución óptima de acuerdo con un determinado sistema de puntuación.

### Métodos heurísticos

Buscan soluciones muy buenas reduciendo considerablemente el número de posibilidades que deben evaluarse.

Son especialmente útiles cuando necesitamos comparar una secuencia contra bases de datos enormes.

BLAST, que estudiaremos en el siguiente tema, utiliza una estrategia heurística.

## 4.2.10. Precisión y coste computacional

Existe una idea general importante:

> **cuanto más exhaustiva es una búsqueda, mayor puede ser su coste computacional**

En Bioinformática es frecuente buscar un equilibrio entre:

- precisión;
- tiempo;
- memoria;
- tamaño de los datos.

La mejor estrategia depende del problema.

# 4.3. Del problema biológico al problema computacional

Cuando planteamos:

> ¿Está esta secuencia relacionada con otra?

un programa no puede responder directamente a esa pregunta biológica.

Primero la transforma en tareas computacionales:

1. representar las secuencias;
2. compararlas;
3. establecer correspondencias;
4. asignar puntuaciones;
5. seleccionar una solución;
6. calcular medidas;
7. devolver resultados.

Después corresponde al investigador interpretar esos resultados.

> **El algoritmo calcula; la interpretación biológica requiere contexto.**

# 4.4. Ejemplo integrado

Supongamos que disponemos de una secuencia desconocida y queremos saber si está relacionada con una secuencia conocida.

El proceso conceptual sería:

1. Obtener ambas secuencias.
2. Buscar una correspondencia entre ellas.
3. Identificar coincidencias, sustituciones y gaps.
4. Calcular una puntuación.
5. Obtener medidas como identidad o longitud del alineamiento.
6. Interpretar biológicamente el resultado.

# 4.5. Errores conceptuales frecuentes

## Hablar de “porcentaje de homología”

La homología no es un porcentaje. Debe hablarse de porcentaje de identidad o similitud.

## Considerar identidad y similitud como sinónimos

En proteínas, dos aminoácidos pueden ser diferentes pero similares en sus propiedades.

## Suponer que alta identidad implica automáticamente misma función

La identidad es una evidencia importante, pero la función debe interpretarse con información adicional.

## Comparar secuencias sin considerar inserciones o deleciones

Los gaps son necesarios para representar correctamente muchos cambios evolutivos.

## Interpretar el resultado de un algoritmo como una conclusión biológica definitiva

El resultado computacional necesita contexto y evaluación biológica.

# 4.6. Cuestiones guía

1. ¿Qué diferencia existe entre identidad y similitud?
2. ¿Por qué no es correcto hablar de “80 % de homología”?
3. ¿Qué información expresa realmente la homología?
4. ¿Qué diferencia existe entre ortólogos y parálogos?
5. ¿Por qué puede ser necesario introducir gaps al comparar secuencias?
6. ¿Por qué no todos los cambios de aminoácido deberían valorarse igual?
7. ¿Qué función cumple un sistema de puntuación?
8. ¿Por qué una búsqueda exhaustiva puede resultar costosa?
9. ¿Qué diferencia conceptual existe entre un método exacto y uno heurístico?
10. ¿Por qué el resultado de un algoritmo necesita interpretación biológica?

# Ideas clave

- Comparar secuencias es una tarea fundamental de la Bioinformática.
- La identidad mide coincidencias exactas.
- La similitud puede considerar sustituciones biológicamente compatibles.
- La homología describe un origen evolutivo común.
- La homología no se expresa como porcentaje.
- Un alineamiento establece correspondencias entre posiciones de las secuencias.
- Los gaps permiten representar inserciones y deleciones.
- Los algoritmos utilizan sistemas de puntuación para valorar alineamientos.
- Las matrices de sustitución ayudan a valorar cambios entre aminoácidos.
- Los métodos exactos y heurísticos responden a necesidades computacionales diferentes.
- El algoritmo produce un resultado computacional; la interpretación final es biológica.

# Conexión con el siguiente tema

En el **Tema 5. Búsqueda y alineamiento de secuencias** se estudiarán:

- alineamiento global;
- alineamiento local;
- BLAST;
- y las métricas utilizadas para interpretar los resultados.

Pasaremos así de comprender **qué significa comparar secuencias** a estudiar **cómo se realiza esa comparación con herramientas bioinformáticas**.
