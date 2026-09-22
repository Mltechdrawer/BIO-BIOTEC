# Tema 8. Integración y explotación de información biológica

## Duración

**2 horas de teoría**

Este tema forma parte del **Bloque III. Análisis funcional y minería de datos biológicos**.

De acuerdo con la guía docente, se estructura en tres apartados:

- **8.1. Ontologías biológicas.**
- **8.2. Bases de conocimiento.**
- **8.3. Enriquecimiento funcional.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar por qué es necesario utilizar vocabularios controlados para integrar información biológica.
- Comprender qué es una ontología y cómo organiza conceptos y relaciones.
- Interpretar la estructura básica de Gene Ontology.
- Diferenciar entre una base de datos y una base de conocimiento.
- Reconocer el valor de las referencias cruzadas y los identificadores en la integración de información.
- Comprender el concepto de enriquecimiento funcional.
- Interpretar de forma básica una lista de términos o rutas enriquecidas.
- Reconocer limitaciones y posibles sesgos en los análisis de enriquecimiento.

---

# Introducción

En el Tema 7 hemos visto cómo podemos asignar información funcional a genes y proteínas.

Sin embargo, la Bioinformática moderna rara vez trabaja con una única entidad.

Es habitual analizar:

- cientos de genes;
- miles de proteínas;
- resultados de expresión;
- variantes;
- conjuntos de candidatos;
- redes de interacción.

Cuando la cantidad de información aumenta aparece un nuevo problema:

> **¿cómo integramos datos procedentes de recursos diferentes y los convertimos en conocimiento interpretable?**

Para ello necesitamos:

- identificadores;
- vocabularios controlados;
- ontologías;
- bases de conocimiento;
- métodos que permitan resumir grandes listas de genes o proteínas.

Este tema aborda precisamente ese paso: pasar de la anotación individual a la **integración y explotación de información biológica**.

---

# 8.1. Ontologías biológicas

## 8.1.1. El problema del lenguaje

Imaginemos que diferentes bases de datos describen una misma idea utilizando expresiones distintas:

```text
muerte celular programada
programmed cell death
apoptotic process
apoptosis
```

Para una persona estas expresiones pueden resultar relacionadas.

Para un sistema informático, son cadenas de texto diferentes.

Si queremos integrar información procedente de distintas fuentes necesitamos vocabularios compartidos.

---

## 8.1.2. Vocabulario controlado

Un **vocabulario controlado** utiliza un conjunto definido de términos.

En lugar de escribir libremente cualquier expresión, se seleccionan términos previamente establecidos.

Esto reduce:

- ambigüedad;
- sinónimos inconsistentes;
- errores de escritura;
- problemas de integración.

---

## 8.1.3. Qué es una ontología

Una ontología no es únicamente una lista de términos.

Además de definir conceptos, representa relaciones entre ellos.

Por ejemplo:

```text
proceso celular
    └── muerte celular
          └── proceso apoptótico
```

Los conceptos forman una estructura relacionada.

Esta organización permite:

- búsquedas más precisas;
- comparación entre registros;
- integración de fuentes;
- análisis computacional.

---

## 8.1.4. Identificadores estables

Los términos de una ontología suelen disponer de identificadores.

Esto evita depender exclusivamente del nombre textual.

Por ejemplo, un término puede cambiar de descripción manteniendo un identificador que permite rastrearlo.

Los identificadores facilitan la interoperabilidad.

---

## 8.1.5. Gene Ontology

**Gene Ontology (GO)** es una de las ontologías biológicas más utilizadas para describir funciones de genes y productos génicos.

Se organiza en tres grandes ramas:

### Molecular Function

Describe la actividad molecular.

Ejemplos conceptuales:

- actividad enzimática;
- unión a ADN;
- unión a ATP.

### Biological Process

Describe procesos biológicos en los que participa la entidad.

Ejemplos:

- división celular;
- reparación del ADN;
- metabolismo.

### Cellular Component

Describe localización o componente celular.

Ejemplos:

- núcleo;
- membrana;
- ribosoma.

Recurso: https://geneontology.org/

---

## 8.1.6. Relaciones jerárquicas

Los términos pueden presentar relaciones como:

- un concepto es un tipo de otro;
- un proceso forma parte de otro;
- una entidad se relaciona con una función.

Esto permite navegar desde conceptos generales hacia otros más específicos.

---

## 8.1.7. Una proteína puede tener muchas anotaciones

Una misma proteína puede asociarse simultáneamente con:

- varias funciones moleculares;
- varios procesos;
- diferentes localizaciones.

Por ello, la anotación funcional no suele reducirse a una sola etiqueta.

---

## 8.1.8. Evidencia en Gene Ontology

Las anotaciones GO pueden estar respaldadas por distintos tipos de evidencia.

Al interpretar un término GO conviene comprobar:

- si deriva de experimento;
- si ha sido inferido;
- si procede de análisis computacional;
- si ha sido revisado.

