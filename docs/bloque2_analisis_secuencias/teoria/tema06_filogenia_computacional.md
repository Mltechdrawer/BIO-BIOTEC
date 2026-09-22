# Tema 6. Análisis filogenético asistido por ordenador

## Duración

**2 horas de teoría**

Este tema cierra el **Bloque II. Métodos computacionales para el análisis de secuencias**.

De acuerdo con la guía docente, se estructura en tres apartados:

- **6.1. Alineamiento múltiple.**
- **6.2. Construcción computacional de árboles.**
- **6.3. Interpretación de relaciones evolutivas.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar qué es un alineamiento múltiple de secuencias.
- Comprender por qué el alineamiento múltiple es un paso previo habitual en análisis filogenéticos.
- Reconocer regiones conservadas y variables en un conjunto de secuencias.
- Comprender, a nivel conceptual, cómo se construyen árboles filogenéticos a partir de datos de secuencia.
- Diferenciar entre métodos basados en distancia y métodos basados en caracteres.
- Interpretar correctamente nodos, ramas, clados y topología.
- Comprender el significado de medidas de soporte como el bootstrap.
- Evitar errores frecuentes en la lectura de árboles filogenéticos.
- Relacionar los resultados computacionales con hipótesis evolutivas, sin interpretarlos como certezas absolutas.

---

# Introducción

En los temas anteriores hemos aprendido a comparar dos secuencias y a buscar secuencias similares en bases de datos.

El siguiente paso consiste en estudiar **más de dos secuencias simultáneamente**.

Cuando comparamos secuencias de distintas especies, genes o proteínas relacionadas, podemos plantearnos preguntas como:

- ¿qué posiciones se conservan?
- ¿qué regiones han cambiado?
- ¿qué secuencias son más parecidas entre sí?
- ¿qué grupos podrían compartir un ancestro común más reciente?
- ¿cómo podemos representar esas relaciones?

Estas preguntas nos llevan al análisis filogenético.

La filogenia intenta reconstruir relaciones evolutivas entre organismos, genes o proteínas.

En Bioinformática, estas relaciones se estudian frecuentemente a partir de secuencias mediante un proceso general:

```text
selección de secuencias
        ↓
alineamiento múltiple
        ↓
estimación de diferencias
        ↓
construcción del árbol
        ↓
evaluación del soporte
        ↓
interpretación biológica
```

El árbol filogenético es, por tanto, el resultado de una cadena de decisiones y análisis.

No debe interpretarse como una representación directa e infalible de la historia evolutiva.

---

# 6.1. Alineamiento múltiple

## 6.1.1. De dos secuencias a muchas secuencias

Un alineamiento por pares compara dos secuencias.

Un **alineamiento múltiple de secuencias** compara tres o más secuencias simultáneamente.

Por ejemplo:

```text
Seq1    ATGCTAGCTA
Seq2    ATGCTAGTTA
Seq3    ATG-TAGCTA
Seq4    ATGCTAGCAA
```

El objetivo es colocar posiciones potencialmente equivalentes en las mismas columnas.

Cada columna representa una hipótesis de correspondencia entre posiciones.

---

## 6.1.2. Qué podemos observar en un alineamiento múltiple

Un alineamiento múltiple permite identificar:

- posiciones conservadas;
- posiciones variables;
- sustituciones;
- inserciones y deleciones;
- regiones altamente conservadas;
- regiones más divergentes.

Ejemplo:

```text
Seq1    ATGCTAGCTA
Seq2    ATGCTAGTTA
Seq3    ATG-TAGCTA
Seq4    ATGCTAGCAA
        *** **** *
```

Las posiciones conservadas pueden indicar:

- restricciones funcionales;
- regiones estructurales importantes;
- sitios activos;
- motivos conservados;
- o simplemente una evolución más lenta.

---

## 6.1.3. Por qué el alineamiento múltiple es importante

El alineamiento múltiple se utiliza en:

- análisis filogenético;
- identificación de regiones conservadas;
- detección de motivos;
- comparación de familias de proteínas;
- anotación funcional;
- diseño de experimentos;
- estudio de evolución molecular.

En filogenia, el alineamiento es especialmente importante porque el árbol se construye a partir de las diferencias observadas entre posiciones que asumimos comparables.

---

## 6.1.4. Un alineamiento es una hipótesis

Es importante comprender que un alineamiento no es una verdad absoluta.

Cuando el programa coloca dos posiciones en la misma columna, está proponiendo que esas posiciones son comparables.

En secuencias muy similares, esta correspondencia suele ser clara.

En secuencias muy divergentes, puede haber varias soluciones posibles.

Por ello, la calidad del alineamiento afecta directamente al análisis posterior.

