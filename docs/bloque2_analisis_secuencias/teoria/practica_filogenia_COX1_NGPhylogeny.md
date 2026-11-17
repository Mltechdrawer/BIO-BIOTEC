# Práctica guiada: construcción de un árbol filogenético de COX1 con NGPhylogeny.fr o Phylogeny.fr

**Asignatura:** Bioinformática  
**Modalidad:** actividad guiada, sin programación  
**Objetivo:** construir e interpretar un árbol filogenético a partir de las secuencias COX1 del ejemplo trabajado previamente en clase.

## 1. Objetivos de aprendizaje

Al terminar la actividad podrás:

- Preparar secuencias biológicas en formato FASTA para un análisis filogenético.
- Ejecutar un flujo de alineamiento múltiple y reconstrucción de un árbol.
- Identificar qué resultados corresponden al alineamiento y cuáles a la inferencia filogenética.
- Interpretar agrupaciones de especies y contrastarlas con el árbol UPGMA estudiado en clase.
- Explicar por qué dos métodos filogenéticos pueden producir árboles diferentes.

## 2. Material necesario

- Los **mismos archivos FASTA de COX1 utilizados en el último ejemplo de clase**. 

Elegimos el gen mitocondrial ortólogo **COX1** (citocromo c oxidasa, subunidad I) en cinco primates. Se recuperó la región **secuencia codificante** (`CDS`, del inglés *Coding Sequence*) anotada de cada registro GenBank, no un intervalo arbitrario del genoma.

| Especie | Accesión NCBI | Coordenadas CDS (1-based, inclusivas) | Longitud |
|---|---|---|---:|
| Humano (*Homo sapiens*) | [NC_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_012920.1) | 5904–7445 | 1542 nt |
| Chimpancé (*Pan troglodytes*) | [NC_001643.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001643.1) | 5321–6862 | 1542 nt |
| Gorila (*Gorilla gorilla*) | [NC_001645.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001645.1) | 5325–6875 | 1551 nt |
| Orangután (*Pongo pygmaeus*) | [NC_001646.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_001646.1) | 5332–6882 | 1551 nt |
| Gibón (*Hylobates lar*) | [NC_002082.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_002082.1) | 5322–6863 | 1542 nt |

**Reproducibilidad: Visualización en navegador** los registros originales se conservan en
`genbank/`, las CDS extraídas en
<a href="../filogenetica/secuencias-cox1.txt" target="_blank" rel="noopener noreferrer">secuencias-cox1.fasta</a>
y los metadatos en
<a href="../filogenetica/validacion-cox1.txt" target="_blank" rel="noopener noreferrer">validacion-cox1.csv</a>.

**Reproducibilidad: Descargas en equipo** los registros originales se conservan en
`genbank/`, las CDS extraídas en
<a href="../filogenetica/secuencias-cox1.fasta" target="_blank" rel="noopener noreferrer">secuencias-cox1.fasta</a>
y los metadatos en
<a href="../filogenetica/validacion-cox1.csv" target="_blank" rel="noopener noreferrer">validacion-cox1.csv</a>.