El término y la evidencia son informaciones diferentes.

---

# 8.2. Bases de conocimiento

## 8.2.1. Base de datos frente a base de conocimiento

Una **base de datos** almacena información estructurada.

Una **base de conocimiento** intenta además integrar y relacionar información para facilitar su interpretación.

En la práctica, la frontera puede no ser absoluta, pero conceptualmente podemos distinguir:

```text
base de datos
    → almacena registros

base de conocimiento
    → conecta registros, relaciones, evidencias y conocimiento biológico
```

---

## 8.2.2. Integración de múltiples fuentes

Una base de conocimiento puede combinar información sobre:

- genes;
- proteínas;
- funciones;
- enfermedades;
- rutas;
- estructuras;
- interacciones;
- publicaciones.

La integración permite pasar de una visión aislada a una visión conectada.

---

## 8.2.3. Identificadores y referencias cruzadas

La integración depende de poder reconocer que distintas fuentes hablan de la misma entidad.

Para ello son esenciales:

- identificadores;
- referencias cruzadas;
- correspondencias entre recursos.

Por ejemplo:

```text
NCBI Gene
    ↕
UniProt
    ↕
Gene Ontology
    ↕
Reactome
```

Este tipo de conexión ya se introdujo en el Bloque I y ahora se utiliza para extraer conocimiento funcional.

---

## 8.2.4. UniProt como recurso integrado

UniProt combina:

- secuencia;
- función;
- evidencias;
- dominios;
- localización;
- referencias;
- enlaces externos.

Por ello, puede funcionar como punto de entrada para acceder a distintas capas de información.

---

## 8.2.5. Reactome

**Reactome** es una base de conocimiento centrada en rutas y procesos biológicos.

Permite relacionar genes y proteínas con:

- reacciones;
- procesos;
- rutas;
- entidades moleculares.

Recurso: https://reactome.org/

---

## 8.2.6. InterPro y la integración de firmas

InterPro integra firmas procedentes de diferentes recursos para ofrecer una visión conjunta sobre:

- familias;
- dominios;
- regiones;
- sitios.

Este enfoque evita consultar de forma aislada múltiples recursos especializados.

---

## 8.2.7. Ventajas de integrar

La integración puede ayudar a:

- confirmar una anotación;
- descubrir relaciones;
- contextualizar genes;
- interpretar listas de candidatos;
- conectar secuencia y función;
- localizar evidencia complementaria.

---

## 8.2.8. Riesgos de la integración

Integrar información también puede propagar problemas.

Por ejemplo:

- anotaciones incorrectas;
- identificadores obsoletos;
- duplicados;
- diferencias entre versiones;
- inferencias automáticas no verificadas.

Por ello, más información no siempre significa mejor información.

---

# 8.3. Enriquecimiento funcional

## 8.3.1. Del gen individual a una lista

Supongamos que un experimento produce una lista de 200 genes.

Leer uno por uno sus registros sería poco eficiente.

Queremos saber si existen patrones comunes.

Podemos preguntar:

> **¿hay funciones o procesos representados con mayor frecuencia de la esperada?**

Este es el objetivo general del enriquecimiento funcional.

---

## 8.3.2. Idea básica

Imaginemos que en una lista de genes aparecen muchos genes relacionados con:

```text
respuesta inmunitaria
```

Si esa proporción es mucho mayor que la observada en el conjunto de referencia, podemos considerar que el término está enriquecido.

La comparación se realiza entre:

- **lista de interés**;
- **conjunto de referencia o background**.

---

## 8.3.3. Conjunto de referencia

La elección del conjunto de referencia es fundamental.

Puede ser:

- todo el genoma;
- todos los genes medidos;
- todas las proteínas detectadas;
- un conjunto experimental específico.

Un background inadecuado puede generar conclusiones engañosas.

---

## 8.3.4. Qué puede enriquecerse

Podemos estudiar enriquecimiento de:

- términos GO;
- rutas;
- familias;
- funciones;
- procesos;
- otras categorías biológicas.

---

## 8.3.5. Ejemplo conceptual

Supongamos:

```text
Lista analizada: 100 genes
Genes relacionados con ciclo celular: 30
```

Si en el conjunto de referencia solo una pequeña proporción de genes pertenece a esa categoría, el resultado puede indicar un enriquecimiento del proceso de ciclo celular.

El análisis intenta determinar si esa concentración podría explicarse fácilmente por azar.

---

## 8.3.6. Significación estadística

Las herramientas de enriquecimiento asignan medidas estadísticas a los resultados.

No es necesario desarrollar aquí el cálculo matemático, pero sí comprender que se compara:

> **lo observado frente a lo esperado**

Un término con un valor estadístico favorable indica que aparece más representado de lo esperado bajo el modelo utilizado.

---

## 8.3.7. Problema de las comparaciones múltiples

