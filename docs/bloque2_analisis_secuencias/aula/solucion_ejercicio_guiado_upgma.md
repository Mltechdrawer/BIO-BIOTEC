# Actividad guiada: de tres secuencias de ADN a un árbol filogenético

> **Tema 6 · Análisis filogenético asistido por ordenador**  
> **Duración orientativa:** 40–45 minutos · **Modalidad:** individual o por parejas  
> **Material:** papel, lápiz y calculadora. **No es necesario programar.**

## ¿Qué aprenderás?

En esta actividad seguirás, paso a paso, el proceso de comparar tres secuencias de ADN, calcular sus distancias genéticas y construir un árbol sencillo mediante **UPGMA**. Los fragmentos son **ficticios** y se utilizan únicamente para aprender el procedimiento: **no representan datos reales de las especies**.

## Paso 1. Observar tres secuencias ya alineadas

Imaginemos que disponemos de un fragmento homólogo de ADN de tres especies de primates. Las secuencias ya están alineadas y todas tienen diez nucleótidos.

| Especie | Secuencia (posiciones 1 a 10) |
|---|---|
| Humano (H) | `ATGCCATGAA` |
| Chimpancé (C) | `ATGCCATGAG` |
| Gorila (G) | `ATGTCATGCG` |

**1.1.** ¿Cuántos nucleótidos tiene cada secuencia? **__________**

**1.2.** ¿Son idénticas las tres secuencias? **__________**

**1.3.** Antes de hacer los cálculos, ¿qué dos especies parecen más similares? **__________**

<details>
<summary>Pista: ¿qué significa que estén alineadas?</summary>
<p>Significa que las posiciones de las tres secuencias ya se han dispuesto para compararlas columna por columna. En este ejercicio no necesitamos introducir huecos (<em>gaps</em>).</p>
</details>

## Paso 2. Contar las diferencias entre parejas

Compara cada pareja **posición por posición**. Cuenta una diferencia cuando las letras de la misma columna sean distintas.

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Humano | A | T | G | C | C | A | T | G | A | A |
| Chimpancé | A | T | G | C | C | A | T | G | A | G |
| Gorila | A | T | G | T | C | A | T | G | C | G |

**2.1.** Humano–Chimpancé: posiciones diferentes **__________**; total **__________**.

**2.2.** Humano–Gorila: posiciones diferentes **__________**; total **__________**.

**2.3.** Chimpancé–Gorila: posiciones diferentes **__________**; total **__________**.

<details>
<summary>Pista: cómo contar una diferencia</summary>
<p>Compara las letras de una misma columna. Por ejemplo, en la posición 4, humano y chimpancé tienen C, mientras que gorila tiene T. Por tanto, esa posición es diferente en las comparaciones humano–gorila y chimpancé–gorila.</p>
</details>

## Paso 3. Calcular la distancia p

La **distancia p** es la proporción de posiciones comparables que presentan nucleótidos diferentes.

<p style="text-align: center; font-size: 1.1em;">
  p =
  <span style="display: inline-block; text-align: center; vertical-align: middle;">
    <span style="display: block; border-bottom: 1px solid; padding: 0 8px 4px;">Número de posiciones diferentes</span>
    <span style="display: block; padding: 4px 8px 0;">Número de posiciones comparables</span>
  </span>
</p>

Como todas las secuencias tienen diez posiciones alineadas y no hay huecos ni bases desconocidas, **dividiremos siempre entre 10**.

**3.1.** Humano–Chimpancé: **_____ / 10 = _____**

**3.2.** Humano–Gorila: **_____ / 10 = _____**

**3.3.** Chimpancé–Gorila: **_____ / 10 = _____**

<details>
<summary>Pista: un ejemplo de división</summary>
<p>Si dos secuencias de diez nucleótidos tuvieran dos posiciones diferentes, su distancia p sería 2/10 = 0,20. Una distancia menor indica menos diferencias observadas.</p>
</details>

## Paso 4. Completar la matriz de distancias

Traslada tus resultados a la tabla. La diagonal es cero porque una secuencia no difiere de sí misma; la matriz es **simétrica** porque la distancia entre H y C es igual a la distancia entre C y H.

| | Humano (H) | Chimpancé (C) | Gorila (G) |
|---|---:|---:|---:|
| **Humano (H)** | 0 | 0,10 | 0,30 |
| **Chimpancé (C)** | 0,10 | 0 | **_____** |
| **Gorila (G)** | 0,30 | **_____** | 0 |

**4.1.** ¿Cuál es la distancia más pequeña entre especies diferentes? **__________**

**4.2.** ¿Qué pareja de especies corresponde a esa distancia? **__________**

## Paso 5. Construir el árbol con UPGMA

UPGMA agrupa primero la pareja con **menor distancia**. Después calcula la distancia del nuevo grupo a las especies restantes.

### Primera agrupación: humano y chimpancé

**5.1.** Escribe el grupo que se forma: **(__________, __________)**.