---

## 6.1.5. Estrategias de alineamiento múltiple

Comparar muchas secuencias simultáneamente es computacionalmente complejo.

Por ello, las herramientas utilizan estrategias aproximadas.

Una estrategia frecuente es el **alineamiento progresivo**.

La idea general es:

1. comparar las secuencias entre sí;
2. estimar cuáles son más parecidas;
3. alinear primero las más similares;
4. incorporar progresivamente el resto.

Herramientas como **Clustal Omega** utilizan este tipo de aproximaciones.

---

## 6.1.6. Influencia del orden de alineamiento

En estrategias progresivas, las decisiones tomadas al principio pueden influir en el resultado final.

Si una región queda mal alineada inicialmente, ese error puede propagarse.

Por ello, no debemos asumir que todo alineamiento generado automáticamente es necesariamente correcto.

Conviene revisar:

- zonas con muchos gaps;
- regiones muy variables;
- extremos de secuencias;
- secuencias mucho más largas o más cortas que el resto.

---

## 6.1.7. Secuencias adecuadas para comparar

Antes de realizar un alineamiento múltiple debemos comprobar que las secuencias sean comparables.

Por ejemplo:

- que representen el mismo gen o una familia relacionada;
- que correspondan a regiones homólogas;
- que tengan una longitud razonablemente compatible;
- que no mezclen fragmentos no equivalentes.

Mezclar secuencias no relacionadas puede producir un alineamiento artificial y un árbol sin interpretación biológica válida.

---

# 6.2. Construcción computacional de árboles

## 6.2.1. Qué es un árbol filogenético

Un árbol filogenético es una representación gráfica de hipótesis sobre relaciones evolutivas.

Ejemplo simplificado:

```text
        ┌── Especie A
    ┌───┤
    │   └── Especie B
────┤
    │   ┌── Especie C
    └───┤
        └── Especie D
```

El árbol indica que A y B aparecen agrupadas entre sí, y C y D forman otro grupo.

---

## 6.2.2. Partes de un árbol

### Hojas o terminales

Representan las secuencias u organismos analizados.

### Ramas

Representan conexiones entre nodos.

### Nodos internos

Representan puntos de divergencia e hipotéticos ancestros comunes.

### Clados

Un clado es un grupo formado por un ancestro común y todos sus descendientes.

### Raíz

La raíz representa el origen del árbol cuando el árbol está enraizado.

---

## 6.2.3. Topología

La **topología** describe el patrón de ramificación.

Por ejemplo:

```text
((A,B),(C,D))
```

expresa que A y B están agrupados, y C y D forman otro grupo.

La topología es uno de los elementos más importantes para interpretar relaciones.

---

## 6.2.4. Árboles enraizados y no enraizados

### Árbol enraizado

Tiene un punto de origen definido y permite interpretar una dirección evolutiva.

### Árbol no enraizado

Representa relaciones entre secuencias, pero no establece por sí mismo cuál es el ancestro común más antiguo.

Un árbol no enraizado puede mostrar agrupaciones sin indicar dirección temporal.

---

## 6.2.5. Uso de un grupo externo

Una forma habitual de enraizar un árbol es utilizar un **outgroup** o grupo externo.

El outgroup es una secuencia relacionada con las demás, pero claramente más distante.

Permite establecer una referencia externa para orientar el árbol.

La selección del outgroup debe tener sentido biológico.

---

## 6.2.6. De un alineamiento a una distancia

Una estrategia sencilla para construir árboles consiste en calcular diferencias entre secuencias.

Si dos secuencias presentan pocas diferencias, su distancia será pequeña.

Si presentan muchas diferencias, su distancia será mayor.

Podemos obtener una matriz conceptual como:

| | A | B | C | D |
|---|---:|---:|---:|---:|
| A | 0 | 2 | 8 | 9 |
| B | 2 | 0 | 7 | 8 |
| C | 8 | 7 | 0 | 3 |
| D | 9 | 8 | 3 | 0 |

Aquí A y B son más próximas, mientras que C y D forman otro grupo cercano.

---

## 6.2.7. Métodos basados en distancia

Estos métodos transforman las diferencias entre secuencias en una matriz de distancias.

Después utilizan esa matriz para construir el árbol.

Dos métodos conocidos son:

- **UPGMA**
- **Neighbor-Joining**

No es necesario implementar estos algoritmos en este curso.

Lo importante es comprender su lógica.

---

## 6.2.8. UPGMA

UPGMA agrupa progresivamente las secuencias más cercanas.

Es conceptualmente sencillo, pero supone que las secuencias evolucionan aproximadamente a una tasa constante.

Esa suposición no siempre es realista.

