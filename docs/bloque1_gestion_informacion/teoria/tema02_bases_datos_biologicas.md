# Tema 2. Bases de datos biológicas y recuperación de información

## Planificación de la sesión

Este tema está previsto para **2 horas de teoría**, distribuidas en dos sesiones durante la semana 2.

La primera hora se centra en:

- 2.1. Bases de datos primarias y secundarias.
- 2.2. Arquitectura y organización de recursos biológicos.

La segunda hora se centra principalmente en:

- 2.3. NCBI, EMBL-EBI, UniProt y PDB.

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar por qué las bases de datos biológicas son una infraestructura esencial de la investigación actual.
- Diferenciar entre bases de datos primarias y secundarias.
- Comprender cómo se organiza la información dentro de un recurso bioinformático.
- Identificar el papel de los registros, identificadores, anotaciones y referencias cruzadas.
- Reconocer las funciones generales de NCBI, EMBL-EBI, UniProt y PDB.
- Seleccionar, de forma razonada, el recurso más adecuado para recuperar un determinado tipo de información biológica.
- Comprender que una búsqueda bioinformática requiere interpretar el contexto del dato y no únicamente localizar un resultado.

---

## Introducción

En el tema anterior se presentó la Bioinformática como una disciplina que permite trabajar de forma sistemática con grandes cantidades de información biológica. También se introdujo la idea de un **ecosistema digital biomolecular** en el que los datos generados por laboratorios de todo el mundo pueden almacenarse, organizarse, relacionarse y reutilizarse.

El siguiente paso consiste en comprender cómo funciona ese ecosistema desde el punto de vista de sus recursos de información.

Una parte importante del trabajo bioinformático comienza con preguntas aparentemente sencillas:

- ¿se conoce ya la secuencia de este gen?
- ¿qué proteína codifica?
- ¿qué función se le atribuye?
- ¿qué variantes se han descrito?
- ¿existe una estructura tridimensional?
- ¿qué publicaciones están asociadas?
- ¿qué información está experimentalmente comprobada y qué información ha sido predicha?
- ¿qué identificador debo utilizar para recuperar el mismo registro más adelante?

Responder correctamente requiere saber **dónde buscar**, pero también entender **qué tipo de información almacena cada recurso y cómo está organizada**.

Una base de datos biológica no es simplemente una colección de páginas web. Es un sistema estructurado en el que los datos se representan mediante registros, campos, relaciones, identificadores y procedimientos de actualización.

Por ello, aprender a utilizar recursos bioinformáticos implica desarrollar una forma de lectura diferente a la utilizada en una página web convencional. No buscamos únicamente texto: buscamos **datos estructurados, relaciones y evidencias**.

---

# 2.1. Bases de datos primarias y secundarias

## 2.1.1. ¿Qué es una base de datos biológica?

Una **base de datos biológica** es un recurso organizado que almacena información relacionada con entidades o procesos biológicos y permite recuperarla mediante consultas.

La información puede incluir, entre otros elementos:

- secuencias de ADN o ARN;
- secuencias de proteínas;
- genes;
- variantes;
- estructuras tridimensionales;
- funciones moleculares;
- interacciones;
- vías metabólicas;
- organismos;
- publicaciones;
- o anotaciones funcionales.

El elemento fundamental de una base de datos no es únicamente el dato, sino su **organización**.

Una secuencia aislada tiene un valor limitado. En cambio, una secuencia asociada a:

- un organismo;
- un gen;
- un método de obtención;
- un identificador;
- una publicación;
- una función;
- y referencias a otros recursos

se convierte en un registro mucho más informativo.

---

## 2.1.2. Datos primarios

Las **bases de datos primarias** almacenan datos biológicos que proceden directamente de experimentos, procesos de secuenciación o depósitos realizados por investigadores y centros de datos.

En este tipo de recursos, el dato depositado constituye la información fundamental.

Ejemplos de datos primarios pueden ser:

