# Tema 7. Anotación computacional de genes y proteínas

## Duración

**1 hora de teoría**

Este tema abre el **Bloque III. Análisis funcional y minería de datos biológicos**.

De acuerdo con la guía docente, se estructura en tres apartados:

- **7.1. Concepto de anotación.**
- **7.2. Fuentes de información funcional.**
- **7.3. Flujo de anotación bioinformática.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar qué significa anotar un gen o una proteína.
- Diferenciar entre anotación estructural y anotación funcional.
- Reconocer que una anotación puede proceder de evidencia experimental, inferencia computacional o integración de múltiples fuentes.
- Identificar fuentes de información funcional utilizadas habitualmente en Bioinformática.
- Comprender el papel de dominios, familias, motivos y referencias bibliográficas en la anotación.
- Describir un flujo básico de anotación bioinformática.
- Valorar la calidad de una anotación atendiendo a su procedencia y nivel de evidencia.
- Comprender que la anotación es un proceso dinámico y revisable.

---

# Introducción

En los bloques anteriores hemos aprendido a localizar información biológica, recuperar secuencias y compararlas.

Ahora damos un paso diferente.

Ya no nos preguntamos únicamente:

> **¿qué secuencia es esta?**

sino:

> **¿qué significa biológicamente esta secuencia?**

Podemos disponer de una secuencia completa y correcta y, sin embargo, saber muy poco sobre ella.

Por ejemplo, una proteína puede tener cientos de aminoácidos, pero necesitamos responder preguntas como:

- ¿qué función realiza?
- ¿en qué proceso participa?
- ¿qué dominio contiene?
- ¿en qué parte de la célula actúa?
- ¿qué genes o proteínas están relacionados con ella?
- ¿existe evidencia experimental?
- ¿qué parte de la información es una predicción?

La **anotación** intenta responder a estas preguntas.

En Bioinformática, anotar consiste en asociar información biológica interpretable a una secuencia o entidad molecular.

---

# 7.1. Concepto de anotación

## 7.1.1. Del dato a la interpretación

Consideremos una secuencia:

```text
MKWVTFISLLFLFSSAYSR...
```

Por sí sola contiene información molecular, pero no nos indica directamente:

- qué proteína es;
- qué función desempeña;
- dónde se localiza;
- qué dominios contiene;
- o en qué procesos participa.

Cuando añadimos información como:

```text
Proteína: ...
Función: ...
Localización: ...
Dominio: ...
Proceso biológico: ...
```

estamos anotando la secuencia.

La anotación transforma un dato molecular en información interpretable.

---

## 7.1.2. Anotación estructural y funcional

Podemos distinguir, de forma general, dos niveles.

### Anotación estructural

Describe **qué elementos existen y dónde se encuentran**.

En una secuencia genómica puede incluir:

- genes;
- exones;
- intrones;
- regiones codificantes;
- sitios de inicio y terminación.

### Anotación funcional

Describe **qué función puede desempeñar el elemento identificado**.

Puede incluir:

- función molecular;
- proceso biológico;
- localización celular;
- dominios;
- familias;
- rutas metabólicas;
- interacciones.

En este bloque nos centraremos principalmente en la anotación funcional.

---

## 7.1.3. Anotación manual y automática

### Anotación manual

Es revisada por expertos.

Puede incorporar:

- resultados experimentales;
- literatura científica;
- conocimiento especializado;
- revisión crítica de evidencias.

Suele ofrecer información de alta calidad, aunque no es viable revisar manualmente millones de secuencias.

### Anotación automática

Se genera mediante herramientas computacionales.

Puede basarse en:

- similitud de secuencia;
- presencia de dominios;
- motivos;
- perfiles;
- reglas;
- modelos predictivos.

Permite trabajar a gran escala, pero necesita ser interpretada con cautela.

---

## 7.1.4. Evidencia experimental e inferencia

Una anotación puede estar apoyada por distintos niveles de evidencia.

### Evidencia experimental

Existe un experimento que respalda directamente la función.

### Inferencia computacional

La función se propone a partir de información como:

- similitud con proteínas conocidas;
- pertenencia a una familia;
- presencia de un dominio;
- conservación evolutiva.

### Integración de evidencias

En muchos casos, la anotación final combina varios tipos de información.

Por ello, una pregunta importante es:

