# Tema 10. Recursos computacionales para el análisis estructural

## Duración

**1 hora de teoría**

Este tema abre el **Bloque IV. Bioinformática estructural y modelado computacional**.

De acuerdo con la estructura del curso, se organiza en dos apartados:

- **10.1. Bases de datos estructurales.**
- **10.2. Representación digital de biomoléculas.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar qué información aporta una estructura biomolecular.
- Identificar los principales recursos utilizados para consultar estructuras tridimensionales.
- Diferenciar estructuras experimentales de modelos computacionales.
- Interpretar la información básica de un registro estructural.
- Comprender cómo se representa digitalmente una biomolécula.
- Reconocer la diferencia entre secuencia, coordenadas atómicas y representación tridimensional.
- Identificar cadenas, residuos, átomos, ligandos y ensamblajes biológicos.
- Comprender la importancia de los formatos estructurales y de los metadatos asociados.

---

# Introducción

Hasta ahora hemos trabajado principalmente con secuencias, anotaciones y relaciones funcionales.

En este bloque cambiaremos de nivel.

Pasaremos de preguntas como:

> **¿qué secuencia es esta?**

o:

> **¿qué función puede tener esta proteína?**

a preguntas como:

> **¿qué forma tridimensional adopta esta biomolécula?**

y:

> **¿cómo se relaciona esa estructura con su función?**

La estructura tridimensional es fundamental porque muchas funciones biológicas dependen directamente de la forma.

Por ejemplo:

- una enzima necesita una geometría concreta en su sitio activo;
- una proteína receptora debe reconocer determinadas moléculas;
- un anticuerpo depende de la forma de sus regiones de unión;
- una proteína de membrana necesita una organización compatible con la bicapa;
- un complejo molecular necesita superficies de interacción adecuadas.

La Bioinformática estructural permite almacenar, consultar, representar, visualizar y analizar este tipo de información mediante recursos computacionales.

---

# 10.1. Bases de datos estructurales

## 10.1.1. Qué contiene una base de datos estructural

Una base de datos estructural almacena información sobre la organización tridimensional de biomoléculas.

Puede incluir:

- proteínas;
- ADN;
- ARN;
- complejos proteína-proteína;
- complejos proteína-ADN;
- complejos con ligandos;
- complejos con fármacos;
- otras macromoléculas biológicas.

La información puede incluir tanto la estructura propiamente dicha como metadatos asociados.

---

## 10.1.2. El Protein Data Bank

El **Protein Data Bank (PDB)** es el archivo internacional de referencia para estructuras tridimensionales de macromoléculas biológicas.

Cada estructura depositada dispone de un identificador PDB.

Ejemplo clásico:

```text
4HHB
```

corresponde a una estructura de hemoglobina humana.

Uno de los portales de consulta más utilizados es:

https://www.rcsb.org/

---

## 10.1.3. Qué podemos encontrar en un registro PDB

Un registro estructural puede contener:

- identificador;
- título;
- biomolécula;
- organismo;
- autores;
- publicación asociada;
- método experimental;
- resolución, cuando procede;
- cadenas;
- secuencias;
- ligandos;
- iones;
- moléculas de agua;
- coordenadas atómicas;
- ensamblajes biológicos;
- referencias cruzadas.

Por tanto, un registro PDB es mucho más que una imagen tridimensional.

---

## 10.1.4. Estructura y evidencia experimental

Una estructura depositada en PDB suele proceder de un método experimental de determinación estructural.

Entre los principales métodos se encuentran:

- **cristalografía de rayos X**;
- **microscopía electrónica criogénica (cryo-EM)**;
- **resonancia magnética nuclear (NMR)**.

Cada método produce datos con características diferentes.

No es necesario estudiar aquí su fundamento físico en detalle, pero sí comprender que la estructura observada depende del método y de la calidad de los datos experimentales.

---

## 10.1.5. Cristalografía de rayos X

Ha sido históricamente uno de los métodos más utilizados.

