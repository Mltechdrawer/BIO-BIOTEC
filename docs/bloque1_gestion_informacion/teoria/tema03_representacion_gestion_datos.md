# Tema 3. Representación y gestión de datos biológicos

## Planificación de la sesión

Este tema está previsto para **2 horas de teoría**, distribuidas entre la semana 3 y la semana 4.

La primera hora se centra principalmente en:

- 3.1. Formatos FASTA, GenBank y PDB.
- Introducción a la representación estructurada de datos biológicos.

La segunda hora se centra principalmente en:

- 3.2. Metadatos y anotación.
- 3.3. Calidad, interoperabilidad y reutilización de datos.

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar por qué los datos biológicos necesitan representaciones computacionales estandarizadas.
- Reconocer la estructura básica de los formatos FASTA, GenBank y PDB.
- Diferenciar entre dato biológico, metadato y anotación.
- Identificar qué información contextual es necesaria para interpretar correctamente un registro biológico.
- Comprender la importancia de la calidad, la interoperabilidad y la reutilización de datos.
- Relacionar formatos, metadatos, identificadores y anotaciones dentro de un flujo de trabajo bioinformático.
- Valorar la trazabilidad y la reproducibilidad como propiedades esenciales de la gestión de datos biológicos.

---

# Introducción

En el tema anterior se estudió dónde se almacena la información biológica y cómo se organiza dentro de bases de datos y recursos bioinformáticos.

El siguiente paso consiste en comprender **cómo se representa esa información para que pueda ser almacenada, intercambiada y procesada por herramientas computacionales**.

Una secuencia de ADN, una proteína o una estructura tridimensional pueden describirse de muchas formas. Sin embargo, para que diferentes programas, bases de datos y equipos de investigación puedan trabajar con los mismos datos es necesario utilizar convenciones comunes.

Estas convenciones se materializan en:

- formatos de archivo;
- campos estructurados;
- identificadores;
- metadatos;
- anotaciones;
- y reglas para describir la procedencia del dato.

En Bioinformática, representar correctamente la información es tan importante como analizarla.

Un análisis puede ser técnicamente correcto y, sin embargo, resultar difícil de reproducir si:

- el formato de entrada no está bien documentado;
- faltan metadatos;
- no se conoce la versión de los datos;
- las anotaciones son ambiguas;
- o no se conserva la procedencia de la información.

Por ello, este tema se centra en una idea fundamental:

> **Los datos biológicos necesitan una representación estructurada, contextualizada y trazable para poder ser interpretados y reutilizados.**

---

# 3.1. Formatos FASTA, GenBank y PDB

## 3.1.1. ¿Por qué existen formatos bioinformáticos?

Los ordenadores no interpretan directamente conceptos como "gen", "proteína" o "estructura molecular".

Para procesar estos elementos es necesario representarlos mediante estructuras de datos.

Un formato define:

- cómo comienza un registro;
- cómo se identifican sus campos;
- cómo se representa una secuencia;
- cómo se incorporan anotaciones;
- y cómo se distinguen diferentes tipos de información.

Los formatos permiten que diferentes herramientas puedan intercambiar datos.

Un mismo dato puede representarse de distintas formas según el objetivo.

Por ejemplo, una secuencia puede almacenarse:

- de forma muy simple, únicamente con un identificador y la secuencia;
- o en un registro más completo que incluya organismo, anotaciones, referencias y características funcionales.

La elección del formato depende de la tarea.

---

## 3.1.2. FASTA

FASTA es uno de los formatos más sencillos y utilizados en Bioinformática para representar secuencias.

Puede contener:

- secuencias de ADN;
- ARN;
- o proteínas.

Su estructura básica es:

```text
>identificador descripción
SECUENCIA
```

La primera línea comienza con el símbolo `>`.

Después aparece un identificador y, opcionalmente, una descripción.

Las líneas siguientes contienen la secuencia.

### Ejemplo

```text
>seq01 proteína hipotética
MKTLLVLAVAVSA...
```

El formato FASTA es deliberadamente simple.

No intenta almacenar toda la información sobre la entidad biológica.

Su objetivo principal es representar la secuencia de forma fácilmente procesable.

### Ventajas

- Es simple.
- Es legible por humanos.
- Es compatible con muchas herramientas.
- Es fácil de generar y procesar.
- Puede contener una o muchas secuencias.

### Limitaciones

FASTA tiene poca capacidad para representar información compleja.

Por ejemplo, no contiene de forma estructurada:

