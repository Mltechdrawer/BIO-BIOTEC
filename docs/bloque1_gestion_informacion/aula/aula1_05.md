# Práctica de Aula 5. Representación, calidad y trazabilidad de datos biológicos

## Duración

**1 hora**

Esta práctica cierra el **Bloque I. Gestión de información biológica y recursos bioinformáticos** y se realiza después de completar el Tema 3.

Se trabajarán de forma integrada los contenidos relacionados con:

- formatos FASTA, GenBank y PDB;
- metadatos y anotación;
- calidad de los datos;
- interoperabilidad;
- reutilización;
- trazabilidad;
- y principios FAIR.

---

## Objetivos

Al finalizar la práctica, el estudiante será capaz de:

- Reconocer qué información contiene y qué información omite cada formato bioinformático.
- Comparar distintas representaciones de una misma entidad biológica.
- Diferenciar entre secuencia, metadatos y anotación.
- Identificar pérdidas de información producidas al transformar datos entre formatos.
- Evaluar la trazabilidad y reutilización de un conjunto de datos biológicos.
- Aplicar criterios básicos de calidad e interoperabilidad.
- Documentar un pequeño flujo de gestión de datos de forma reproducible.

---

## Contexto

En las prácticas anteriores se ha trabajado cómo localizar información en bases de datos y cómo relacionar registros procedentes de distintos recursos.

El último paso del Bloque I consiste en analizar **cómo se representa y conserva esa información**.

Una misma entidad biológica puede aparecer de distintas formas:

- como secuencia FASTA;
- como registro GenBank;
- como registro de proteína;
- como estructura PDB;
- o como información integrada en una base de datos.

Estas representaciones no son equivalentes.

Cada una conserva determinados elementos y omite otros.

Por ello, gestionar correctamente un dato implica saber:

> **qué información contiene, qué contexto necesita y qué debemos conservar para poder reutilizarlo más adelante.**

---

# Caso de estudio

El profesorado proporcionará un pequeño conjunto de datos relacionado con una entidad biológica.

El conjunto incluirá, cuando sea posible:

- una secuencia en formato FASTA;
- un registro GenBank o equivalente;
- información asociada a una proteína;
- y un registro estructural o fragmento de información PDB.

El objetivo será comparar las representaciones y evaluar qué información se conserva en cada una.

---

# Tarea 1. Identificar los componentes del dato

Para cada representación, indica:

1. Qué entidad representa.
2. Qué identificador utiliza.
3. Si contiene secuencia.
4. Si contiene metadatos.
5. Si contiene anotaciones.
6. Si contiene referencias bibliográficas.
7. Si contiene información de versión o actualización.
8. Si contiene referencias cruzadas.

### Tabla de trabajo

| Representación | Entidad | Secuencia | Metadatos | Anotaciones | Referencias | Versión | Referencias cruzadas |
|---|---|---|---|---|---|---|---|
| FASTA | | | | | | | |
| GenBank | | | | | | | |
| PDB / registro estructural | | | | | | | |

---

# Tarea 2. FASTA frente a GenBank

Compara la representación FASTA con el registro GenBank correspondiente.

Responde:

1. ¿Qué información aparece en ambos?
2. ¿Qué información aparece únicamente en GenBank?
3. ¿Qué información se pierde si convertimos GenBank a FASTA?
4. ¿Qué ventajas ofrece FASTA para el procesamiento automático?
5. ¿En qué situación preferirías conservar el registro GenBank completo?
6. ¿Qué información adicional deberías guardar junto al fichero FASTA para mantener la trazabilidad?

---

# Tarea 3. Dato, metadato y anotación

Selecciona al menos seis elementos del registro analizado y clasifícalos como:

- **dato**;
- **metadato**;
- **anotación**.

### Tabla

| Elemento | Clasificación | Justificación |
|---|---|---|
| | Dato / Metadato / Anotación | |
| | Dato / Metadato / Anotación | |
| | Dato / Metadato / Anotación | |
| | Dato / Metadato / Anotación | |
| | Dato / Metadato / Anotación | |
| | Dato / Metadato / Anotación | |

Después responde:

> ¿Puede una anotación convertirse en un dato de entrada para otro análisis? Explica brevemente tu respuesta.

---

# Tarea 4. Calidad del dato

Evalúa el conjunto proporcionado utilizando los siguientes criterios:

### Completitud

- ¿Falta alguna información necesaria?
- ¿La secuencia está completa?
- ¿Existen campos vacíos o no disponibles?

### Consistencia

- ¿Coinciden organismo, identificadores y descripción entre recursos?
- ¿Existen diferencias que deban aclararse?

### Procedencia

- ¿Puede determinarse de dónde procede cada dato?
- ¿Se conoce el recurso de origen?