Requiere obtener cristales de la molécula o complejo. A partir del patrón de difracción se reconstruye un modelo estructural.

Una característica importante es la **resolución**.

De forma general:

> **menor valor numérico de resolución → mayor nivel de detalle**

Por ejemplo, una estructura a 1,5 Å suele ofrecer más detalle que una estructura a 3,5 Å.

Sin embargo, la calidad de una estructura no debe evaluarse únicamente con una cifra.

---

## 10.1.6. Cryo-EM

La microscopía electrónica criogénica ha adquirido gran importancia en los últimos años.

Permite estudiar especialmente bien:

- grandes complejos;
- proteínas de membrana;
- ensamblajes macromoleculares.

No requiere cristalización de la misma forma que la cristalografía de rayos X.

El resultado final también es un modelo estructural derivado de datos experimentales.

---

## 10.1.7. NMR

La resonancia magnética nuclear puede utilizarse para estudiar estructuras de biomoléculas en solución.

En algunos casos, el resultado no es una única conformación, sino un conjunto de modelos compatibles con los datos experimentales.

Esto es importante porque una proteína no siempre debe imaginarse como una estructura completamente rígida.

---

## 10.1.8. Estructuras experimentales y modelos computacionales

En este bloque debemos mantener una distinción clara entre:

### Estructura experimental

Se obtiene a partir de datos físicos medidos experimentalmente.

### Modelo computacional

Se obtiene mediante métodos de predicción o modelado.

Ambos pueden visualizarse de forma tridimensional, pero no representan el mismo nivel de evidencia.

Esta diferencia será esencial en el Tema 12.

---

## 10.1.9. RCSB PDB

RCSB PDB permite:

- buscar estructuras;
- consultar metadatos;
- visualizar modelos;
- examinar secuencias;
- identificar ligandos;
- analizar ensamblajes;
- descargar ficheros estructurales.

Puede realizarse una búsqueda mediante:

- identificador PDB;
- nombre de proteína;
- organismo;
- autor;
- ligando;
- secuencia;
- palabras clave.

---

## 10.1.10. PDBe y PDBj

El archivo PDB es gestionado internacionalmente a través del **Worldwide Protein Data Bank (wwPDB)**.

Entre sus principales portales se encuentran:

- **RCSB PDB**
- **PDBe**
- **PDBj**

Estos recursos acceden al mismo archivo estructural internacional, aunque presentan interfaces y herramientas diferentes.

---

# 10.2. Representación digital de biomoléculas

## 10.2.1. Una estructura como conjunto de coordenadas

Una biomolécula tridimensional puede representarse computacionalmente mediante las coordenadas de sus átomos.

Para cada átomo podemos almacenar aproximadamente:

```text
átomo
residuo
cadena
x
y
z
```

Por ejemplo:

```text
CA  ALA  A  12.5  8.1  3.4
```

Las coordenadas `x`, `y` y `z` determinan la posición del átomo en el espacio tridimensional.

---

## 10.2.2. Jerarquía estructural

Una estructura puede entenderse como una jerarquía:

```text
estructura
   ↓
cadenas
   ↓
residuos
   ↓
átomos
```

Esta organización permite seleccionar y analizar partes concretas de una biomolécula.

---

## 10.2.3. Átomos

El nivel más detallado de la representación estructural corresponde a los átomos.

Cada átomo puede tener información asociada:

- tipo;
- elemento químico;
- residuo al que pertenece;
- cadena;
- coordenadas;
- ocupación;
- factor de temperatura.

---

## 10.2.4. Residuos

Los átomos se agrupan en residuos.

En una proteína, cada residuo corresponde normalmente a un aminoácido.

Por ejemplo:

```text
ALA
GLY
LYS
TRP
```

En ADN o ARN los residuos corresponden a nucleótidos.

---

## 10.2.5. Cadenas

Las estructuras pueden contener una o varias cadenas.

Una cadena puede representar:

- una proteína;
- una parte de una proteína;
- un ácido nucleico;
- una subunidad de un complejo.

Es importante no asumir que:

> **una entrada PDB = una única proteína**