- Navegador web y acceso a [NGPhylogeny.fr](https://ngphylogeny.fr/) o, como alternativa, a [Phylogeny.fr](https://phylogeny.fr/). Ambas se utilizan desde el navegador, sin instalar programas.
- El árbol UPGMA del ejemplo anterior, para compararlo con el resultado de esta práctica.

> **Importante:** utiliza las cinco secuencias COX1 indicadas en la tabla. No las sustituyas por otras: la comparación debe hacerse con los mismos datos de clase. Basta con realizar una de las dos rutas propuestas; no es obligatorio ejecutar ambas plataformas.

## 3. Preparar las secuencias

1. Descarga los archivos FASTA de COX1 del ejemplo anterior.
2. Abre cada archivo con un editor de texto y observa su estructura: una cabecera que comienza por `>` y, debajo, la secuencia.
3. Reúne todas las secuencias en **un único archivo de texto** llamado `COX1_conjunto.fasta`. Conserva una cabecera distinta e identificable para cada especie.
4. Comprueba que no has copiado explicaciones, numeraciones ni otros caracteres ajenos a las secuencias.

Si descargas `secuencias-cox1.fasta`, el archivo ya contiene las cinco secuencias reunidas: puedes utilizarlo directamente sin volver a unirlas.

**Comprobación:** ¿cuántas secuencias contiene el archivo? ¿Cómo se identifica cada especie?

## 4. Acceder a la herramienta

### Ruta A. NGPhylogeny.fr

1. Abre [NGPhylogeny.fr](https://ngphylogeny.fr/).
2. Busca la modalidad **One Click** y el flujo que utilice **FastME**, si sigue disponible con ese nombre en la interfaz.
3. Antes de ejecutar, comprueba en la página qué programas y parámetros utiliza el flujo seleccionado. Los nombres y las opciones de la web pueden cambiar.

**Nota:** FastME es un método de inferencia filogenética basado en distancias, pero **no equivale a UPGMA**. No esperes obtener necesariamente el mismo árbol.

### Ruta B. Phylogeny.fr como alternativa

1. Abre [Phylogeny.fr — One Click](https://phylogeny.fr/analysis/one-click).
2. Localiza el campo **Or paste sequences here** o la zona **Upload a FASTA file**.
3. En **Execution mode**, selecciona **Accurate**. Esta ruta utiliza **MAFFT → ClipKit → IQ-TREE** si se mantiene activada la depuración.
4. Mantén marcada **Use ClipKit to eliminate poorly aligned regions** para seguir la configuración comprobada con estas secuencias.

**Qué hace cada programa:** MAFFT alinea las secuencias; ClipKit elimina columnas que cumplen los criterios de depuración configurados; IQ-TREE infiere el árbol por máxima verosimilitud. La opción **Fast** utiliza FastTree en lugar de IQ-TREE; si la empleas, registra ese cambio en la entrega.

> **Los métodos cambian:** Phylogeny.fr permite completar los objetivos de esta práctica, pero su modo One Click no reproduce el flujo FastME de la ruta A. Debes comparar UPGMA con el método que realmente hayas ejecutado.

## 5. Ejecutar el análisis

### Ruta A. NGPhylogeny.fr

1. Carga el archivo `COX1_conjunto.fasta` en el campo de entrada de secuencias.
2. Comprueba que la herramienta reconoce el tipo de secuencias adecuado (**nucleótidos**, si los FASTA de clase contienen ADN).
3. Revisa las opciones disponibles y, para esta primera ejecución, mantén los valores predeterminados del flujo, salvo que la herramienta solicite un dato obligatorio.
4. Inicia el análisis.
5. Espera a que termine. Si aparece un identificador o enlace al trabajo, consérvalo durante la sesión.

### Ruta B. Phylogeny.fr

1. Sube `COX1_conjunto.fasta` o el archivo original `secuencias-cox1.fasta`. También puedes abrir la versión de visualización en navegador y copiar su contenido completo en **Or paste sequences here**: desde la primera cabecera `>` hasta el final de la quinta secuencia.
2. Revisa que están las cinco cabeceras y sus secuencias de ADN. No pulses **Example**, porque sustituiría los datos por un ejemplo de la plataforma.
3. Comprueba que has seleccionado **Accurate** y mantenido **ClipKit** activado. El correo electrónico es opcional; puedes dejarlo vacío.
4. Pulsa **Submit Analysis**.
5. Conserva la dirección de la página del trabajo. La página se actualiza automáticamente mientras se ejecutan los pasos.
6. Espera hasta ver **Analysis Complete**, el mensaje de finalización correcta y los tres pasos completados. Que termine solo el alineamiento no significa que haya terminado la inferencia del árbol.

**Comprobación realizada el 17 de noviembre de 2026:** el flujo MAFFT → ClipKit → IQ-TREE terminó correctamente con las cinco secuencias originales. El alineamiento depurado obtenido tenía **1.542 posiciones y ningún hueco**. Estos valores sirven como referencia de comprobación, no como sustituto de revisar los resultados de tu propia ejecución.

**Si se produce un error:** revisa que el archivo contiene varias secuencias FASTA, que todas son del mismo tipo y que las cabeceras son distintas. No interpretes un error de ejecución como un resultado biológico.

## 6. Examinar y guardar los resultados

En la página de resultados, identifica y descarga **cuando estén disponibles**:

- El **alineamiento múltiple**: observa las regiones conservadas y los huecos introducidos.
- El **árbol filogenético**: guarda su representación gráfica.
- El **árbol en formato Newick**: ábrelo con un editor de texto e identifica nombres, paréntesis y longitudes de rama si aparecen.
- La **matriz de distancias**, si el flujo permite descargarla.

No todos los flujos ni todas las versiones del servidor ofrecen los mismos archivos. Si algún resultado no aparece, anótalo en lugar de inventarlo.

### Localizar los resultados en Phylogeny.fr

- **Phylogenetic Tree:** examina el árbol interactivo. **Phylogram** representa las longitudes de rama; **Cladogram** muestra la topología. Usa **Export** para guardar una representación gráfica en alguno de los formatos ofrecidos.
- **Sequence Alignment:** alterna entre `alignment.aln` (alineamiento previo a la depuración) y `alignment_clean.aln` (alineamiento depurado utilizado para inferir el árbol). Anota el número de secuencias, las posiciones y la presencia de huecos.
- **Generated Files:** descarga `tree.nwk`, los dos alineamientos y los registros del análisis. **Download All** reúne los archivos en un ZIP.
- Revisa los registros para identificar el modelo seleccionado y los parámetros efectivos. En la ejecución de comprobación, IQ-TREE seleccionó `TPM2u+F+I` mediante BIC y realizó **5.000 réplicas de ultrafast bootstrap**. Registra lo que indique tu propio trabajo.

La ejecución comprobada no ofreció una matriz de distancias entre sus archivos generados: su ausencia no impide completar la actividad. Descarga los resultados durante la sesión; la página indica una fecha de eliminación del trabajo.

> **Atención a la raíz:** la documentación de One Click indica un enraizamiento por punto medio (*midpoint rooting*). Este procedimiento utiliza longitudes de rama y no equivale a designar el gibón como grupo externo. Registra cualquier cambio de raíz que hagas con **Reroot** o **Midpoint**; no atribuyas significado biológico al lugar de la raíz sin justificar el criterio utilizado.

## 7. Interpretar el árbol

Responde con ayuda del árbol obtenido:

1. ¿Qué dos especies aparecen agrupadas de forma más próxima? Indica qué parte del árbol respalda tu respuesta.
2. ¿Qué grupos o clados reconoces?
3. ¿El árbol incluye longitudes de rama? Si es así, ¿qué información aportan en este análisis?
4. ¿Puedes determinar cuál de las especies actuales es el antepasado de otra? Justifica la respuesta.
5. ¿Qué limitaciones tiene extraer conclusiones evolutivas utilizando un solo gen, COX1?
6. ¿Aparecen valores de soporte en los nodos? Si utilizaste IQ-TREE en modo Accurate, identifica los valores de ultrafast bootstrap disponibles. Explica por qué no representan el porcentaje de identidad entre secuencias ni la probabilidad directa de que un clado sea verdadero.

## 8. Comparación con el ejemplo UPGMA

Coloca juntos el árbol de esta práctica y el árbol UPGMA del ejemplo de clase.

1. ¿Coinciden las agrupaciones principales?
2. ¿Existen diferencias en la topología, es decir, en las relaciones de ramificación?
3. ¿Hay diferencias en la longitud de las ramas o en la posición de la raíz?
4. ¿Se pueden atribuir automáticamente las diferencias al método de construcción? **No**: también pueden intervenir el alineamiento, el tratamiento de posiciones ambiguas, el modelo evolutivo y la configuración del análisis.
5. Responde según la ruta utilizada:
   - **FastME en NGPhylogeny.fr:** ¿en qué se diferencia de UPGMA, aunque ambos sean métodos basados en distancias?
   - **IQ-TREE en Phylogeny.fr:** ¿qué diferencia hay entre agrupar a partir de una matriz de distancias con UPGMA y buscar un árbol por máxima verosimilitud bajo un modelo evolutivo?
   - **Otro método:** identifica el que realmente utilizaste y explica su diferencia respecto a UPGMA.
6. ¿Qué supuesto hace UPGMA sobre las tasas evolutivas? ¿Lo impone también el método elegido en tu ejecución?
7. ¿Cómo se ha establecido la raíz en cada árbol? Distingue las diferencias de enraizamiento de las diferencias en las agrupaciones del árbol sin raíz.

> **Para interpretar correctamente:** un cambio en el orden visual de las puntas no significa necesariamente que haya cambiado la topología. Las ramas de un árbol pueden rotarse alrededor de un nodo sin modificar las relaciones representadas.

## 9. Entrega

Prepara un documento breve con:

- El número de secuencias y sus identificadores.
- Una captura del alineamiento o una descripción de lo observado.
- La imagen del árbol y, si está disponible, el archivo Newick.
- Las respuestas de los apartados 7 y 8.
- La plataforma y el flujo utilizados, indicando programas, depuración del alineamiento, modelo evolutivo y soporte de ramas cuando esa información esté disponible.
- El criterio de enraizamiento y cualquier modificación realizada en el visor.
- El identificador o enlace del trabajo, además de los archivos descargados para conservar los resultados.

## 10. Recursos

- [NGPhylogeny.fr — herramienta online](https://ngphylogeny.fr/)
- [NGPhylogeny.fr — documentación](https://ngphylogeny.fr/documentation)
- [Phylogeny.fr — alternativa online](https://phylogeny.fr/)
- [Phylogeny.fr — One Click](https://phylogeny.fr/analysis/one-click)
- [Phylogeny.fr — documentación](https://phylogeny.fr/docs)
- [Formato Newick — descripción en PHYLIP](https://phylipweb.github.io/phylip/newicktree.html)

---


