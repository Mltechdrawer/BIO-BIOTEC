# Tema 1. Introducción a la Bioinformática y ecosistema digital biomolecular

## Objetivos

- Explicar qué papel desempeña la Bioinformática en la investigación biológica actual.
- Describir, de forma general, cómo ha evolucionado la Bioinformática desde sus primeras aplicaciones hasta el actual ecosistema digital biomolecular.
- Identificar los principales componentes de una infraestructura de datos biológicos.
- Comprender el recorrido que sigue un dato biológico desde su generación hasta su reutilización.
- Reconocer algunas de las principales aplicaciones de la Bioinformática en distintos ámbitos de la Biotecnología.

---

## Introducción

La Biología contemporánea produce una cantidad de información difícil de manejar únicamente mediante observación experimental y análisis manual. Secuencias de ADN y ARN, proteínas, estructuras tridimensionales, perfiles de expresión génica, relaciones funcionales o información sobre variantes genéticas forman parte de un volumen creciente de datos que debe almacenarse, organizarse, compararse, interpretarse y compartir.

La **Bioinformática** surge precisamente en la intersección entre la Biología, la Informática, las Matemáticas y la Estadística para abordar estas necesidades. No se limita al uso de programas informáticos aplicados a problemas biológicos. También comprende los métodos, modelos, infraestructuras y procedimientos necesarios para representar la información biológica de forma computacional y extraer conocimiento a partir de ella.

En la investigación actual, el trabajo experimental y el análisis computacional están cada vez más conectados. Un experimento puede generar datos que posteriormente se procesan mediante herramientas bioinformáticas, pero también es posible iniciar una investigación a partir de información que ya ha sido producida por otros grupos y depositada en repositorios públicos. De esta forma, el laboratorio físico convive con un amplio **ecosistema digital biomolecular** formado por bases de datos, repositorios, herramientas de análisis, servicios web, estándares y recursos computacionales.

Este primer tema presenta ese contexto general. El objetivo no es estudiar todavía en detalle las bases de datos concretas ni los formatos utilizados para representar la información biológica, sino comprender por qué existen, cómo se relacionan entre sí y qué papel desempeñan en la investigación y en la Biotecnología.

---

## 1.1. Evolución de la Bioinformática

### De las primeras secuencias al análisis computacional

La necesidad de aplicar métodos computacionales a la Biología apareció antes de que existieran los grandes proyectos genómicos actuales. Cuando comenzaron a determinarse secuencias de proteínas y ácidos nucleicos, surgió de manera inmediata un problema de representación y comparación: ¿cómo almacenar esas secuencias?, ¿cómo localizar similitudes entre ellas?, ¿cómo identificar regiones conservadas?, ¿cómo relacionar una nueva secuencia con otras previamente conocidas?

Estas preguntas pueden formularse como problemas computacionales. Una secuencia biológica puede representarse mediante una cadena de símbolos y, a partir de esa representación, pueden diseñarse algoritmos para compararla con otras secuencias, localizar patrones o establecer relaciones.

La Bioinformática se desarrolló inicialmente alrededor de estas necesidades. La información biológica comenzó a organizarse en colecciones digitales y se diseñaron métodos específicos para realizar búsquedas, alineamientos y comparaciones.

### El impacto de la secuenciación masiva

La evolución de las tecnologías de secuenciación modificó profundamente la escala del problema. Mientras que inicialmente obtener una secuencia podía requerir un esfuerzo considerable, la automatización de los procedimientos experimentales permitió producir cantidades cada vez mayores de información.

Los proyectos de secuenciación de genomas completos marcaron un cambio importante. El objeto de estudio ya no era solamente una secuencia individual, sino conjuntos masivos de secuencias que debían ensamblarse, almacenarse, anotarse y analizarse.