- anotaciones funcionales;
- posiciones de genes;
- referencias;
- taxonomía detallada;
- calidad;
- o características moleculares.

Por ello, suele utilizarse cuando el elemento principal de interés es la **secuencia**.

---

## 3.1.3. Identificadores en FASTA

La línea de cabecera puede contener distintos tipos de identificadores dependiendo del recurso del que proceda la secuencia.

Esto puede generar problemas si no se conserva la procedencia.

Por ejemplo:

```text
>ABC123
```

no permite saber por sí solo:

- qué base de datos generó el identificador;
- qué versión corresponde;
- qué organismo representa;
- o qué tipo de entidad contiene.

Por ello, cuando se trabaja con FASTA es recomendable conservar información adicional sobre el origen de la secuencia.

Una práctica adecuada consiste en registrar:

- recurso de origen;
- identificador;
- versión;
- fecha de descarga;
- organismo;
- y criterios utilizados para seleccionar la secuencia.

---

## 3.1.4. FASTA con múltiples secuencias

Un fichero FASTA puede contener varios registros.

Ejemplo:

```text
>seq01
ATGCGT...
>seq02
ATGACT...
>seq03
ATGAAA...
```

Este tipo de fichero es frecuente en:

- alineamientos;
- análisis comparativos;
- búsquedas de similitud;
- filogenia;
- y procesamiento masivo de secuencias.

La simplicidad del formato facilita su uso en flujos de trabajo automatizados.

---

## 3.1.5. GenBank

El formato GenBank contiene una representación mucho más rica que FASTA.

No almacena únicamente una secuencia.

También puede incluir:

- identificadores;
- descripción;
- organismo;
- taxonomía;
- referencias;
- características anotadas;
- genes;
- regiones codificantes;
- coordenadas;
- productos;
- y la secuencia.

Un registro GenBank puede interpretarse como una combinación de:

**secuencia + metadatos + anotaciones**

### Estructura general

Un registro suele incluir campos como:

```text
LOCUS
DEFINITION
ACCESSION
VERSION
SOURCE
ORGANISM
REFERENCE
FEATURES
ORIGIN
```

Cada campo tiene una función.

---

## 3.1.6. LOCUS, ACCESSION y VERSION

### LOCUS

Incluye información general sobre el registro, como:

- nombre;
- longitud;
- tipo de molécula;
- y otros atributos.

### ACCESSION

Contiene el número de acceso.

Es un identificador estable del registro.

### VERSION

Permite distinguir diferentes versiones de la secuencia.

Esta diferencia es importante.

El identificador puede mantenerse, mientras que la versión cambia cuando se modifica la secuencia.

Para reproducir un análisis resulta preferible registrar la versión concreta utilizada.

---

## 3.1.7. SOURCE y ORGANISM

Estos campos describen el origen biológico de la secuencia.

Pueden incluir:

- nombre científico;
- clasificación taxonómica;
- y otra información relacionada con el organismo.

Esta información es esencial.

Dos secuencias similares pueden pertenecer a especies diferentes y tener funciones distintas.

---

## 3.1.8. FEATURES

La sección `FEATURES` contiene anotaciones asociadas a posiciones concretas de la secuencia.

Puede representar:

- genes;
- regiones codificantes;
- exones;
- intrones;
- promotores;
- regiones reguladoras;
- o características moleculares.

Ejemplo conceptual:

```text
gene            100..900
CDS             150..850
```

Las coordenadas permiten relacionar información biológica con posiciones concretas.

A partir de esta sección es posible responder preguntas como:

- ¿dónde comienza un gen?
- ¿qué región codifica una proteína?
- ¿qué producto se asocia a una región?
- ¿qué anotaciones existen sobre una posición?

---

## 3.1.9. ORIGIN

La sección `ORIGIN` contiene la secuencia.

La información se presenta con numeración y organización por bloques.

A diferencia de FASTA, la secuencia aparece integrada dentro de un registro más amplio.

---

## 3.1.10. FASTA frente a GenBank

| Característica | FASTA | GenBank |
|---|---|---|
| Secuencia | Sí | Sí |
| Identificador | Sí | Sí |
| Descripción | Limitada | Sí |
| Organismo | No estructurado | Sí |
| Referencias | No | Sí |
| Anotaciones | No | Sí |
| Coordenadas | No | Sí |
| Procesamiento simple | Muy fácil | Más complejo |
| Uso típico | Análisis de secuencias | Registro anotado |

No existe un formato "mejor".

Cada uno responde a una necesidad diferente.