Un análisis puede evaluar cientos o miles de términos.

Si realizamos muchas pruebas, algunas pueden parecer significativas por azar.

Por ello se utilizan correcciones por comparaciones múltiples.

Es frecuente encontrar medidas como:

- p-value;
- p-value ajustado;
- FDR.

En este nivel del curso, lo importante es comprender que **un p-value sin corregir no debería interpretarse de forma aislada cuando se prueban muchas categorías**.

---

## 8.3.8. Redundancia de resultados

Las ontologías son jerárquicas.

Por ello, un análisis puede devolver términos muy relacionados.

Por ejemplo:

```text
respuesta al estrés
respuesta a estrés oxidativo
respuesta celular a estrés oxidativo
```

No necesariamente representan tres descubrimientos independientes.

La interpretación requiere agrupar y contextualizar términos.

---

## 8.3.9. Herramientas de enriquecimiento

Existen diferentes herramientas y recursos que permiten realizar estos análisis.

Entre ellos:

- Gene Ontology;
- Reactome;
- g:Profiler;
- Enrichr;
- herramientas integradas en plataformas de análisis.

La herramienta concreta puede variar, pero el razonamiento es común.

---

## 8.3.10. Interpretación responsable

Un resultado enriquecido no significa que:

- todos los genes de la lista participen en ese proceso;
- el proceso esté necesariamente activado;
- exista causalidad;
- el resultado sea biológicamente relevante sin contexto.

El enriquecimiento ayuda a generar y priorizar interpretaciones.

---

# 8.4. Flujo de integración y enriquecimiento

```text
lista de genes o proteínas
        ↓
normalización de identificadores
        ↓
anotaciones funcionales
        ↓
integración de recursos
        ↓
definición del background
        ↓
análisis de enriquecimiento
        ↓
corrección estadística
        ↓
interpretación biológica
```

---

# 8.5. Ejemplo integrado

Supongamos que un experimento identifica genes cuya expresión cambia después de aplicar un tratamiento.

Podemos:

1. normalizar los identificadores;
2. obtener términos GO;
3. consultar rutas en Reactome;
4. realizar un análisis de enriquecimiento;
5. identificar procesos sobrerrepresentados;
6. revisar los genes responsables del resultado;
7. contrastar la interpretación con la literatura.

Así pasamos de una lista extensa a una interpretación funcional organizada.

---

# 8.6. Errores frecuentes

## Mezclar identificadores sin normalizarlos

Puede provocar pérdidas o duplicados.

## Ignorar el conjunto de referencia

El resultado depende del background.

## Interpretar cada término como independiente

Las ontologías contienen relaciones jerárquicas.

## Utilizar solo el p-value

Debe considerarse la corrección por comparaciones múltiples.

## Confundir asociación con causalidad

Un término enriquecido no demuestra un mecanismo causal.

## No revisar los genes que originan el enriquecimiento

La interpretación debe volver a los datos originales.

---

# 8.7. Cuestiones guía

1. ¿Por qué un vocabulario libre dificulta la integración de datos?
2. ¿Qué diferencia existe entre un vocabulario controlado y una ontología?
3. ¿Cuáles son las tres ramas principales de Gene Ontology?
4. ¿Por qué los identificadores son importantes para integrar recursos?
5. ¿Qué diferencia conceptual existe entre una base de datos y una base de conocimiento?
6. ¿Qué tipo de información aporta Reactome?
7. ¿Qué pregunta intenta responder un análisis de enriquecimiento?
8. ¿Por qué es importante elegir correctamente el background?
9. ¿Por qué debemos corregir por comparaciones múltiples?
10. ¿Por qué los términos enriquecidos pueden ser redundantes?
11. ¿Qué significa que un proceso esté enriquecido?
12. ¿Qué limitaciones deben considerarse antes de formular una conclusión biológica?

---

# Ideas clave

- Las ontologías permiten representar conceptos y relaciones de forma computable.
- Gene Ontology organiza función molecular, proceso biológico y componente celular.
- Los identificadores y referencias cruzadas facilitan la integración.
- Las bases de conocimiento conectan entidades, evidencias y relaciones.
- Reactome permite contextualizar genes y proteínas en rutas.
- El enriquecimiento funcional resume patrones en listas de genes o proteínas.
- La elección del background condiciona el resultado.
- Las comparaciones múltiples deben corregirse.
- Un término enriquecido no implica causalidad.
- La interpretación debe volver siempre a los genes, evidencias y contexto biológico.

---

# Conexión con el siguiente tema

Hasta ahora hemos trabajado con herramientas bioinformáticas que organizan, integran y analizan información.

En el **Tema 9. Inteligencia artificial y automatización en Bioinformática** estudiaremos cómo automatizar tareas y cómo utilizar herramientas de IA como apoyo al análisis, manteniendo siempre:

- trazabilidad;
- reproducibilidad;
- verificación de resultados.