Muchos registros representan complejos con varias cadenas.

---

## 10.2.6. Ligandos

Una estructura puede contener moléculas que no forman parte de la cadena principal.

Por ejemplo:

- ATP;
- NAD;
- iones;
- inhibidores;
- fármacos;
- cofactores;
- sustratos.

Estas moléculas se denominan frecuentemente **ligandos**.

Su posición puede ser especialmente importante para interpretar la función.

---

## 10.2.7. Moléculas de agua

Los ficheros estructurales pueden incluir moléculas de agua.

No son necesariamente ruido.

Algunas participan en:

- estabilización;
- puentes de hidrógeno;
- reconocimiento molecular;
- interacción con ligandos.

---

## 10.2.8. Unidad asimétrica y ensamblaje biológico

Un concepto importante es distinguir entre:

### Unidad asimétrica

Contenido estructural determinado en el experimento cristalográfico o depositado según el método.

### Ensamblaje biológico

Organización molecular que se considera biológicamente relevante.

En algunos casos ambas coinciden.

En otros, el ensamblaje funcional contiene varias copias o combinaciones de cadenas.

Por ello, al estudiar una proteína oligomérica no basta con observar cualquier representación disponible.

---

## 10.2.9. Formato PDB tradicional

Durante décadas se utilizó ampliamente el formato de texto denominado **PDB**.

Una línea típica podía contener información como:

```text
ATOM      1  N   VAL A   1      11.104  13.207   2.100
```

Este formato es relativamente sencillo de leer visualmente.

Sin embargo, tiene limitaciones heredadas de su diseño original.

---

## 10.2.10. PDBx/mmCIF

El formato moderno principal para los datos del PDB es **PDBx/mmCIF**.

Permite representar estructuras mucho más grandes y metadatos más complejos.

Su organización utiliza categorías y atributos.

Ejemplo conceptual:

```text
_atom_site.label_atom_id
_atom_site.label_comp_id
_atom_site.Cartn_x
_atom_site.Cartn_y
_atom_site.Cartn_z
```

El formato PDBx/mmCIF es actualmente la referencia para el archivo estructural.

---

## 10.2.11. Por qué evolucionan los formatos

Las estructuras actuales pueden contener:

- cientos de cadenas;
- millones de átomos;
- grandes complejos;
- numerosos ligandos;
- metadatos extensos.

Los formatos antiguos no fueron diseñados para esa escala.

Por ello, la representación digital también debe evolucionar.

---

## 10.2.12. Del fichero a la imagen

Un fichero estructural no contiene una “fotografía” de la proteína.

Contiene datos.

El software de visualización interpreta esos datos y genera una representación.

Podemos representar la misma estructura de muchas formas:

- átomos;
- bolas y varillas;
- líneas;
- superficie;
- cartoon;
- ribbon;
- representación de hélices y láminas.

Por tanto:

> **estructura digital y representación visual no son exactamente lo mismo**

---

# 10.3. Niveles de representación de proteínas

Para interpretar estructuras conviene recordar los niveles clásicos:

## Estructura primaria

Secuencia de aminoácidos.

## Estructura secundaria

Patrones locales como:

- hélices alfa;
- láminas beta;
- giros.

## Estructura terciaria

Organización tridimensional completa de una cadena.

## Estructura cuaternaria

Organización de varias cadenas o subunidades.

La Bioinformática estructural trabaja especialmente con los niveles tridimensionales, pero estos dependen de la secuencia.

---

# 10.4. Metadatos estructurales

Una estructura debe interpretarse junto con sus metadatos.

Entre los más importantes:

- método experimental;
- resolución;
- organismo;
- cadenas;
- mutaciones;
- ligandos;
- condiciones experimentales;
- publicación asociada;
- fecha;
- ensamblaje biológico.

Dos estructuras de una misma proteína pueden representar situaciones diferentes.

Por ejemplo:

- proteína libre;
- proteína unida a un ligando;
- proteína mutante;
- proteína en complejo;
- proteína de otra especie.