La **altura** del nodo que une ambas especies es la mitad de su distancia:

**5.2.** Altura del primer nodo = **0,10 / 2 = __________**.

### Segunda agrupación: incorporar al gorila

Ahora tenemos dos grupos: **HC** (humano y chimpancé) y **G** (gorila). Para calcular su distancia, hacemos la media de las dos distancias originales al gorila:

<p style="text-align: center; font-size: 1.1em;">
  d(HC,G) =
  <span style="display: inline-block; text-align: center; vertical-align: middle;">
    <span style="display: block; border-bottom: 1px solid; padding: 0 8px 4px;">d(H,G) + d(C,G)</span>
    <span style="display: block; padding: 4px 8px 0;">2</span>
  </span>
</p>

**5.3.** Sustituye los valores: **(0,30 + _____) / 2 = __________**.

**5.4.** Altura del nodo final = **_____ / 2 = __________**.

**5.5.** Longitud de la rama que conecta el primer nodo con el segundo = **altura final − altura inicial = _____ − _____ = __________**.

<details>
<summary>Pista: altura del nodo y longitud de rama</summary>
<p>La altura de un nodo se mide desde las hojas hasta ese nodo. Para calcular la longitud de una rama interna, resta la altura del nodo hijo a la altura del nodo padre. No confundas la distancia entre grupos con la longitud de una sola rama.</p>
</details>

## Paso 6. Dibujar e interpretar el árbol

Completa el siguiente esquema indicando las especies en las hojas. El nodo que une humano y chimpancé debe quedar más próximo a sus hojas que el nodo final, que incorpora al gorila.

```text
                 ┌── __________________
          ┌──────┤
          │      └── __________________
    ──────┤
          └───────── __________________
```

**6.1.** ¿Qué dos especies comparten el ancestro común más reciente en este árbol? **__________**

**6.2.** ¿Significa el árbol que el humano desciende del chimpancé actual? **__________**. Explica brevemente: **________________________________**.

**6.3.** ¿Podemos afirmar que este árbol demuestra la historia evolutiva real de las tres especies? **__________**. ¿Por qué? **________________________________**.

<details>
<summary>Pista: cómo interpretar el árbol</summary>
<p>Un nodo interno representa un ancestro común <em>inferido</em>. Las especies actuales se sitúan en las hojas: ninguna de ellas tiene que ser antepasada de otra especie actual. Además, aquí usamos secuencias ficticias y un método con supuestos propios.</p>
</details>

## Soluciones para autocorrección

<details>
<summary>Soluciones completas</summary>
<p><strong>Paso 1.</strong> Las tres secuencias tienen 10 nucleótidos; no son idénticas. Humano y chimpancé parecen los más similares.</p>
<p><strong>Paso 2.</strong> Humano–chimpancé: 1 diferencia (posición 10). Humano–gorila: 3 diferencias (posiciones 4, 9 y 10). Chimpancé–gorila: 2 diferencias (posiciones 4 y 9).</p>
<p><strong>Paso 3.</strong> Distancias p: H–C = 1/10 = <strong>0,10</strong>; H–G = 3/10 = <strong>0,30</strong>; C–G = 2/10 = <strong>0,20</strong>.</p>
<p><strong>Paso 4.</strong> Las dos celdas pendientes contienen <strong>0,20</strong>. La menor distancia fuera de la diagonal es 0,10 (humano–chimpancé).</p>
<p><strong>Paso 5.</strong> Primera agrupación: (H,C), altura 0,10/2 = <strong>0,05</strong>. Distancia del grupo HC a G: (0,30 + 0,20)/2 = <strong>0,25</strong>. Altura final: 0,25/2 = <strong>0,125</strong>. Rama interna entre ambos nodos: 0,125 − 0,05 = <strong>0,075</strong>. Las ramas terminales H y C miden 0,05 cada una; la rama de G mide 0,125.</p>
<p><strong>Paso 6.</strong> Humano y chimpancé comparten el ancestro común más reciente según el árbol obtenido. El humano no desciende del chimpancé actual. El ejercicio es ilustrativo y no permite demostrar la filogenia real de estas especies.</p>
<p><strong>Árbol resuelto:</strong></p>
<pre>
                 ┌── Humano
          ┌──────┤
          │      └── Chimpancé
    ──────┤
          └───────── Gorila
</pre>
<p>El primer nodo agrupa humano y chimpancé (altura 0,05). El segundo incorpora al gorila (altura 0,125). El dibujo representa las relaciones de parentesco, pero las ramas no están a escala.</p>
<p><strong>Representación Newick opcional:</strong> <code>((Humano:0.05,Chimpance:0.05):0.075,Gorila:0.125);</code></p>
</details>

---

**Para seguir aprendiendo:** compara los pasos de este ejercicio con el ejemplo completo de cinco primates y el gen COX1. En aquel caso las secuencias son reales, más largas y necesitan un alineamiento previo.
