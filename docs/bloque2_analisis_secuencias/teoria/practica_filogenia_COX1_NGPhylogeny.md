# Práctica guiada: construcción de un árbol filogenético de COX1 con NGPhylogeny.fr

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

- Los **mismos archivos FASTA de COX1 utilizados en el último ejemplo de clase**. Descárgalos desde el material de la asignatura. **Pendiente de incorporar aquí el enlace directo a esos archivos**.
- Navegador web y acceso a [NGPhylogeny.fr](https://ngphylogeny.fr/).
- El árbol UPGMA del ejemplo anterior, para compararlo con el resultado de esta práctica.

> **Importante:** en esta versión de la guía no se indican especies ni resultados concretos porque todavía no se han incorporado los FASTA originales. No sustituyas las secuencias por otras: la comparación debe hacerse con los datos de clase.

## 3. Preparar las secuencias

1. Descarga los archivos FASTA de COX1 del ejemplo anterior.
2. Abre cada archivo con un editor de texto y observa su estructura: una cabecera que comienza por `>` y, debajo, la secuencia.
3. Reúne todas las secuencias en **un único archivo de texto** llamado `COX1_conjunto.fasta`. Conserva una cabecera distinta e identificable para cada especie.
4. Comprueba que no has copiado explicaciones, numeraciones ni otros caracteres ajenos a las secuencias.

**Comprobación:** ¿cuántas secuencias contiene el archivo? ¿Cómo se identifica cada especie?

## 4. Acceder a la herramienta

1. Abre [NGPhylogeny.fr](https://ngphylogeny.fr/).
2. Busca la modalidad **One Click** y el flujo que utilice **FastME**, si sigue disponible con ese nombre en la interfaz.
3. Antes de ejecutar, comprueba en la página qué programas y parámetros utiliza el flujo seleccionado. Los nombres y las opciones de la web pueden cambiar.

**Nota:** FastME es un método de inferencia filogenética basado en distancias, pero **no equivale a UPGMA**. No esperes obtener necesariamente el mismo árbol.

## 5. Ejecutar el análisis

1. Carga el archivo `COX1_conjunto.fasta` en el campo de entrada de secuencias.
2. Comprueba que la herramienta reconoce el tipo de secuencias adecuado (**nucleótidos**, si los FASTA de clase contienen ADN).
3. Revisa las opciones disponibles y, para esta primera ejecución, mantén los valores predeterminados del flujo, salvo que la herramienta solicite un dato obligatorio.
4. Inicia el análisis.
5. Espera a que termine. Si aparece un identificador o enlace al trabajo, consérvalo durante la sesión.

**Si se produce un error:** revisa que el archivo contiene varias secuencias FASTA, que todas son del mismo tipo y que las cabeceras son distintas. No interpretes un error de ejecución como un resultado biológico.

## 6. Examinar y guardar los resultados

En la página de resultados, identifica y descarga **cuando estén disponibles**:

- El **alineamiento múltiple**: observa las regiones conservadas y los huecos introducidos.
- El **árbol filogenético**: guarda su representación gráfica.
- El **árbol en formato Newick**: ábrelo con un editor de texto e identifica nombres, paréntesis y longitudes de rama si aparecen.
- La **matriz de distancias**, si el flujo permite descargarla.

No todos los flujos ni todas las versiones del servidor ofrecen los mismos archivos. Si algún resultado no aparece, anótalo en lugar de inventarlo.

## 7. Interpretar el árbol

Responde con ayuda del árbol obtenido:

1. ¿Qué dos especies aparecen agrupadas de forma más próxima? Indica qué parte del árbol respalda tu respuesta.
2. ¿Qué grupos o clados reconoces?
3. ¿El árbol incluye longitudes de rama? Si es así, ¿qué información aportan en este análisis?
4. ¿Puedes determinar cuál de las especies actuales es el antepasado de otra? Justifica la respuesta.
5. ¿Qué limitaciones tiene extraer conclusiones evolutivas utilizando un solo gen, COX1?

## 8. Comparación con el ejemplo UPGMA

Coloca juntos el árbol de esta práctica y el árbol UPGMA del ejemplo de clase.

1. ¿Coinciden las agrupaciones principales?
2. ¿Existen diferencias en la topología, es decir, en las relaciones de ramificación?
3. ¿Hay diferencias en la longitud de las ramas o en la posición de la raíz?
4. ¿Se pueden atribuir automáticamente las diferencias al método de construcción? **No**: también pueden intervenir el alineamiento, el tratamiento de posiciones ambiguas, el modelo de distancias y la configuración del análisis.
5. ¿Qué diferencia conceptual recuerdas entre UPGMA y un método como FastME? Investiga qué supuesto hace UPGMA sobre las tasas evolutivas.

> **Para interpretar correctamente:** un cambio en el orden visual de las puntas no significa necesariamente que haya cambiado la topología. Las ramas de un árbol pueden rotarse alrededor de un nodo sin modificar las relaciones representadas.

## 9. Entrega

Prepara un documento breve con:

- El número de secuencias y sus identificadores.
- Una captura del alineamiento o una descripción de lo observado.
- La imagen del árbol y, si está disponible, el archivo Newick.
- Las respuestas de los apartados 7 y 8.
- Una frase que indique el método y las opciones efectivamente utilizados según la página de resultados.

## 10. Recursos

- [NGPhylogeny.fr — herramienta online](https://ngphylogeny.fr/)
- [NGPhylogeny.fr — documentación](https://ngphylogeny.fr/documentation)
- [Formato Newick — descripción en PHYLIP](https://phylipweb.github.io/phylip/newicktree.html)

---


