# Construcción de árboles filogenéticos: UPGMA y Neighbor-Joining

Paso de una matriz de distancias entre secuencias homólogas a un árbol, y por qué distintos algoritmos pueden producir resultados diferentes.

    Los valores de las matrices de este documento son **ficticios y didácticos**. No proceden del análisis COX1 de los cinco primates. 

## 1. De las secuencias a las distancias

Tras seleccionar secuencias homólogas y alinearlas, podemos medir sus diferencias. Una opción introductoria es la **distancia p**, la proporción de posiciones comparables que presentan nucleótidos diferentes:

<p style="text-align:center"><strong>Distancia p</strong> = número de posiciones diferentes / número de posiciones comparables</p>

La matriz resultante es simétrica y tiene ceros en la diagonal. **UPGMA** y **Neighbor-Joining (NJ)** parten de esa matriz, pero no siguen el mismo criterio para agrupar las especies.

## 2. UPGMA: agrupamiento jerárquico por distancias

**UPGMA** significa *Unweighted Pair Group Method with Arithmetic Mean* (método de agrupamiento por pares no ponderado con media aritmética).

El algoritmo identifica los dos grupos con menor distancia, los une, actualiza las distancias y repite el proceso hasta obtener un árbol **enraizado**. Supone que las distancias son compatibles con un **reloj molecular**: las ramas desde la raíz hasta las hojas tienen la misma longitud total (árbol ultramétrico).

### Ejemplo guiado

Usaremos cuatro especies y distancias ficticias, en unidades arbitrarias:

| | Humano | Chimpancé | Gorila | Orangután |
|---|---:|---:|---:|---:|
| **Humano** | 0 | 2 | 6 | 10 |
| **Chimpancé** | 2 | 0 | 6 | 10 |
| **Gorila** | 6 | 6 | 0 | 10 |
| **Orangután** | 10 | 10 | 10 | 0 |

**Primera iteración.** La menor distancia es 2, entre humano y chimpancé. Se forma el grupo **HC**. Su altura en el árbol es 2/2 = **1**. Las distancias actualizadas son:

- d(HC, Gorila) = (6 + 6) / 2 = **6**.
- d(HC, Orangután) = (10 + 10) / 2 = **10**.

**Segunda iteración.** Se agrupan **HC** y gorila, a distancia 6. La altura del nuevo nodo es 6/2 = **3**. La longitud de la rama desde HC hasta el nuevo nodo es 3 − 1 = **2**.

**Tercera iteración.** La distancia del grupo **HCG** al orangután es la media de las distancias entre todos los pares de sus miembros: (10 + 10 + 10)/3 = **10**. La altura de la raíz es 10/2 = **5**.

El árbol obtenido tiene la estructura **(((Humano, Chimpancé), Gorila), Orangután)**. Sus longitudes de rama quedan determinadas por las alturas de los nodos. En notación Newick:

```text
(((Humano:1,Chimpance:1):2,Gorila:3):2,Orangutan:5);
```

### Construcción progresiva del árbol

<a href="../upgma_interactivo/index.html"
   target="_blank"
   rel="noopener noreferrer">
   Explorar la construcción de UPGMA paso a paso
</a>

<details>
<summary>¿Por qué «no ponderado» no significa ignorar el tamaño de los grupos?</summary>
<p>UPGMA calcula la distancia entre dos grupos como la media de todas las distancias entre los elementos de uno y otro. Si un grupo contiene tres secuencias y otro una, se consideran las tres comparaciones. Al actualizar distancias a partir de grupos ya formados, se deben ponderar sus medias por el número de secuencias que contiene cada grupo.</p>
</details>

<details>
<summary>¿Cuál es la principal limitación biológica de UPGMA?</summary>
<p>UPGMA presupone una tasa de evolución aproximadamente constante entre linajes (reloj molecular). Cuando esta hipótesis no se cumple, puede agrupar incorrectamente linajes con velocidades evolutivas diferentes. Por eso es útil para aprender el procedimiento, pero no debe elegirse automáticamente para cualquier conjunto de datos.</p>
</details>

## 3. Neighbor-Joining: agrupación a partir de distancias corregidas

**Neighbor-Joining (NJ)** también construye un árbol a partir de una matriz de distancias, pero **no elige simplemente la pareja con menor distancia directa**. Evalúa las parejas teniendo en cuenta su distancia respecto al conjunto de taxones.

Para una matriz con **n** taxones, se calcula para cada taxón *i* la suma de sus distancias a los demás, *r(i)*. A continuación se calcula:

<p style="text-align:center"><strong>Q(i,j) = (n − 2) × d(i,j) − r(i) − r(j)</strong></p>