Por ello, su uso debe interpretarse con cautela.

---

## 6.2.9. Neighbor-Joining

Neighbor-Joining también utiliza distancias, pero no exige de la misma forma una tasa de evolución constante.

Es un método ampliamente utilizado para construir árboles de manera relativamente rápida.

---

## 6.2.10. Métodos basados en caracteres

Otros métodos utilizan directamente la información de cada posición del alineamiento.

Entre ellos se encuentran:

- máxima parsimonia;
- máxima verosimilitud;
- métodos bayesianos.

Estos métodos evalúan diferentes árboles posibles según criterios distintos.

---

## 6.2.11. Máxima parsimonia

La máxima parsimonia busca el árbol que requiere el menor número de cambios evolutivos.

La idea es intuitiva:

> **preferir la explicación que necesita menos cambios**

Sin embargo, la evolución real no siempre sigue el camino más simple.

---

## 6.2.12. Máxima verosimilitud

La máxima verosimilitud evalúa qué árbol hace más probable observar los datos del alineamiento bajo un determinado modelo de evolución.

Es más sofisticada que los métodos basados únicamente en distancia.

Puede ofrecer análisis más realistas, pero requiere más cálculo.

---

## 6.2.13. No existe un único árbol “automático”

El árbol obtenido depende de:

- secuencias seleccionadas;
- calidad del alineamiento;
- posiciones utilizadas;
- método de construcción;
- modelo evolutivo;
- parámetros;
- elección del outgroup.

Por tanto, diferentes decisiones pueden generar árboles diferentes.

---

# 6.3. Interpretación de relaciones evolutivas

## 6.3.1. Leer agrupaciones

Consideremos:

```text
        ┌── A
    ┌───┤
    │   └── B
────┤
    │   ┌── C
    └───┤
        └── D
```

A y B comparten un ancestro común más reciente entre sí que con C o D.

Del mismo modo, C y D forman otro grupo.

---

## 6.3.2. El orden vertical no importa

Los árboles pueden rotarse alrededor de un nodo sin cambiar su significado.

Por ejemplo:

```text
    A
           ─── nodo
     /
    B
```

y:

```text
    B
           ─── nodo
     /
    A
```

representan la misma relación.

Por ello, no debemos interpretar la posición “arriba” o “abajo” como más evolucionada o más antigua.

---

## 6.3.3. Las especies actuales no son ancestros unas de otras

Un error frecuente consiste en interpretar que una especie situada “antes” en el árbol es el ancestro de otra.

En general, las hojas representan organismos o secuencias actuales.

Dos especies actuales pueden compartir un ancestro común, pero una no tiene por qué ser el ancestro directo de la otra.

---

## 6.3.4. Longitud de las ramas

En algunos árboles, la longitud de las ramas contiene información.

Puede representar:

- cantidad de cambio;
- distancia genética;
- o tiempo, dependiendo del tipo de árbol.

Pero no todos los árboles utilizan la longitud de la misma forma.

Antes de interpretarla debemos comprobar qué representa.

---

## 6.3.5. Soporte de los nodos

Un árbol puede mostrar una determinada agrupación, pero necesitamos saber hasta qué punto está respaldada por los datos.

Una medida frecuente es el **bootstrap**.

---

## 6.3.6. Bootstrap

El bootstrap evalúa la estabilidad de las agrupaciones.

De forma conceptual:

1. se generan muchas versiones del alineamiento mediante remuestreo;
2. se construye un árbol para cada versión;
3. se observa cuántas veces aparece cada agrupación.

Un nodo puede mostrar, por ejemplo:

```text
95
```

Esto significa que esa agrupación apareció en aproximadamente el 95 % de las réplicas de bootstrap.

---

## 6.3.7. Qué significa un bootstrap alto

Un valor alto indica que esa agrupación es estable frente al remuestreo de los datos.

No significa:

- 95 % de probabilidad de que el árbol sea verdadero;
- 95 % de certeza evolutiva;
- ni que todo el árbol sea correcto.

Es una medida de soporte de una agrupación concreta.

---

## 6.3.8. Árbol de genes y árbol de especies

Otro punto importante es distinguir entre:

- árbol de un gen;
- árbol de una proteína;
- árbol de especies.

Un árbol construido a partir de un único gen refleja la historia de ese gen.

Esa historia puede no coincidir perfectamente con la historia de las especies.

Esto puede deberse a:

- duplicaciones;
- pérdidas génicas;
- transferencia horizontal;
- recombinación;
- tasas evolutivas diferentes.

---

## 6.3.9. Homología, ortología y paralogía en árboles

Los árboles ayudan a estudiar relaciones entre genes homólogos.

Una duplicación puede producir genes parálogos.