> **¿qué evidencia respalda esta anotación?**

---

## 7.1.5. Transferencia de anotación por similitud

Una estrategia frecuente consiste en comparar una secuencia desconocida con otra ya caracterizada.

Si existe una relación suficientemente fuerte, podemos utilizar la información conocida como apoyo para proponer una función.

Pero esta transferencia tiene riesgos.

Dos secuencias similares pueden:

- tener funciones parecidas;
- haber divergido funcionalmente;
- compartir solo un dominio;
- pertenecer a miembros diferentes de una familia.

Por ello:

> **similitud de secuencia no equivale automáticamente a identidad funcional**

---

## 7.1.6. Dominios y motivos

Una proteína puede contener regiones con funciones concretas.

### Dominio

Es una región que puede presentar:

- estructura propia;
- función característica;
- conservación evolutiva.

Una misma proteína puede contener varios dominios.

### Motivo

Es una secuencia corta conservada asociada con una característica funcional o estructural.

La detección de dominios y motivos ayuda a interpretar proteínas incluso cuando la función completa no está bien caracterizada.

---

## 7.1.7. Familias de proteínas

Las proteínas relacionadas pueden agruparse en familias.

Los miembros de una familia pueden compartir:

- origen evolutivo;
- dominios;
- motivos;
- estructura;
- funciones relacionadas.

La pertenencia a una familia aporta información útil para la anotación, pero no debe utilizarse sin considerar diferencias entre miembros.

---

# 7.2. Fuentes de información funcional

## 7.2.1. UniProt

**UniProt** es uno de los principales recursos para información funcional sobre proteínas.

Un registro puede incluir:

- nombre y función;
- organismo;
- secuencia;
- localización celular;
- dominios y regiones;
- modificaciones;
- variantes;
- referencias bibliográficas;
- evidencias;
- enlaces a otros recursos.

Es especialmente importante distinguir entre información revisada y anotaciones generadas automáticamente.

Recurso: https://www.uniprot.org/

---

## 7.2.2. InterPro

**InterPro** integra información procedente de diferentes recursos especializados para identificar:

- familias;
- dominios;
- sitios funcionales;
- regiones conservadas.

Permite analizar una proteína y observar qué firmas funcionales aparecen en su secuencia.

Recurso: https://www.ebi.ac.uk/interpro/

---

## 7.2.3. Pfam

**Pfam** se ha utilizado ampliamente para identificar familias y dominios proteicos mediante modelos construidos a partir de alineamientos de secuencias.

Su información está actualmente integrada y accesible a través de recursos como InterPro.

La idea fundamental es que un dominio conservado puede detectarse aunque la proteína completa haya divergido.

---

## 7.2.4. Gene Ontology

**Gene Ontology (GO)** proporciona un vocabulario estructurado para describir funciones de genes y proteínas.

Organiza términos en tres grandes categorías:

- **Molecular Function**: qué actividad realiza.
- **Biological Process**: en qué proceso participa.
- **Cellular Component**: dónde actúa.

GO será desarrollado con mayor detalle en el Tema 8.

Recurso: https://geneontology.org/

---

## 7.2.5. Rutas y procesos

Existen recursos que relacionan genes y proteínas con rutas y procesos biológicos.

Entre ellos:

- Reactome;
- KEGG;
- otros recursos especializados.

Estos recursos permiten pasar de la función de una proteína individual a una visión más amplia del sistema biológico.

Reactome: https://reactome.org/

---

## 7.2.6. Literatura científica

La literatura sigue siendo una fuente esencial.

Una anotación puede estar respaldada por:

- estudios bioquímicos;
- experimentos de expresión;
- análisis genéticos;
- caracterización estructural;
- estudios de interacción.

Por ello, una buena anotación debería permitir rastrear la información hasta su evidencia original cuando sea posible.

---

# 7.3. Flujo de anotación bioinformática

## 7.3.1. El punto de partida

Un flujo de anotación puede comenzar con:

- una secuencia de ADN;
- una secuencia codificante;
- una proteína;
- un conjunto de genes;
- un genoma completo.

En este tema utilizaremos como ejemplo una proteína.

---

## 7.3.2. Paso 1. Verificar la secuencia

Antes de anotar conviene comprobar:

- identificador;
- organismo;
- longitud;
- integridad;
- procedencia.