### Evidencia

- ¿Qué información es experimental?
- ¿Qué información está anotada o predicha?

### Actualización

- ¿Se conoce la versión o fecha de actualización?

Resume la evaluación en una tabla:

| Criterio | Valoración | Evidencia encontrada |
|---|---|---|
| Completitud | | |
| Consistencia | | |
| Procedencia | | |
| Evidencia | | |
| Actualización | | |

---

# Tarea 5. Trazabilidad

Imagina que vas a utilizar la secuencia proporcionada en un análisis bioinformático.

Indica qué información conservarías para que otra persona pudiera repetir tu trabajo.

Como mínimo, considera:

- recurso de origen;
- identificador;
- versión;
- organismo;
- fecha de descarga;
- formato;
- descripción;
- transformación realizada;
- herramienta utilizada;
- parámetros relevantes.

Completa:

```text
Recurso de origen:
Identificador:
Versión:
Organismo:
Fecha de descarga:
Formato original:
Formato utilizado en el análisis:
Transformaciones realizadas:
Herramienta:
Parámetros:
Observaciones:
```

---

# Tarea 6. Interoperabilidad

Observa los identificadores asociados a la entidad estudiada.

Identifica al menos dos relaciones entre recursos.

Ejemplo:

```text
GenBank accession
      ↓
UniProt accession
      ↓
PDB ID
```

Responde:

1. ¿Se utiliza el mismo identificador en todos los recursos?
2. ¿Cómo se establece la relación entre ellos?
3. ¿Qué ocurriría si se conservara únicamente uno de los identificadores sin indicar su base de datos?
4. ¿Por qué las referencias cruzadas favorecen la interoperabilidad?

---

# Tarea 7. Evaluación FAIR

Valora brevemente el conjunto de datos según los principios FAIR.

## Findable

¿Dispone de identificadores y metadatos que permitan localizarlo?

**Valoración:**  
...

## Accessible

¿Puede recuperarse desde un recurso claramente identificado?

**Valoración:**  
...

## Interoperable

¿Utiliza formatos e identificadores que permiten relacionarlo con otros recursos?

**Valoración:**  
...

## Reusable

¿Dispone de suficiente contexto, procedencia y documentación para reutilizarlo?

**Valoración:**  
...

---

# Tarea 8. Decisión final

Imagina que debes entregar a otro grupo de investigación los datos utilizados para continuar el análisis.

Dispones de tres opciones:

### Opción A

Entregar únicamente el fichero FASTA.

### Opción B

Entregar FASTA y una captura de pantalla del registro original.

### Opción C

Entregar FASTA junto con identificador, versión, recurso de origen, metadatos relevantes y documentación del procedimiento utilizado.

Selecciona una opción y justifica tu elección en un máximo de 100 palabras.

---

## Entregable

El documento final debe incluir:

1. Tabla comparativa de representaciones.
2. Comparación FASTA/GenBank.
3. Clasificación de dato, metadato y anotación.
4. Evaluación de calidad.
5. Ficha de trazabilidad.
6. Relaciones entre identificadores.
7. Valoración FAIR.
8. Decisión final justificada.

La extensión orientativa es de **2 páginas**.

---

## Criterios de realización

Se valorará:

- la correcta interpretación de los formatos;
- la distinción entre dato, metadato y anotación;
- la identificación de información perdida entre representaciones;
- la calidad de la documentación;
- la capacidad para mantener la trazabilidad;
- la comprensión de la interoperabilidad;
- y la justificación de las decisiones tomadas.

No se valorará la copia literal de campos, sino la capacidad para explicar **qué información es necesaria para comprender y reutilizar un dato biológico**.

---

## Preguntas de cierre

1. ¿Por qué FASTA es adecuado para muchos análisis pero insuficiente para documentar completamente un dato?
2. ¿Qué diferencia existe entre formato y significado biológico?
3. ¿Qué elemento de la trazabilidad consideras más importante?
4. ¿Qué problema puede producir una conversión de formatos?
5. ¿Por qué los principios FAIR son relevantes en Bioinformática?

---

## Cierre del Bloque I

Con esta práctica se completa el Bloque I.

Las cinco prácticas de aula han seguido la secuencia:

1. Leer y comprender literatura científica.
2. Utilizar correctamente artículos científicos.
3. Comprender bases de datos y registros.
4. Recuperar información entre varios recursos.
5. Representar, documentar y reutilizar datos.

La lógica global del bloque puede resumirse así:

> **buscar → evaluar → recuperar → relacionar → representar → documentar → reutilizar**

Estas competencias se utilizarán a partir del Bloque II, donde comenzaremos a trabajar con métodos computacionales para comparar y analizar secuencias.