Con el desarrollo posterior de las tecnologías de secuenciación de alto rendimiento, esta tendencia se aceleró. La generación de datos dejó de ser necesariamente el principal cuello de botella del proceso. En muchos contextos, el reto pasó a ser la **gestión y el análisis de los datos producidos**.

Esto transformó también el papel de la Bioinformática. Ya no se trataba únicamente de ejecutar un determinado algoritmo sobre una secuencia, sino de diseñar flujos completos capaces de procesar grandes cantidades de información de forma reproducible.

### De la genómica a las ciencias ómicas

El crecimiento de la Bioinformática ha ido acompañado de la aparición de diferentes áreas de análisis molecular a gran escala. Entre ellas se encuentran:

- la **genómica**, centrada en el estudio de los genomas;
- la **transcriptómica**, relacionada con el conjunto de ARN expresado;
- la **proteómica**, orientada al estudio de proteínas;
- la **metagenómica**, que permite estudiar comunidades de microorganismos a partir de su material genético;
- y otras áreas que integran diferentes tipos de información molecular.

Cada una de ellas genera datos con características propias, pero todas comparten necesidades comunes: almacenamiento, normalización, integración, comparación, análisis y reutilización.

La Bioinformática se convierte así en una disciplina transversal que proporciona métodos y herramientas para trabajar con diferentes niveles de información biológica.

### Integración de datos y automatización

A medida que aumentó el número de fuentes disponibles, apareció un nuevo reto: **integrar información procedente de recursos diferentes**.

Por ejemplo, para estudiar una proteína puede ser necesario combinar su secuencia, información funcional, variantes conocidas, organismos en los que aparece, bibliografía científica y estructuras tridimensionales. Cada elemento puede proceder de una fuente distinta.

Por esta razón, la Bioinformática actual no consiste únicamente en analizar conjuntos de datos aislados. Una parte importante del trabajo consiste en relacionar recursos, comprobar la procedencia de la información y construir procesos que permitan recuperar y combinar datos de forma coherente.

La automatización también ha adquirido una importancia creciente. Muchos análisis se organizan actualmente como secuencias de pasos que pueden ejecutarse de manera sistemática: recuperar datos, comprobar su calidad, transformarlos, analizarlos, generar resultados y documentar el proceso.

### Inteligencia artificial y Bioinformática

En los últimos años, los métodos de inteligencia artificial han ampliado las posibilidades de análisis en Bioinformática. Se utilizan, entre otras aplicaciones, para clasificación de datos biológicos, predicción de propiedades moleculares, análisis de secuencias y predicción estructural.

La aparición de herramientas basadas en inteligencia artificial no elimina la necesidad de comprender los datos y los procedimientos utilizados. Al contrario, aumenta la importancia de cuestiones como la calidad de la información de entrada, la validación de los resultados, la reproducibilidad y la interpretación crítica de las predicciones.

A lo largo de la asignatura se volverá sobre estas cuestiones en distintos contextos. En este primer tema basta con retener una idea: la Bioinformática evoluciona junto con las tecnologías capaces de **generar, almacenar y analizar información biológica**.

---

## 1.2. Infraestructuras de datos biológicos

### Un ecosistema distribuido

Los datos utilizados en Bioinformática no se encuentran almacenados en un único lugar. La investigación biológica se apoya en una red internacional de instituciones, repositorios, bases de datos y servicios especializados.

Podemos imaginar este entorno como un **ecosistema digital distribuido**. Diferentes organizaciones mantienen recursos que almacenan determinados tipos de información y ofrecen mecanismos para consultarlos, descargarlos o analizarlos.

Algunos recursos contienen secuencias de ADN o ARN; otros se especializan en proteínas, estructuras moleculares, variantes, información funcional o literatura científica. Muchos de ellos están conectados mediante identificadores y referencias cruzadas.

Este ecosistema permite que un dato producido en un laboratorio pueda ser reutilizado posteriormente por otros investigadores en contextos diferentes.

### Del experimento al repositorio