- una secuencia nucleotídica;
- una secuencia proteica;
- coordenadas experimentales de una estructura tridimensional;
- lecturas de secuenciación;
- o determinados conjuntos de datos experimentales.

Estas bases de datos suelen desempeñar una función de **archivo**.

El objetivo es conservar la información y hacerla accesible para que pueda utilizarse posteriormente.

### Características habituales

Las bases de datos primarias suelen presentar varias características:

- reciben datos procedentes de la comunidad científica;
- asignan identificadores a los registros;
- conservan diferentes versiones;
- almacenan metadatos;
- mantienen información sobre la procedencia;
- y permiten descargar los datos.

Esto no significa que toda la información contenida sea automáticamente correcta.

El hecho de que un dato esté depositado en una base de datos no elimina la necesidad de valorar:

- cómo se obtuvo;
- qué controles se realizaron;
- qué nivel de evidencia existe;
- o si el registro ha sido revisado posteriormente.

---

## 2.1.3. Datos secundarios

Las **bases de datos secundarias** contienen información derivada del análisis, integración, clasificación o anotación de datos existentes.

En lugar de limitarse a almacenar datos originales, añaden una capa de interpretación.

Pueden incluir:

- funciones asignadas;
- familias de proteínas;
- dominios;
- relaciones evolutivas;
- clasificaciones;
- anotaciones;
- o conexiones entre registros procedentes de distintas fuentes.

La frontera entre base de datos primaria y secundaria no siempre es absoluta.

Muchos recursos modernos integran ambos tipos de información.

Un mismo registro puede contener:

- datos originales;
- anotaciones automáticas;
- información revisada manualmente;
- enlaces a otras bases de datos;
- y resultados derivados de análisis computacionales.

Por tanto, la clasificación primaria/secundaria debe utilizarse como una **herramienta conceptual**, no como una división rígida.

---

## 2.1.4. Curación de datos

Un concepto importante al trabajar con bases de datos biológicas es la **curación**.

La curación consiste en revisar, organizar y mejorar la información almacenada.

Puede incluir:

- comprobación de consistencia;
- corrección de errores;
- incorporación de información procedente de literatura científica;
- establecimiento de relaciones entre registros;
- revisión de nomenclatura;
- o actualización de anotaciones.

La curación puede ser:

### Automática

Se realiza mediante procedimientos computacionales.

Es necesaria cuando el volumen de datos es muy grande.

### Manual

Intervienen expertos que revisan la evidencia disponible.

Es más costosa, pero puede aportar un nivel de calidad y contextualización difícil de conseguir exclusivamente mediante procesos automáticos.

En muchos recursos se combinan ambos procedimientos.

---

## 2.1.5. Datos experimentales y datos predichos

Otro aspecto esencial es distinguir entre:

- **información obtenida experimentalmente**;
- **información inferida o predicha computacionalmente**.

Esta distinción aparece continuamente en Bioinformática.

Por ejemplo, una función proteica puede haber sido:

- demostrada experimentalmente;
- inferida por similitud con otra proteína;
- asignada automáticamente;
- o predicha mediante un modelo computacional.

Del mismo modo, una estructura tridimensional puede proceder de un experimento o de una predicción computacional.

Dos registros pueden mostrar aparentemente el mismo tipo de información, pero su nivel de evidencia puede ser muy diferente.

Por ello, al recuperar información no basta con preguntar:

> **¿Qué dice la base de datos?**

También debemos preguntar:

> **¿De dónde procede esa información y qué evidencia la respalda?**

---

# 2.2. Arquitectura y organización de recursos biológicos

## 2.2.1. El registro como unidad de información

La mayor parte de las bases de datos biológicas organizan la información mediante **registros**.

Un registro representa una entidad determinada:

- un gen;
- una secuencia;
- una proteína;
- una estructura;
- una publicación;
- un organismo;
- o cualquier otro elemento relevante para el recurso.

Cada registro suele incluir distintos campos.