Se selecciona una pareja con el menor valor de **Q**, se crea un nodo común y se actualiza la matriz. Se repite hasta completar el árbol. El resultado habitual es un árbol **no enraizado**: NJ no determina por sí solo dónde se sitúa la raíz evolutiva.

### Ejemplo con la misma matriz

En nuestra matriz de cuatro especies:

| Taxón | Suma de distancias, r |
|---|---:|
| Humano | 18 |
| Chimpancé | 18 |
| Gorila | 22 |
| Orangután | 30 |

Como n = 4, tenemos (n − 2) = 2. Por ejemplo:

- Q(Humano, Chimpancé) = 2 × 2 − 18 − 18 = **−32**.
- Q(Humano, Gorila) = 2 × 6 − 18 − 22 = **−28**.
- Q(Gorila, Orangután) = 2 × 10 − 22 − 30 = **−32**.

Las parejas **Humano–Chimpancé** y **Gorila–Orangután** empatan en el mínimo. En una matriz de cuatro taxones esto es esperable: cada partición interna del árbol puede representarse escogiendo cualquiera de sus dos pares complementarios. Seleccionamos **Humano–Chimpancé**.

Las longitudes de las ramas desde el nuevo nodo **U** son:

<p style="text-align:center">L(H,U) = d(H,C)/2 + [r(H) − r(C)] / [2(n − 2)] = <strong>1</strong></p>
<p style="text-align:center">L(C,U) = d(H,C) − L(H,U) = <strong>1</strong></p>

Para un taxón restante *k*, la distancia actualizada es:

<p style="text-align:center">d(U,k) = [d(H,k) + d(C,k) − d(H,C)] / 2</p>

Por tanto, **d(U,Gorila) = 5** y **d(U,Orangután) = 9**. La distancia entre gorila y orangután sigue siendo **10**. Con los tres nodos restantes, las ramas que parten del nodo central tienen longitudes **2** (hacia U), **3** (hacia gorila) y **7** (hacia orangután). El árbol no enraizado presenta la partición **(Humano, Chimpancé) | (Gorila, Orangután)**.

### Construcción progresiva del árbol

<a href="../neighbor_joining_interactivo/index.html"
   target="_blank"
   rel="noopener noreferrer">
   Explorar Neighbor-Joining paso a paso
</a>


<details>
<summary>¿Por qué Neighbor-Joining no es simplemente «otro UPGMA»?</summary>
<p>UPGMA fusiona los grupos más próximos según la distancia disponible y produce un árbol enraizado ultramétrico. NJ utiliza la matriz Q para valorar qué pares son vecinos en el árbol, sin exigir que todos los linajes evolucionen a la misma velocidad. NJ tampoco proporciona una raíz evolutiva por sí mismo: para enraizar el árbol hace falta información o un criterio adicional, como un grupo externo apropiado.</p>
</details>

## 4. Comparación de ambos métodos

| Aspecto | UPGMA | Neighbor-Joining |
|---|---|---|
| Datos de entrada | Matriz de distancias | Matriz de distancias |
| Criterio de agrupación | Menor distancia entre grupos | Menor valor de la matriz Q |
| Tipo de árbol resultante | Enraizado | Habitualmente no enraizado |
| Reloj molecular | Lo presupone | No lo presupone |
| Valor didáctico | Muy fácil de seguir paso a paso | Introduce la corrección por distancias globales |

**Importante:** que dos métodos produzcan una topología parecida en un ejemplo no significa que sean equivalentes. Tampoco basta con un árbol de un solo gen para establecer definitivamente la historia evolutiva de las especies.

## 5. Para reflexionar

1. ¿Por qué necesitamos alinear las secuencias antes de calcular sus distancias?
2. ¿Qué cambia al utilizar la matriz Q de NJ en lugar de escoger directamente la menor distancia?
3. ¿Por qué un árbol de NJ necesita un criterio adicional para identificar la raíz?
4. ¿Qué problema puede introducir la hipótesis del reloj molecular de UPGMA?

## 6. Relación con nuestro ejemplo reproducible

El [ejemplo práctico con COX1 de cinco primates](filogenetica/index.md) documenta la selección y validación de secuencias reales, el alineamiento, la matriz de distancias y la construcción del árbol mediante UPGMA. Este documento explica los algoritmos con números pequeños para poder seguir las operaciones manualmente. **No debe confundirse la matriz didáctica de cuatro especies con la matriz real de COX1.**

## Referencias

- [Biopython: `Bio.Phylo.TreeConstruction`](https://biopython.org/docs/latest/api/Bio.Phylo.TreeConstruction.html).
- [MAFFT: documentación oficial](https://mafft.cbrc.jp/alignment/software/).
- [Clustal Omega: EMBL-EBI](https://www.ebi.ac.uk/jdispatcher/msa/clustalo).