De forma simplificada, un dato biológico puede recorrer varias etapas:

**Generación → procesamiento → anotación → almacenamiento → publicación → reutilización**

La secuencia exacta puede variar dependiendo del tipo de experimento, pero este esquema permite comprender el ciclo general de la información.

#### Generación

El dato se obtiene mediante una técnica experimental. Puede tratarse, por ejemplo, de una secuencia, una medida de expresión, una estructura molecular o cualquier otra observación susceptible de ser digitalizada.

#### Procesamiento

Los datos originales suelen necesitar algún tipo de tratamiento antes de poder ser interpretados. Puede ser necesario corregir errores, filtrar información, convertir formatos o aplicar algoritmos específicos.

#### Anotación

Un dato aislado tiene un valor limitado si no está acompañado de información que permita interpretarlo. La anotación añade contexto: qué organismo está implicado, qué región se ha estudiado, qué método se ha utilizado o qué función se ha asociado a un elemento biológico.

#### Almacenamiento

Los datos se incorporan a sistemas diseñados para conservarlos y permitir su recuperación. Dependiendo de su naturaleza, pueden almacenarse en repositorios generales o especializados.

#### Publicación

La información científica suele estar vinculada a publicaciones, proyectos de investigación o conjuntos de datos accesibles mediante identificadores persistentes.

#### Reutilización

Otros investigadores pueden recuperar posteriormente esos datos para responder nuevas preguntas, comparar resultados o integrarlos con información procedente de otros estudios.

Este último paso es especialmente importante. La utilidad de un conjunto de datos no termina necesariamente con el estudio que lo generó.

### Repositorios, bases de datos y servicios

Aunque estos términos se utilizan a veces de manera indistinta, conviene establecer una diferencia conceptual.

Un **repositorio** tiene como función principal conservar y proporcionar acceso a conjuntos de datos o registros.

Una **base de datos biológica** organiza la información siguiendo una determinada estructura para facilitar su consulta, relación e interpretación.

Un **servicio bioinformático** permite realizar operaciones sobre los datos, como búsquedas, comparaciones, análisis o visualizaciones.

En la práctica, muchos grandes recursos bioinformáticos combinan estas funciones. Una misma plataforma puede almacenar información, permitir búsquedas complejas, ofrecer herramientas de análisis y relacionar sus registros con otros recursos.

En el Tema 2 estudiaremos con mayor detalle algunos de estos recursos y veremos ejemplos concretos como NCBI, EMBL-EBI, UniProt y PDB.

### Identificadores y referencias cruzadas

Para que los recursos puedan relacionarse entre sí es necesario disponer de mecanismos que permitan identificar de forma inequívoca sus registros.

Por esta razón, las bases de datos utilizan **identificadores**, también denominados frecuentemente números de acceso o *accession numbers*. Estos códigos permiten localizar un registro determinado y citarlo de forma precisa.

Los identificadores también hacen posible establecer **referencias cruzadas** entre diferentes bases de datos. Un registro de una proteína puede, por ejemplo, enlazar con la secuencia que la codifica, con información bibliográfica o con una estructura tridimensional disponible en otro recurso.

Esta capacidad de relacionar información es uno de los elementos fundamentales del ecosistema bioinformático.

### Metadatos

Junto al dato biológico aparecen los **metadatos**, es decir, información que describe el propio dato y su contexto.

Los metadatos pueden indicar, entre otras cuestiones:

- el organismo del que procede una muestra;
- el método experimental utilizado;
- las condiciones en las que se realizó un experimento;
- la fecha de obtención o publicación;
- la procedencia del registro;
- o las relaciones con otros datos.

Sin metadatos adecuados, un conjunto de datos puede resultar difícil de interpretar o reutilizar.

La gestión de los metadatos será especialmente relevante cuando estudiemos en el Tema 3 la representación y gestión de información biológica.

### Calidad, interoperabilidad y reutilización