---

## 3.1.11. PDB

El formato PDB se utiliza para representar estructuras tridimensionales de macromoléculas.

A diferencia de FASTA o GenBank, el elemento principal no es una secuencia lineal, sino la posición de átomos en el espacio.

Un fichero PDB puede incluir:

- identificadores;
- información experimental;
- cadenas;
- residuos;
- átomos;
- coordenadas tridimensionales;
- ligandos;
- y otros elementos estructurales.

### Representación de coordenadas

Las líneas `ATOM` contienen información sobre átomos pertenecientes a macromoléculas.

Ejemplo simplificado:

```text
ATOM      1  N   MET A   1      11.104  13.207   9.245
```

Este tipo de línea codifica:

- número de átomo;
- nombre del átomo;
- residuo;
- cadena;
- posición del residuo;
- coordenadas X, Y, Z.

Estas coordenadas permiten reconstruir una estructura tridimensional.

---

## 3.1.12. Secuencia y estructura

FASTA representa principalmente una secuencia.

GenBank representa una secuencia acompañada de anotaciones.

PDB representa una estructura tridimensional.

Podemos resumirlo así:

**FASTA → secuencia**

**GenBank → secuencia + contexto + anotación**

**PDB → estructura tridimensional + información estructural**

Esta diferencia refleja que los formatos bioinformáticos se diseñan según el tipo de dato que necesitan representar.

---

# 3.2. Metadatos y anotación

## 3.2.1. Qué son los metadatos

Los **metadatos** son datos que describen otros datos.

En Bioinformática pueden indicar:

- organismo;
- tejido;
- muestra;
- método experimental;
- fecha;
- laboratorio;
- tecnología utilizada;
- versión;
- condiciones experimentales;
- o procedencia.

Una secuencia sin metadatos puede resultar difícil de interpretar.

Por ejemplo:

```text
ATGCGT...
```

es una secuencia.

Pero sin contexto no sabemos:

- de qué organismo procede;
- qué región representa;
- cómo se obtuvo;
- si corresponde a ADN genómico o ARN;
- ni qué experimento la generó.

Los metadatos aportan ese contexto.

---

## 3.2.2. Metadatos técnicos y biológicos

Podemos distinguir, de forma general, dos grandes categorías.

### Metadatos biológicos

Describen el contexto biológico.

Por ejemplo:

- organismo;
- tejido;
- tipo celular;
- estado fisiológico;
- condición experimental.

### Metadatos técnicos

Describen cómo se obtuvo o procesó el dato.

Por ejemplo:

- plataforma;
- software;
- versión;
- parámetros;
- fecha;
- protocolo.

Ambos tipos son necesarios para interpretar y reproducir un análisis.

---

## 3.2.3. Qué es una anotación

Una **anotación** añade significado biológico a un dato.

Puede consistir en:

- identificar un gen;
- asignar una función;
- marcar una región;
- asociar una proteína con un proceso;
- identificar un dominio;
- o relacionar una secuencia con una estructura.

La anotación transforma un dato aislado en información interpretada.

Por ejemplo:

```text
100..900
```

son coordenadas.

Pero:

```text
gene 100..900
```

es una anotación.

La anotación indica qué significa esa región.

---

## 3.2.4. Anotación manual y automática

### Anotación automática

Se genera mediante algoritmos.

Es necesaria cuando existen millones de registros.

Puede basarse en:

- similitud;
- reglas;
- modelos;
- perfiles;
- o predicciones.

### Anotación manual

Es revisada por expertos.

Puede incorporar:

- literatura científica;
- evidencia experimental;
- conocimiento del dominio;
- y evaluación crítica.

Ambos tipos de anotación pueden coexistir en un mismo recurso.

Por ello, al utilizar una anotación debemos comprobar:

> **¿cómo se ha generado?**

---

## 3.2.5. Evidencia asociada a las anotaciones

Una anotación no debería interpretarse de forma aislada.

Conviene conocer:

- si está basada en experimento;
- si se infiere por homología;
- si es automática;
- si ha sido revisada;
- o si deriva de una predicción.

Esta información determina el nivel de confianza.

En Bioinformática, una afirmación puede ser técnicamente correcta dentro de un registro y, sin embargo, estar asociada a un nivel de evidencia limitado.

---

## 3.2.6. La anotación como proceso dinámico

Las anotaciones cambian.

A medida que aparecen nuevos datos, una anotación puede:

- modificarse;
- ampliarse;
- corregirse;
- o reemplazarse.