Una secuencia incorrecta puede generar anotaciones incorrectas.

---

## 7.3.3. Paso 2. Buscar secuencias relacionadas

Podemos utilizar herramientas de comparación como BLAST.

El objetivo es identificar:

- proteínas similares;
- proteínas caracterizadas;
- posibles homólogos.

Aquí se reutilizan directamente los conocimientos del Bloque II.

---

## 7.3.4. Paso 3. Analizar dominios y firmas

La secuencia puede analizarse con recursos como InterPro para detectar:

- dominios;
- familias;
- sitios funcionales;
- regiones conservadas.

Esto permite obtener información independiente de la similitud global.

---

## 7.3.5. Paso 4. Consultar registros funcionales

A continuación podemos consultar:

- UniProt;
- Gene Ontology;
- Reactome;
- literatura científica;
- bases de conocimiento especializadas.

La información de varias fuentes puede complementar la interpretación.

---

## 7.3.6. Paso 5. Evaluar la evidencia

No todas las anotaciones tienen el mismo nivel de confianza.

Debemos distinguir:

- evidencia experimental;
- inferencia por homología;
- predicción automática;
- información revisada;
- información no revisada.

---

## 7.3.7. Paso 6. Formular una anotación

Una anotación responsable debe evitar afirmar más de lo que permiten los datos.

Es preferible escribir:

> “Proteína con un dominio compatible con…”

que afirmar una función concreta cuando la evidencia es insuficiente.

---

## 7.3.8. Paso 7. Documentar

Debemos conservar:

- identificadores;
- recursos consultados;
- fecha;
- versiones cuando estén disponibles;
- herramientas;
- parámetros;
- evidencias utilizadas.

Esto permite revisar y reproducir la anotación.

---

# 7.4. Un flujo resumido

```text
secuencia
   ↓
verificación
   ↓
búsqueda de homólogos
   ↓
dominios y familias
   ↓
fuentes funcionales
   ↓
evaluación de evidencias
   ↓
anotación
   ↓
documentación
```

---

# 7.5. Errores frecuentes

## Transferir automáticamente una función

Una secuencia parecida no garantiza función idéntica.

## Ignorar el nivel de evidencia

Una predicción no debe presentarse como si fuera un resultado experimental.

## Analizar únicamente la proteína completa

Puede existir un dominio conservado dentro de una proteína muy diferente.

## Utilizar una sola fuente

La integración de varias fuentes suele mejorar la interpretación.

## No registrar la procedencia

Una anotación sin trazabilidad es difícil de revisar.

## Confundir anotación con certeza

Una anotación puede cambiar cuando aparece nueva evidencia.

---

# 7.6. Cuestiones guía

1. ¿Qué diferencia existe entre anotación estructural y anotación funcional?
2. ¿Qué ventajas y limitaciones presenta la anotación automática?
3. ¿Por qué una alta similitud de secuencia no garantiza función idéntica?
4. ¿Qué información aporta un dominio proteico?
5. ¿Qué diferencia existe entre una familia y un motivo?
6. ¿Qué tipo de información podemos obtener de UniProt?
7. ¿Qué aporta InterPro?
8. ¿Por qué es importante conocer la evidencia de una anotación?
9. ¿Por qué conviene integrar varias fuentes?
10. ¿Qué información debería conservarse para que una anotación sea trazable?

---

# Ideas clave

- Anotar significa asociar significado biológico a datos moleculares.
- La anotación puede ser estructural o funcional.
- Puede basarse en evidencia experimental o inferencia computacional.
- La similitud de secuencia es una fuente de evidencia, no una garantía funcional.
- Dominios, motivos y familias ayudan a interpretar proteínas.
- UniProt, InterPro, Gene Ontology y recursos de rutas aportan información complementaria.
- Una buena anotación integra evidencias.
- La procedencia y el nivel de evidencia deben conservarse.
- La anotación es un proceso revisable y dinámico.

---

# Conexión con el siguiente tema

En este tema hemos trabajado la interpretación funcional de genes y proteínas individuales.

En el **Tema 8. Integración y explotación de información biológica** ampliaremos la escala y estudiaremos cómo organizar e integrar funciones mediante:

- ontologías biológicas;
- bases de conocimiento;
- análisis de enriquecimiento funcional.