Una especiación puede producir genes ortólogos.

Sin embargo, para distinguir estas relaciones correctamente es necesario interpretar el árbol en su contexto.

No basta únicamente con observar qué secuencias aparecen juntas.

---

# 6.4. Flujo básico de análisis filogenético

Un análisis sencillo puede seguir:

```text
1. Seleccionar secuencias
        ↓
2. Verificar que son comparables
        ↓
3. Realizar alineamiento múltiple
        ↓
4. Revisar el alineamiento
        ↓
5. Elegir método de construcción
        ↓
6. Construir el árbol
        ↓
7. Evaluar soporte
        ↓
8. Interpretar agrupaciones
        ↓
9. Relacionar con el contexto biológico
```

Cada etapa puede influir en el resultado final.

---

# 6.5. Ejemplo conceptual

Supongamos que analizamos una misma proteína en cuatro especies:

```text
Humano
Ratón
Pez
Levadura
```

Después del alineamiento múltiple observamos que humano y ratón presentan muchas posiciones conservadas.

El pez presenta más diferencias.

La levadura es la secuencia más divergente.

El árbol podría mostrar:

```text
        ┌── Humano
    ┌───┤
    │   └── Ratón
────┤
    │   ┌── Pez
    └───┤
        └── Levadura
```

Esto sugeriría que humano y ratón presentan una relación más cercana para la secuencia analizada.

Pero no debemos concluir únicamente a partir de este esquema que hemos reconstruido toda la historia de las especies.

Estamos analizando una secuencia concreta.

---

# 6.6. Errores frecuentes

## Interpretar cercanía visual como cercanía evolutiva

Lo importante es la topología, no la distancia visual entre nombres.

## Pensar que una especie actual es ancestro de otra

Las hojas suelen representar linajes actuales.

## Ignorar la calidad del alineamiento

Un árbol construido sobre un mal alineamiento puede ser engañoso.

## Interpretar bootstrap como probabilidad de verdad

Es una medida de estabilidad o soporte, no una probabilidad absoluta.

## Confundir árbol de genes y árbol de especies

La historia de un gen puede diferir de la historia de los organismos.

## Pensar que existe un único árbol correcto generado automáticamente

El resultado depende del método y de las decisiones tomadas.

---

# 6.7. Cuestiones guía

1. ¿Qué diferencia existe entre alineamiento por pares y alineamiento múltiple?
2. ¿Por qué el alineamiento múltiple es importante antes de construir un árbol?
3. ¿Qué información puede aportar una región altamente conservada?
4. ¿Por qué un alineamiento debe considerarse una hipótesis?
5. ¿Qué diferencia existe entre un árbol enraizado y uno no enraizado?
6. ¿Qué función tiene un outgroup?
7. ¿Qué diferencia conceptual existe entre métodos de distancia y métodos basados en caracteres?
8. ¿Qué representa un nodo interno?
9. ¿Por qué el orden vertical de las hojas no tiene significado?
10. ¿Qué nos indica un valor de bootstrap?
11. ¿Por qué un árbol de un gen no tiene por qué coincidir exactamente con un árbol de especies?
12. ¿Qué factores pueden cambiar el árbol obtenido?

---

# Ideas clave

- El alineamiento múltiple compara tres o más secuencias simultáneamente.
- Cada columna del alineamiento representa una hipótesis de correspondencia.
- La calidad del alineamiento condiciona el análisis filogenético.
- Los árboles representan hipótesis sobre relaciones evolutivas.
- Los nodos internos representan ancestros comunes hipotéticos.
- La topología es más importante que la disposición visual.
- Los métodos de construcción pueden basarse en distancias o en caracteres.
- UPGMA y Neighbor-Joining son métodos basados en distancia.
- Máxima parsimonia y máxima verosimilitud utilizan enfoques diferentes.
- El bootstrap evalúa el soporte de agrupaciones concretas.
- Un árbol de genes no equivale necesariamente a un árbol de especies.
- La interpretación filogenética requiere combinar resultados computacionales y contexto biológico.

---

# Cierre del Bloque II

Este tema completa el **Bloque II. Métodos computacionales para el análisis de secuencias**.

A lo largo del bloque se ha seguido una progresión:

**Tema 4 → comprender qué significa comparar secuencias**

**Tema 5 → alinear y buscar secuencias similares**

**Tema 6 → comparar múltiples secuencias e interpretar relaciones evolutivas**

La lógica global puede resumirse así:

> **comparar → alinear → buscar → evaluar → agrupar → interpretar**

Estas competencias servirán de base para el Bloque III, donde el objetivo dejará de ser únicamente comparar secuencias y pasará a ser **extraer e integrar información funcional de genes y proteínas**.