Por ello es importante registrar:

- identificador;
- versión;
- fecha de consulta;
- y recurso.

---

# 3.3. Calidad, interoperabilidad y reutilización de datos

## 3.3.1. Calidad de los datos

La calidad no es una propiedad única.

Puede depender de:

- precisión;
- completitud;
- consistencia;
- procedencia;
- actualización;
- nivel de evidencia;
- documentación;
- y adecuación al uso.

Un dato puede ser correcto para una tarea y no ser adecuado para otra.

Por ejemplo, una secuencia parcial puede ser suficiente para identificar un organismo, pero insuficiente para estudiar una proteína completa.

Por ello, siempre debemos preguntar:

> **¿Es este dato adecuado para la pregunta que quiero responder?**

---

## 3.3.2. Procedencia

La **procedencia** describe de dónde viene el dato.

Debe permitir reconstruir:

- quién lo generó;
- dónde se obtuvo;
- cómo se procesó;
- qué transformaciones sufrió;
- y qué recurso lo proporciona.

La procedencia es esencial para la trazabilidad.

Sin ella, un resultado puede ser difícil de validar.

---

## 3.3.3. Interoperabilidad

La interoperabilidad es la capacidad de diferentes sistemas para intercambiar y utilizar datos de forma coherente.

En Bioinformática es especialmente importante porque una misma investigación puede combinar información de:

- NCBI;
- EMBL-EBI;
- UniProt;
- PDB;
- literatura;
- y herramientas de análisis.

La interoperabilidad depende de elementos como:

- formatos;
- identificadores;
- vocabularios;
- metadatos;
- referencias cruzadas;
- y estándares.

Sin interoperabilidad, cada recurso funcionaría como una isla.

---

## 3.3.4. El problema de los identificadores

Una misma entidad puede tener identificadores diferentes en recursos distintos.

Por ejemplo:

```text
gen → identificador NCBI
proteína → identificador UniProt
estructura → identificador PDB
```

Estos identificadores no son intercambiables.

La interoperabilidad requiere saber cómo relacionarlos.

Por ello, conservar referencias cruzadas es una parte esencial de la gestión de datos.

---

## 3.3.5. Reutilización

Un dato reutilizable debe poder ser:

- encontrado;
- interpretado;
- descargado;
- procesado;
- y relacionado con su contexto.

Para reutilizar un conjunto de datos necesitamos conocer:

- qué representa;
- cómo se obtuvo;
- qué formato utiliza;
- qué versión corresponde;
- qué licencia o condiciones de uso existen;
- y qué limitaciones presenta.

La reutilización permite responder nuevas preguntas sin repetir necesariamente el experimento original.

---

## 3.3.6. Principios FAIR

Un marco ampliamente utilizado para describir buenas prácticas de gestión de datos son los principios FAIR.

FAIR significa:

- **Findable**: localizables.
- **Accessible**: accesibles.
- **Interoperable**: interoperables.
- **Reusable**: reutilizables.

Estos principios no significan que todos los datos deban ser completamente abiertos.

Significan que deben estar gestionados de forma que puedan ser encontrados, comprendidos e integrados adecuadamente según sus condiciones de acceso.

### Findable

Los datos deben disponer de:

- identificadores;
- metadatos;
- mecanismos de búsqueda.

### Accessible

Debe existir una forma clara de recuperar los datos o conocer sus condiciones de acceso.

### Interoperable

Deben utilizar formatos y vocabularios que permitan integrarlos con otros recursos.

### Reusable

Deben incluir suficiente información sobre:

- procedencia;
- contexto;
- licencias;
- calidad;
- y condiciones de uso.

---

## 3.3.7. Trazabilidad y reproducibilidad

Un análisis bioinformático debería poder reconstruirse.

Para ello conviene registrar:

- fuente de datos;
- identificadores;
- versiones;
- fecha de descarga;
- formato;
- transformaciones;
- herramientas;
- parámetros.

Podemos resumir este principio así:

> **Un resultado reproducible necesita datos identificables y un proceso documentado.**

---

# 3.4. Un mismo dato, diferentes representaciones

Una misma entidad puede representarse de distintas maneras.

Supongamos una proteína.

Podemos tener:

- una secuencia FASTA;
- un registro UniProt;
- una secuencia codificante en GenBank;
- una estructura PDB;
- una publicación asociada.

Todos estos elementos se refieren a aspectos relacionados de la misma entidad, pero no contienen la misma información.

Por ello, un análisis bioinformático suele requerir combinar representaciones.