---

# 10.5. Ejemplo conceptual

Supongamos que buscamos una enzima en PDB.

Encontramos tres estructuras:

### Estructura A

```text
proteína sin ligando
```

### Estructura B

```text
proteína + sustrato
```

### Estructura C

```text
proteína + inhibidor
```

Las tres corresponden a la misma proteína, pero aportan información diferente.

La estructura B puede ayudar a identificar el sitio activo.

La estructura C puede ayudar a estudiar interacción con un compuesto.

La comparación entre ellas puede mostrar cambios conformacionales.

Por ello, elegir una estructura no consiste únicamente en seleccionar el primer resultado.

---

# 10.6. Del registro estructural al análisis

Un flujo básico puede ser:

```text
identificar proteína
      ↓
buscar en PDB
      ↓
seleccionar estructura
      ↓
revisar método y calidad
      ↓
identificar cadenas y ligandos
      ↓
descargar/visualizar
      ↓
analizar
```

La selección correcta de la estructura condicionará cualquier análisis posterior.

---

# 10.7. Errores frecuentes

## Pensar que PDB contiene únicamente proteínas

También incluye ácidos nucleicos y complejos biomoleculares.

## Confundir estructura experimental con modelo computacional

Ambos pueden visualizarse en 3D, pero su origen y evidencia son diferentes.

## Elegir la primera estructura disponible

Puede no ser la más adecuada para la pregunta biológica.

## Ignorar ligandos y cadenas

Pueden ser esenciales para interpretar la función.

## Interpretar una estructura como una fotografía fija

Las biomoléculas son dinámicas y una estructura representa un estado determinado.

## Confundir fichero y visualización

El fichero almacena datos estructurales; el programa decide cómo representarlos gráficamente.

## Ignorar el ensamblaje biológico

La unidad mostrada inicialmente puede no corresponder al complejo funcional.

---

# 10.8. Cuestiones guía

1. ¿Qué información aporta una estructura tridimensional que no aporta directamente una secuencia?
2. ¿Qué es el Protein Data Bank?
3. ¿Qué diferencia existe entre estructura experimental y modelo computacional?
4. ¿Qué métodos experimentales se utilizan habitualmente para determinar estructuras?
5. ¿Qué significa la resolución en cristalografía?
6. ¿Por qué una entrada PDB puede contener varias cadenas?
7. ¿Qué información puede aportar un ligando?
8. ¿Qué diferencia existe entre unidad asimétrica y ensamblaje biológico?
9. ¿Qué representa una coordenada atómica?
10. ¿Qué diferencia existe entre formato PDB y PDBx/mmCIF?
11. ¿Por qué no debe interpretarse una estructura como una fotografía estática definitiva?
12. ¿Qué metadatos revisarías antes de seleccionar una estructura para un análisis?

---

# Ideas clave

- La Bioinformática estructural estudia la representación, consulta y análisis computacional de estructuras biomoleculares.
- PDB es el archivo internacional de referencia para estructuras macromoleculares.
- Las estructuras experimentales pueden proceder de cristalografía, cryo-EM o NMR.
- Una estructura digital se representa mediante coordenadas y metadatos.
- Las estructuras se organizan en cadenas, residuos y átomos.
- Los ligandos y ensamblajes pueden ser fundamentales para interpretar la función.
- PDBx/mmCIF es el formato moderno principal del archivo PDB.
- El fichero estructural contiene datos; la visualización es una representación de esos datos.
- Una misma proteína puede tener múltiples estructuras que representan estados diferentes.
- La selección de una estructura debe responder a una pregunta biológica concreta.

---

# Conexión con el siguiente tema

En este tema hemos aprendido dónde se almacenan las estructuras biomoleculares y cómo se representan digitalmente.

En el **Tema 11. Visualización y análisis de estructuras biomoleculares** estudiaremos cómo utilizar esas representaciones para:

- explorar modelos tridimensionales;
- visualizar elementos estructurales;
- analizar superficies y regiones;
- estudiar interacciones moleculares.