La existencia de grandes cantidades de datos no garantiza por sí sola que sean útiles.

Para que la información pueda reutilizarse es necesario considerar aspectos como:

- su procedencia;
- la calidad de los datos;
- la forma en la que han sido anotados;
- los formatos utilizados;
- la existencia de identificadores estables;
- y la documentación del proceso mediante el cual se han generado.

La **interoperabilidad** se refiere a la capacidad de diferentes sistemas y recursos para intercambiar y utilizar información de manera coherente. En Bioinformática es especialmente importante porque los análisis suelen combinar información procedente de múltiples fuentes.

A lo largo de la asignatura veremos que una parte importante del trabajo bioinformático no consiste únicamente en obtener un resultado, sino en poder explicar **de dónde proceden los datos, qué transformaciones han sufrido y cómo se ha llegado al resultado final**.

---

## 1.3. Papel de la Bioinformática en la investigación y la Biotecnología

### Una herramienta para formular y responder preguntas

La Bioinformática no debe entenderse únicamente como una fase posterior al trabajo experimental. También puede intervenir antes de diseñar un experimento.

Supongamos que un equipo quiere estudiar una proteína relacionada con un determinado proceso biológico. Antes de realizar nuevos experimentos podría preguntarse:

- ¿se conoce ya su secuencia?
- ¿existen proteínas similares en otros organismos?
- ¿qué función se le atribuye?
- ¿se dispone de alguna estructura tridimensional?
- ¿qué trabajos científicos la han estudiado?
- ¿existen variantes conocidas?
- ¿qué otros genes o proteínas aparecen relacionados con ella?

Muchas de estas preguntas pueden comenzar a responderse utilizando información pública disponible en recursos bioinformáticos.

El análisis computacional permite así aprovechar conocimiento previamente generado y puede ayudar a formular hipótesis o decidir qué experimentos resulta conveniente realizar.

### Complementariedad entre laboratorio y análisis computacional

El trabajo experimental y la Bioinformática forman un ciclo que se retroalimenta.

Un experimento genera datos. Los datos se analizan mediante métodos computacionales. El análisis produce resultados que pueden sugerir nuevas hipótesis. Estas hipótesis pueden requerir nuevos experimentos.

Podemos representarlo de forma simplificada:

**Pregunta biológica → experimento → datos → análisis bioinformático → interpretación → nueva pregunta**

Pero también puede comenzar en otro punto:

**Datos públicos → análisis bioinformático → hipótesis → experimento**

Esta segunda posibilidad es una de las consecuencias más importantes de la existencia de grandes infraestructuras internacionales de datos biológicos.

### Aplicaciones en Biotecnología

La Bioinformática interviene actualmente en numerosos ámbitos de la Biotecnología.

#### Biomedicina

El análisis de información genética y molecular puede contribuir al estudio de enfermedades, variantes genéticas, mecanismos moleculares y posibles dianas terapéuticas.

#### Desarrollo de fármacos

La información sobre secuencias, estructuras y funciones de proteínas permite seleccionar y caracterizar posibles dianas, estudiar interacciones moleculares y apoyar distintas etapas del descubrimiento de fármacos.

#### Biotecnología industrial

La búsqueda y caracterización de enzimas con determinadas propiedades puede beneficiarse de la comparación de secuencias, la información funcional y el análisis estructural.

#### Agricultura y mejora vegetal

Los datos genómicos permiten estudiar genes relacionados con características de interés, analizar diversidad genética y apoyar programas de mejora.

#### Microbiología y biotecnología ambiental

La Bioinformática permite estudiar microorganismos y comunidades microbianas mediante información genética, incluso en situaciones en las que no todos los organismos pueden cultivarse fácilmente en laboratorio.

Estos ejemplos no representan áreas independientes. En muchas investigaciones se combinan diferentes tipos de información y herramientas.

### Del dato al conocimiento