Por ejemplo:

**Identificador → nombre → organismo → descripción → secuencia → anotaciones → referencias**

La estructura exacta depende del recurso.

Comprender qué representa un registro es fundamental.

Un identificador de proteína no equivale necesariamente a un identificador de gen, y un identificador de secuencia no tiene por qué identificar una función biológica.

---

## 2.2.2. Identificadores

Los identificadores permiten localizar de manera inequívoca los registros.

Pueden aparecer como:

- números de acceso;
- códigos;
- identificadores persistentes;
- o identificadores internos de una base de datos.

Su función es evitar ambigüedades.

Los nombres biológicos pueden cambiar o presentar sinónimos. Los identificadores proporcionan una referencia más estable.

### Ejemplo conceptual

Una proteína puede aparecer con:

- un nombre completo;
- una abreviatura;
- varios sinónimos;
- el nombre del gen;
- y diferentes denominaciones históricas.

Sin un identificador, una búsqueda puede producir resultados ambiguos.

---

## 2.2.3. Versiones

Los datos biológicos cambian.

Una secuencia puede corregirse, una anotación puede actualizarse y un registro puede incorporar nueva evidencia.

Por ello, algunos sistemas utilizan **versiones**.

Una versión permite distinguir:

> el registro actual

de

> una representación anterior del mismo registro.

Esta cuestión es especialmente importante para la reproducibilidad.

Si un análisis se realizó utilizando una versión determinada de un conjunto de datos, una actualización posterior podría producir resultados diferentes.

---

## 2.2.4. Campos

Los registros se dividen en campos que describen distintos aspectos de la información.

Algunos campos habituales pueden contener:

- nombre;
- descripción;
- organismo;
- taxonomía;
- longitud;
- secuencia;
- función;
- referencias;
- anotaciones;
- fechas;
- palabras clave;
- estructuras asociadas;
- o referencias cruzadas.

Una búsqueda avanzada suele consistir precisamente en consultar determinados campos.

No es lo mismo buscar una palabra:

- en cualquier parte del registro;
- únicamente en el nombre del gen;
- en el organismo;
- en el título de una publicación;
- o en un identificador.

Comprender los campos permite realizar búsquedas más precisas.

---

## 2.2.5. Relaciones entre registros

Los datos biológicos están relacionados.

Por ejemplo:

**gen → transcrito → proteína → estructura → función → publicación**

Una base de datos moderna intenta representar parte de estas relaciones.

Estas conexiones permiten navegar desde un tipo de información hacia otro.

Podemos comenzar con un gen y llegar a:

- su secuencia;
- proteínas asociadas;
- publicaciones;
- variantes;
- estructuras;
- o recursos externos.

Esta navegación constituye una de las características más potentes del ecosistema bioinformático.

---

## 2.2.6. Referencias cruzadas

Las **referencias cruzadas** enlazan registros pertenecientes a recursos diferentes.

Por ejemplo, un registro de proteína puede incluir enlaces hacia:

- una base de datos de genes;
- una base de datos estructural;
- un recurso de dominios;
- una publicación;
- o una vía metabólica.

Estas referencias permiten integrar información distribuida.

Una misma entidad biológica puede tener diferentes identificadores dependiendo del recurso.

Por ello, una parte importante del trabajo bioinformático consiste en saber traducir o relacionar identificadores.

---

## 2.2.7. Búsqueda simple y búsqueda avanzada

### Búsqueda simple

Se basa normalmente en una palabra, nombre o identificador.

Es útil para una primera exploración.

### Búsqueda avanzada

Permite combinar diferentes criterios.

Por ejemplo:

- organismo;
- tipo de molécula;
- longitud;
- fecha;
- estado de revisión;
- función;
- presencia de estructura;
- o términos específicos.

La diferencia es importante.

Una búsqueda simple responde:

> ¿qué registros contienen este término?

Una búsqueda avanzada puede responder:

> ¿qué proteínas humanas revisadas contienen este término y además tienen información estructural?

---

## 2.2.8. Recuperación frente a interpretación

Recuperar un registro no significa haber resuelto un problema.

Una búsqueda correcta implica al menos tres fases:

**Localizar → interpretar → validar**

### Localizar

Encontrar el registro adecuado.

### Interpretar

Comprender qué representa cada campo.

### Validar

Comprobar procedencia, evidencia, estado de revisión y coherencia con otras fuentes.

Esta secuencia será importante en todas las prácticas de la asignatura.

---

# 2.3. NCBI, EMBL-EBI, UniProt y PDB

Los cuatro recursos que se presentan en este apartado no cumplen exactamente la misma función.

Algunos son grandes infraestructuras que agrupan muchos servicios y bases de datos, mientras que otros están especializados en un tipo concreto de información.

La pregunta no debería ser:

> **¿Cuál es la mejor base de datos?**

sino:

> **¿Cuál es el recurso adecuado para la información que necesito?**

---

## 2.3.1. NCBI

El **National Center for Biotechnology Information (NCBI)** proporciona acceso a una amplia colección de información biomédica y genómica.

Entre sus recursos más conocidos se encuentran:

- PubMed;
- Nucleotide;
- Gene;
- Protein;
- Genome;
- BLAST;
- PubChem;
- y otros recursos especializados.

NCBI actúa como un gran punto de entrada a información biológica diversa.

### Qué tipo de preguntas podemos abordar

Podemos utilizar NCBI para localizar:

- información sobre genes;
- secuencias de nucleótidos;
- secuencias de proteínas;
- genomas;
- publicaciones;
- variantes;
- o relaciones entre diferentes tipos de registros.

### Navegación entre recursos

Una de las características más importantes de NCBI es la conexión entre bases de datos.

Desde un registro de Gene, por ejemplo, podemos acceder a:

- secuencias;
- publicaciones;
- proteínas;
- genomas;
- y otros recursos relacionados.

Esto permite pasar de una entidad biológica a distintos niveles de información.

### Sitio web

https://www.ncbi.nlm.nih.gov/

---

## 2.3.2. EMBL-EBI

El **European Bioinformatics Institute (EMBL-EBI)** forma parte del European Molecular Biology Laboratory.

Mantiene una amplia colección de recursos de datos y herramientas para investigación en ciencias de la vida.

Entre los recursos vinculados a EMBL-EBI se encuentran servicios relacionados con:

- secuencias;
- genomas;
- proteínas;
- estructuras;
- expresión;
- literatura;
- anotación funcional;
- y análisis bioinformático.

EMBL-EBI no debe entenderse como una única base de datos.

Es una **infraestructura que mantiene y coordina numerosos recursos especializados**.

### Una perspectiva europea

EMBL-EBI desempeña un papel central en la infraestructura europea de datos biológicos y participa en iniciativas internacionales de intercambio y conservación de información.

Muchos recursos utilizados diariamente en Bioinformática están alojados, coordinados o mantenidos desde EMBL-EBI.

### Sitio web

https://www.ebi.ac.uk/

---

## 2.3.3. UniProt

**UniProt** es uno de los principales recursos de información sobre proteínas.

Su núcleo es **UniProtKB**, que integra:

- secuencias de proteínas;
- nombres;
- funciones;
- información sobre genes;
- taxonomía;
- localización;
- dominios;
- modificaciones;
- referencias bibliográficas;
- y referencias cruzadas.

Una característica importante es la distinción entre registros:

- **revisados**, asociados a UniProtKB/Swiss-Prot;
- **no revisados**, asociados a UniProtKB/TrEMBL.

Los registros revisados han sido objeto de curación, mientras que los no revisados dependen en mayor medida de procedimientos automáticos.

Esto convierte UniProt en un ejemplo especialmente útil para comprender la diferencia entre:

**dato → anotación automática → curación → conocimiento integrado**

### Preguntas típicas