El reto consiste en mantener las relaciones entre ellas.

---

# 3.5. Ejemplo de flujo de gestión de datos

Supongamos que queremos estudiar una proteína.

### Paso 1. Recuperar el registro

Localizamos el identificador en UniProt.

### Paso 2. Descargar la secuencia

Exportamos la secuencia en FASTA.

### Paso 3. Conservar metadatos

Registramos:

- organismo;
- identificador;
- estado de revisión;
- fecha;
- versión.

### Paso 4. Analizar

Utilizamos la secuencia en una herramienta bioinformática.

### Paso 5. Consultar estructura

Relacionamos el registro con PDB.

### Paso 6. Documentar

Conservamos:

- identificadores;
- enlaces;
- parámetros;
- resultados.

De esta forma, la información puede reproducirse y reutilizarse.

---

# 3.6. Errores frecuentes

## Descargar datos sin conservar identificadores

Después puede ser difícil determinar su origen.

## Confundir formato con contenido

Dos ficheros pueden contener la misma secuencia pero diferentes metadatos.

## No registrar versiones

Una actualización puede modificar un resultado.

## Interpretar una anotación automática como evidencia experimental

El nivel de evidencia debe comprobarse.

## Eliminar metadatos durante una conversión

Convertir GenBank a FASTA simplifica la información, pero también elimina anotaciones y contexto.

## Mezclar identificadores de distintas entidades

Un gen, un transcrito, una proteína y una estructura representan niveles diferentes.

## Conservar únicamente el resultado final

Sin información sobre los datos y el procedimiento, el análisis puede no ser reproducible.

---

# 3.7. Cuestiones guía

1. ¿Qué información se pierde al convertir un registro GenBank a FASTA?
2. ¿Por qué FASTA sigue siendo tan utilizado a pesar de ser un formato muy simple?
3. ¿Qué diferencia existe entre metadato y anotación?
4. ¿Por qué una anotación debe ir acompañada de información sobre evidencia?
5. ¿Qué problemas puede causar utilizar un identificador sin indicar el recurso de origen?
6. ¿Por qué la interoperabilidad es esencial cuando se combinan varias bases de datos?
7. ¿Qué información mínima deberíamos conservar al descargar una secuencia?
8. ¿Cómo ayudan los principios FAIR a mejorar la reutilización de datos?
9. ¿Qué relación existe entre versión y reproducibilidad?
10. ¿Por qué un análisis puede ser correcto pero no reproducible?

---

# Ideas clave

- Los formatos permiten representar datos biológicos de forma procesable.
- FASTA representa principalmente secuencias.
- GenBank integra secuencia, metadatos y anotaciones.
- PDB representa información estructural tridimensional.
- Los metadatos describen el contexto del dato.
- Las anotaciones añaden significado biológico.
- El nivel de evidencia debe considerarse al interpretar una anotación.
- La calidad depende de la adecuación del dato a la pregunta.
- La interoperabilidad permite integrar información procedente de distintos recursos.
- La reutilización requiere procedencia, documentación y contexto.
- Los principios FAIR proporcionan un marco para mejorar la gestión de datos.
- La reproducibilidad exige conservar identificadores, versiones, formatos y transformaciones.

---

# Cierre del Bloque I

Este tema completa el Bloque I: **Gestión de información biológica y recursos bioinformáticos**.

A lo largo del bloque se ha seguido una progresión:

**Tema 1 → ecosistema bioinformático**

**Tema 2 → bases de datos y recuperación**

**Tema 3 → representación y gestión de datos**

La idea central puede resumirse mediante una cadena:

> **localizar → identificar → interpretar → representar → documentar → reutilizar**

Estas competencias serán necesarias en los siguientes bloques.

En el Bloque II comenzaremos a utilizar secuencias como objeto de análisis computacional y estudiaremos los fundamentos de la comparación de secuencias.

---

# Recursos de referencia

- NCBI: https://www.ncbi.nlm.nih.gov/
- EMBL-EBI: https://www.ebi.ac.uk/
- UniProt: https://www.uniprot.org/
- RCSB PDB: https://www.rcsb.org/

---

# Bibliografía del bloque

Según el proyecto docente, para el Bloque I se recomienda:

- Lesk, A. M. *Introduction to Bioinformatics*.
- Pevsner, J. *Bioinformatics and Functional Genomics*.
- Buffalo, V. *Bioinformatics Data Skills*.
- Zvelebil, M. J. y Baum, J. O. *Understanding Bioinformatics*.