Una característica importante de la Bioinformática es que trabaja en varios niveles.

Podemos distinguir, de forma simplificada:

**Dato → información → interpretación → conocimiento**

Una secuencia es un dato. Cuando conocemos su procedencia, sus características y su relación con otros registros, disponemos de información adicional. Cuando analizamos esa información para responder una pregunta biológica estamos realizando una interpretación. Si esa interpretación puede relacionarse con conocimiento existente y validarse adecuadamente, puede contribuir a generar nuevo conocimiento científico.

El objetivo de las herramientas bioinformáticas no es sustituir la interpretación biológica. Su función es permitir trabajar de forma sistemática con cantidades y relaciones de información que resultarían muy difíciles de manejar manualmente.

### Competencia bioinformática

Para un profesional de la Biotecnología, utilizar Bioinformática no significa necesariamente desarrollar nuevos algoritmos o implementar desde cero las herramientas utilizadas.

Sí implica, en cambio, adquirir capacidad para:

- formular adecuadamente una pregunta;
- identificar qué tipo de información puede ayudar a responderla;
- seleccionar una fuente apropiada;
- recuperar y organizar los datos;
- utilizar correctamente las herramientas disponibles;
- interpretar los resultados;
- evaluar sus limitaciones;
- y documentar el proceso seguido.

Estas competencias serán el hilo conductor de las actividades prácticas de la asignatura.

---

## Una visión conjunta: el ecosistema digital biomolecular

Los tres apartados anteriores pueden reunirse en una misma idea.

La investigación biológica actual funciona dentro de un ecosistema en el que:

1. los laboratorios generan datos;
2. los datos se transforman en registros digitales;
3. los registros se almacenan en repositorios y bases de datos;
4. diferentes recursos se relacionan mediante identificadores y referencias;
5. las herramientas bioinformáticas permiten buscar, comparar y analizar la información;
6. los resultados se interpretan en un contexto biológico;
7. y el conocimiento generado puede producir nuevos datos que vuelven a incorporarse al ecosistema.

La Bioinformática proporciona los métodos y herramientas que permiten recorrer ese ciclo.

Por ello, una de las competencias fundamentales que comenzaremos a desarrollar en este bloque puede resumirse mediante cinco preguntas:

> **¿Qué información existe? ¿Dónde está? ¿Cómo puedo recuperarla? ¿Cómo debo interpretarla? ¿Hasta qué punto puedo confiar en ella?**

Estas preguntas aparecerán repetidamente a lo largo de la asignatura.

En el siguiente tema nos centraremos en la segunda y tercera de ellas: estudiaremos cómo se organizan las **bases de datos biológicas** y cómo podemos recuperar información desde algunos de los principales recursos bioinformáticos internacionales.

---

## Ideas clave

- La Bioinformática integra métodos computacionales para representar, gestionar, analizar e interpretar información biológica.
- Su evolución está estrechamente ligada al aumento de la capacidad para generar datos moleculares.
- La investigación biológica actual se apoya en un ecosistema distribuido de repositorios, bases de datos y servicios bioinformáticos.
- Los datos necesitan contexto, metadatos, identificadores y documentación para poder ser interpretados y reutilizados.
- La Bioinformática conecta el trabajo experimental con el análisis computacional y puede intervenir tanto antes como después de un experimento.
- En Biotecnología, una competencia esencial consiste en localizar, recuperar, evaluar, analizar y documentar información biológica procedente de fuentes especializadas.

---

## Bibliografía del bloque

Para este tema se utilizará la bibliografía básica y recomendada indicada para el Bloque I en el proyecto docente de la asignatura:

- Lesk, A. M. *Introduction to Bioinformatics*.
- Pevsner, J. *Bioinformatics and Functional Genomics*.
- Buffalo, V. *Bioinformatics Data Skills*.
- Zvelebil, M. J. y Baum, J. O. *Understanding Bioinformatics*.