UniProt puede utilizarse para consultar:

- la secuencia de una proteína;
- su función;
- el gen asociado;
- dominios;
- modificaciones;
- localización;
- referencias;
- y conexiones con otros recursos.

### Sitio web

https://www.uniprot.org/

---

## 2.3.4. PDB

El **Protein Data Bank (PDB)** es el archivo internacional de estructuras tridimensionales de macromoléculas biológicas.

Contiene información estructural sobre:

- proteínas;
- ADN;
- ARN;
- complejos biomoleculares;
- y moléculas asociadas.

Las estructuras del archivo PDB proceden fundamentalmente de métodos experimentales de determinación estructural.

El portal RCSB PDB permite buscar, visualizar y analizar estas estructuras.

### Información que puede encontrarse

Un registro estructural puede incluir:

- coordenadas atómicas;
- cadenas;
- ligandos;
- método experimental;
- resolución;
- autores;
- publicaciones;
- organismo;
- y referencias cruzadas.

### Estructuras experimentales y modelos computacionales

Es importante distinguir entre:

- estructuras depositadas en el archivo PDB;
- y modelos estructurales calculados mediante métodos computacionales.

Los portales actuales pueden mostrar ambos tipos de información, pero no representan el mismo nivel de evidencia.

Esta diferencia será especialmente importante en el Bloque IV, cuando estudiemos predicción estructural e inteligencia artificial.

### Sitio web

https://www.rcsb.org/

---

# 2.4. Comparación de recursos

Una misma pregunta biológica puede requerir varios recursos.

| Necesidad | Recurso que puede ser útil |
|---|---|
| Buscar información general sobre un gen | NCBI Gene |
| Recuperar una secuencia nucleotídica | NCBI Nucleotide / recursos EMBL-EBI |
| Consultar información funcional de una proteína | UniProt |
| Localizar literatura científica | PubMed |
| Buscar una estructura tridimensional | PDB |
| Explorar recursos y herramientas europeas | EMBL-EBI |

Esta tabla es únicamente orientativa.

Los recursos están conectados y, en muchos casos, la información se solapa.

La competencia importante no consiste en memorizar qué botón utilizar, sino en comprender:

> **qué representa cada registro y qué nivel de evidencia contiene.**

---

# 2.5. Ejemplo de recorrido de información

Supongamos que queremos investigar una proteína relacionada con una enfermedad.

Podríamos comenzar con el nombre del gen.

### Paso 1. NCBI

Localizamos el registro del gen y obtenemos:

- identificadores;
- organismo;
- localización;
- referencias;
- secuencias relacionadas.

### Paso 2. UniProt

Seguimos una referencia hacia la proteína correspondiente.

Consultamos:

- secuencia;
- función;
- estado de revisión;
- dominios;
- variantes;
- referencias.

### Paso 3. PDB

Comprobamos si existe una estructura tridimensional experimental.

Podemos analizar:

- método experimental;
- cadenas;
- ligandos;
- resolución;
- regiones representadas.

### Paso 4. Literatura

Consultamos las publicaciones asociadas.

De esta manera, diferentes recursos aportan distintas capas de información sobre la misma entidad biológica.

---

# 2.6. Estrategia básica de recuperación de información

Ante cualquier consulta bioinformática puede utilizarse el siguiente esquema:

## Paso 1. Definir la entidad

¿Qué estoy buscando?

- un gen;
- una proteína;
- una secuencia;
- una estructura;
- una publicación;
- o una función.

## Paso 2. Seleccionar el recurso

¿Dónde se representa mejor ese tipo de información?

## Paso 3. Buscar

Utilizar:

- nombre;
- sinónimo;
- organismo;
- identificador;
- o combinación de campos.

## Paso 4. Confirmar el registro

Comprobar:

- organismo;
- descripción;
- identificador;
- tipo de entidad.

## Paso 5. Evaluar la evidencia

Preguntar:

- ¿es experimental o predicha?
- ¿está revisada?
- ¿de dónde procede?
- ¿qué publicaciones la respaldan?

## Paso 6. Registrar la procedencia

Anotar:

- recurso;
- identificador;
- versión si procede;
- fecha de consulta;
- y cualquier información relevante para reproducir la búsqueda.

---

# 2.7. Errores frecuentes

## Confundir nombre con identificador

Los nombres pueden presentar sinónimos o variar entre organismos.

El identificador suele ser una referencia más precisa.

## Elegir el primer resultado

El primer registro mostrado no tiene por qué corresponder al organismo o entidad buscada.

## Ignorar el organismo

Genes y proteínas con nombres similares pueden existir en especies diferentes.

## No comprobar el estado de revisión

Dos registros pueden contener información con diferentes niveles de curación.

## Confundir predicción con evidencia experimental

Un dato computacional puede ser muy útil, pero debe interpretarse como tal.

## Copiar información sin registrar la fuente

La trazabilidad es esencial.

## Buscar únicamente por texto libre

Cuando sea posible, conviene utilizar campos e identificadores.

---

# 2.8. Cuestiones guía

1. ¿Qué diferencia conceptual existe entre una base de datos primaria y una secundaria?
2. ¿Por qué esta distinción no siempre es completamente rígida?
3. ¿Qué papel desempeña la curación en una base de datos biológica?
4. ¿Por qué un identificador suele ser más fiable que un nombre?
5. ¿Qué ventajas ofrecen las referencias cruzadas?
6. ¿Qué diferencia existe entre localizar un registro e interpretarlo correctamente?
7. ¿Qué recurso utilizarías para buscar una proteína y su función?
8. ¿Qué recurso utilizarías para localizar una estructura tridimensional?
9. ¿Por qué es importante distinguir información experimental de información predicha?
10. ¿Qué datos deberíamos registrar para poder repetir una búsqueda bioinformática?

---

# Ideas clave

- Las bases de datos biológicas organizan datos mediante registros, campos, identificadores y relaciones.
- Las bases de datos primarias almacenan fundamentalmente datos depositados o experimentales; las secundarias añaden análisis, integración o anotación.
- La separación entre bases primarias y secundarias no siempre es absoluta.
- La curación y el nivel de evidencia son elementos esenciales para interpretar un registro.
- Los identificadores permiten localizar entidades de forma más precisa que los nombres.
- Las referencias cruzadas conectan diferentes capas del ecosistema bioinformático.
- NCBI y EMBL-EBI son grandes infraestructuras que integran numerosos recursos.
- UniProt está especializado en información sobre proteínas.
- PDB almacena información estructural tridimensional de macromoléculas.
- Recuperar información no significa simplemente encontrar un resultado: hay que identificar, interpretar y validar el registro.

---

# Conexión con el Tema 3

En este tema hemos estudiado **dónde se almacena la información y cómo se organiza dentro de los recursos bioinformáticos**.

El siguiente tema se centrará en **cómo se representa esa información de forma computacional**.

Estudiaremos:

- formatos como FASTA, GenBank y PDB;
- metadatos y anotación;
- calidad;
- interoperabilidad;
- y reutilización de datos.

La secuencia del bloque puede resumirse así:

**ecosistema bioinformático → bases de datos → representación de datos**

---

# Recursos oficiales

- NCBI: https://www.ncbi.nlm.nih.gov/
- EMBL-EBI: https://www.ebi.ac.uk/
- UniProt: https://www.uniprot.org/
- RCSB PDB: https://www.rcsb.org/

---

# Bibliografía del bloque

Según el proyecto docente, para el Bloque I se recomienda la siguiente bibliografía:

- Lesk, A. M. *Introduction to Bioinformatics*.
- Pevsner, J. *Bioinformatics and Functional Genomics*.
- Buffalo, V. *Bioinformatics Data Skills*.
- Zvelebil, M. J. y Baum, J. O. *Understanding Bioinformatics*.
