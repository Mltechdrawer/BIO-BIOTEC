# Práctica de Aula 4. Recuperación de información mediante varios recursos bioinformáticos

## Duración

**1 hora**

Esta práctica se realiza después de completar el Tema 2 y se centra en el uso de:

- NCBI;
- EMBL-EBI;
- UniProt;
- PDB;
- referencias bibliográficas y referencias cruzadas.

---

## Objetivos

Al finalizar la práctica, el estudiante será capaz de:

- Seleccionar el recurso más adecuado en función del tipo de información buscada.
- Recuperar información sobre una misma entidad biológica utilizando varios recursos.
- Relacionar identificadores procedentes de bases de datos diferentes.
- Diferenciar información sobre genes, secuencias, proteínas, estructuras y publicaciones.
- Evaluar el nivel de evidencia asociado a la información recuperada.
- Mantener la trazabilidad del recorrido seguido entre diferentes recursos.
- Elaborar una respuesta bioinformática basada en varias fuentes.

---

## Contexto

Una pregunta biológica rara vez se responde utilizando un único recurso.

La información sobre una entidad puede estar distribuida entre distintas bases de datos:

**gen → secuencia → proteína → función → estructura → publicación**

El objetivo de esta práctica es realizar un pequeño recorrido por el ecosistema bioinformático y comprobar cómo diferentes recursos aportan distintas capas de información.

---

# Caso de estudio

El profesorado asignará a cada estudiante, pareja o grupo una **entidad biológica**: por ejemplo, un gen o una proteína.

A partir de esa entidad deberá construirse un recorrido entre diferentes recursos bioinformáticos.

El objetivo no es recopilar toda la información disponible, sino seleccionar únicamente aquella que permita responder de forma razonada a las preguntas planteadas.

---

# Tarea 1. Definir la pregunta

Antes de comenzar la búsqueda, formula una pregunta concreta.

Ejemplos de estructura:

> ¿Qué información básica se conoce sobre esta entidad y qué recursos permiten relacionar su secuencia, función, estructura y literatura científica?

o bien:

> ¿Qué evidencias permiten relacionar este gen con una proteína concreta y con una estructura tridimensional conocida?

Escribe tu pregunta:

**Pregunta de trabajo:**  
...

---

# Tarea 2. Recuperación inicial

Utiliza uno de los grandes recursos generales, como NCBI o EMBL-EBI, para localizar la entidad.

Registra:

**Recurso utilizado:**  
...

**Término de búsqueda:**  
...

**Identificador del registro seleccionado:**  
...

**Organismo:**  
...

**Tipo de entidad:**  
...

**Descripción:**  
...

### Verificación

Antes de continuar, responde:

1. ¿Cómo has comprobado que el registro corresponde a la entidad correcta?
2. ¿Qué elemento ha resultado más útil: nombre, organismo, descripción o identificador?
3. ¿Existen registros similares que podrían provocar confusión?

---

# Tarea 3. Relación con una proteína

Si la entidad inicial es un gen, localiza la proteína asociada.

Si la entidad inicial es una proteína, localiza el gen correspondiente cuando sea posible.

Utiliza UniProt cuando resulte adecuado.

Registra:

**Identificador UniProt:**  
...

**Nombre de la proteína:**  
...

**Gen asociado:**  
...

**Organismo:**  
...

**Estado de revisión:**  
...

**Función principal:**  
...

**Una referencia bibliográfica asociada:**  
...

### Pregunta

> ¿Qué parte de la información funcional parece estar curada y qué parte podría proceder de anotación automática?

---

# Tarea 4. Relación con información estructural

Comprueba si existe información estructural asociada.

Utiliza PDB cuando corresponda.

Registra:

**Identificador PDB:**  
...

**Macromolécula representada:**  
...

**Método experimental:**  
...

**Cadenas:**  
...

**Ligandos u otras moléculas relevantes:**  
...

**Publicación asociada:**  
...

Si no existe una estructura experimental disponible, indícalo expresamente.

### Pregunta

> ¿Qué diferencia existe entre afirmar que una estructura ha sido determinada experimentalmente y afirmar que existe un modelo computacional?

---

# Tarea 5. Construir el recorrido de identificadores

Representa el recorrido seguido mediante un esquema.

Ejemplo:

**Nombre inicial → identificador del gen → identificador de proteína → identificador estructural → publicación**

Completa:

```text
Entidad inicial:
    ↓
Recurso 1:
    ↓
Identificador:
    ↓
Recurso 2:
    ↓
Identificador:
    ↓
Recurso 3:
    ↓
Identificador:
```

El esquema debe permitir que otra persona pueda repetir el mismo recorrido.

---

# Tarea 6. Tabla de trazabilidad

Completa la tabla:

| Información utilizada | Recurso | Identificador | Evidencia / procedencia |
|---|---|---|---|
| Gen o entidad inicial | | | |
| Secuencia | | | |
| Función | | | |
| Proteína | | | |
| Estructura | | | |
| Publicación | | | |

Si alguna categoría no está disponible, indícalo.

---

# Tarea 7. Respuesta final

Redacta un texto breve, de aproximadamente **150–200 palabras**, que responda a la pregunta inicial.

La respuesta debe:

1. identificar claramente la entidad;
2. integrar información procedente de al menos dos recursos;
3. incluir los identificadores relevantes;
4. diferenciar información experimental de información anotada o inferida cuando corresponda;
5. citar al menos una publicación científica asociada;
6. indicar cualquier limitación encontrada.

---

## Entregable

El documento final debe contener:

1. Pregunta de trabajo.
2. Registro inicial y justificación de su selección.
3. Información recuperada de UniProt, cuando proceda.
4. Información estructural de PDB, cuando exista.
5. Esquema de identificadores.
6. Tabla de trazabilidad.
7. Respuesta final de 150–200 palabras.

La extensión orientativa es de **2 páginas**.

---

## Criterios de realización

Se valorará:

- la selección adecuada de los recursos;
- la correcta identificación de la entidad;
- la coherencia entre los distintos identificadores;
- la distinción entre diferentes niveles de evidencia;
- la trazabilidad del proceso;
- la capacidad para sintetizar información procedente de varias fuentes;
- y la claridad de la respuesta final.

No se busca recopilar grandes cantidades de información, sino demostrar que el estudiante sabe **navegar entre recursos y construir una respuesta verificable**.

---

## Uso de inteligencia artificial

Puede utilizarse una herramienta de IA como apoyo para:

- proponer términos de búsqueda;
- explicar campos del registro;
- ayudar a interpretar terminología;
- o revisar la claridad del texto final.

Sin embargo:

- los identificadores deben comprobarse directamente en las bases de datos;
- las funciones deben verificarse en el recurso correspondiente;
- las publicaciones deben existir y estar relacionadas con la entidad;
- y cualquier uso de IA debe declararse expresamente.

La IA no se considera una fuente científica.

---

## Preguntas de cierre

1. ¿Qué recurso ha resultado más útil como punto de partida?
2. ¿Qué recurso ha proporcionado la información más interpretada?
3. ¿Qué tipo de información ha sido más difícil de relacionar?
4. ¿Has encontrado identificadores diferentes para la misma entidad?
5. ¿Qué problema podría producirse si no se registraran los identificadores utilizados?

---

## Idea clave

> **La recuperación de información bioinformática no consiste en consultar una única base de datos, sino en construir un recorrido reproducible entre recursos, identificadores, evidencias y publicaciones.**
