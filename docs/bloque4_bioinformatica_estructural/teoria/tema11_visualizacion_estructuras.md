# Tema 11. Visualización y análisis de estructuras biomoleculares

## Duración

**2 horas de teoría**

Este tema forma parte del **Bloque IV. Bioinformática estructural y modelado computacional**.

De acuerdo con la estructura del curso, se organiza en tres apartados:

- **11.1. Modelos tridimensionales.**
- **11.2. Herramientas de visualización.**
- **11.3. Análisis de interacciones moleculares.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Interpretar una estructura biomolecular en tres dimensiones.
- Diferenciar entre distintas representaciones gráficas de una misma estructura.
- Identificar elementos de estructura secundaria y organización cuaternaria.
- Comprender qué información aporta una superficie molecular.
- Seleccionar una representación adecuada según la pregunta biológica.
- Reconocer las principales herramientas de visualización estructural.
- Identificar interacciones no covalentes relevantes entre biomoléculas.
- Interpretar contactos proteína-ligando y proteína-proteína.
- Comprender las limitaciones de una estructura estática y de un análisis exclusivamente visual.

---

# Introducción

En el Tema 10 vimos que una estructura biomolecular puede representarse digitalmente mediante coordenadas atómicas y metadatos.

Sin embargo, disponer de esas coordenadas no significa comprender automáticamente la estructura.

Un fichero estructural puede contener miles o incluso millones de posiciones atómicas. Para interpretar esa información necesitamos transformar los datos en representaciones visuales que permitan responder preguntas concretas.

Por ejemplo:

- ¿qué forma general tiene la proteína?
- ¿dónde se encuentran las hélices y las láminas?
- ¿qué residuos forman un sitio activo?
- ¿qué cadenas participan en un complejo?
- ¿dónde se une un ligando?
- ¿qué contactos estabilizan una interacción?
- ¿qué región está expuesta al solvente?

La visualización molecular no es, por tanto, un recurso meramente ilustrativo.

Es una herramienta de análisis.

---

# 11.1. Modelos tridimensionales

## 11.1.1. De las coordenadas al modelo visual

En un fichero estructural podemos encontrar coordenadas como:

```text
x, y, z
```

para cada átomo.

El programa de visualización utiliza esas coordenadas para reconstruir la posición relativa de los átomos y representar la molécula en el espacio.

Podemos pensar en el proceso como:

```text
coordenadas atómicas
        ↓
modelo geométrico
        ↓
representación gráfica
        ↓
interpretación biológica
```

La representación final depende de las decisiones del usuario.

---

## 11.1.2. Una estructura admite múltiples representaciones

No existe una única forma correcta de representar una molécula.

La misma proteína puede visualizarse como:

- líneas;
- sticks;
- bolas y varillas;
- esferas;
- cartoon;
- ribbon;
- superficie molecular;
- combinación de varias representaciones.

Cada una destaca información diferente.

---

## 11.1.3. Representación por líneas

La representación mediante líneas muestra enlaces de forma sencilla.

Ventajas:

- poco coste visual;
- permite ver muchos átomos;
- útil para inspecciones rápidas.

Limitaciones:

- puede resultar difícil interpretar estructuras grandes;
- no muestra bien el volumen real de los átomos.

---

## 11.1.4. Sticks y bolas y varillas

En una representación de **sticks**, los enlaces aparecen como cilindros.

En una representación de **balls and sticks**, los átomos se representan mediante esferas y los enlaces mediante cilindros.

Es útil para:

- observar ligandos;
- estudiar sitios activos;
- identificar geometría local;
- analizar contactos.

No es la mejor representación para comprender rápidamente la forma global de una proteína grande.

---

## 11.1.5. Representación de esferas

Los átomos pueden representarse como esferas aproximando su volumen.

Esta representación permite observar:

- ocupación espacial;
- empaquetamiento;
- accesibilidad;
- complementariedad.

Puede ser útil para estudiar contactos estrechos o el volumen ocupado por una región.

---

## 11.1.6. Cartoon y ribbon

Las representaciones **cartoon** o **ribbon** simplifican la cadena principal y resaltan elementos de estructura secundaria.

Por ejemplo:

- hélices alfa;
- láminas beta;
- bucles.

Son especialmente útiles para comprender:

- plegamiento;
- dominios;
- organización global;
- relaciones entre subunidades.

Por este motivo son muy habituales en figuras científicas.

---

## 11.1.7. Estructura secundaria

En una proteína pueden distinguirse elementos como:

### Hélices alfa

Regiones helicoidales estabilizadas por puentes de hidrógeno internos.

### Láminas beta

Formadas por varias hebras beta asociadas.

### Giros y bucles

Conectan elementos de estructura secundaria y pueden participar en reconocimiento o unión.

La distribución de estos elementos ayuda a caracterizar el plegamiento de una proteína.

---

## 11.1.8. Dominios estructurales

Una proteína puede contener regiones estructurales relativamente independientes denominadas **dominios**.

Un dominio puede:

- plegarse de forma relativamente autónoma;
- tener una función concreta;
- aparecer conservado en distintas proteínas.

La visualización permite observar si una proteína presenta:

- un único dominio;
- varios dominios;
- regiones flexibles entre dominios.

---

## 11.1.9. Estructura cuaternaria

Muchas proteínas funcionales están formadas por varias cadenas.

Por ejemplo:

```text
cadena A + cadena B
```

o:

```text
A + B + C + D
```

La visualización tridimensional permite estudiar:

- cómo se organizan las subunidades;
- qué superficies están en contacto;
- si existe simetría;
- qué ligandos aparecen en las interfaces.

---

## 11.1.10. Colorear para interpretar

El color es una herramienta analítica.

Una estructura puede colorearse por:

- cadena;
- elemento de estructura secundaria;
- dominio;
- residuo;
- propiedad química;
- conservación;
- carga;
- confianza del modelo.

Por ejemplo, colorear cada cadena de forma diferente puede revelar rápidamente la organización de un complejo.

El color debe elegirse para responder a una pregunta, no únicamente por razones estéticas.

---

## 11.1.11. Superficie molecular

Una representación de superficie muestra el volumen externo de la molécula.

Puede ser útil para estudiar:

- cavidades;
- canales;
- sitios de unión;
- interfaces;
- accesibilidad al solvente.

Una superficie puede revelar características difíciles de observar con cartoon o sticks.

---

## 11.1.12. Propiedades sobre la superficie

Sobre una superficie pueden representarse propiedades como:

- carga electrostática;
- hidrofobicidad;
- conservación;
- accesibilidad.

Esto permite relacionar forma y propiedades químicas.

Por ejemplo, una cavidad con determinadas características puede ser compatible con la unión de un ligando.

---

# 11.2. Herramientas de visualización

## 11.2.1. Visualización en el navegador

Actualmente muchas bases de datos estructurales incorporan visores tridimensionales en el navegador.

Esto permite:

- rotar la molécula;
- hacer zoom;
- seleccionar cadenas;
- mostrar ligandos;
- cambiar representaciones;
- realizar medidas básicas.

RCSB PDB y PDBe ofrecen este tipo de visualización integrada.

---

## 11.2.2. Mol*

**Mol*** es un visor molecular web utilizado en recursos estructurales modernos.

Permite trabajar directamente en el navegador con estructuras grandes y complejas.

Entre sus posibilidades se encuentran:

- mostrar cadenas;
- seleccionar residuos;
- visualizar ligandos;
- cambiar estilos;
- inspeccionar ensamblajes;
- analizar regiones concretas.

Para una primera exploración estructural, un visor web suele ser suficiente.

---

## 11.2.3. PyMOL

**PyMOL** es una herramienta ampliamente utilizada para visualización molecular.

Permite:

- cargar estructuras;
- seleccionar regiones;
- cambiar representaciones;
- colorear;
- medir distancias;
- generar figuras;
- automatizar acciones mediante comandos.

Su uso es frecuente en investigación y publicación científica.

---

## 11.2.4. UCSF ChimeraX

**ChimeraX** es otra herramienta de análisis y visualización estructural.

Permite trabajar con:

- proteínas;
- complejos;
- mapas de densidad;
- modelos predichos;
- interacciones;
- superficies.

Es especialmente útil cuando se necesita un análisis más avanzado que el que ofrece un visor web.

---

## 11.2.5. Visualización interactiva frente a figura estática

Una imagen incluida en un artículo muestra una vista seleccionada.

Una herramienta interactiva permite:

- rotar;
- ampliar;
- ocultar elementos;
- seleccionar residuos;
- cambiar colores;
- medir;
- explorar regiones.

Por ello, una imagen es una representación final, mientras que un visor es una herramienta de exploración.

---

## 11.2.6. Selecciones

Una de las operaciones fundamentales consiste en seleccionar partes de la estructura.

Por ejemplo:

```text
cadena A
residuo 150
ligando ATP
residuos a menos de 4 Å del ligando
```

Las selecciones permiten centrar el análisis en elementos concretos.

---

## 11.2.7. Medidas geométricas

Los visores permiten realizar medidas como:

- distancia entre átomos;
- ángulos;
- contactos;
- distancias entre residuos.

Estas medidas ayudan a estudiar si una interacción es geométricamente plausible.

---

## 11.2.8. Superposición estructural

Dos estructuras pueden superponerse para analizar sus semejanzas y diferencias.

Por ejemplo:

- misma proteína con y sin ligando;
- proteína normal y mutante;
- proteínas homólogas;
- estructura experimental y modelo predicho.

La superposición permite identificar cambios conformacionales.

---

## 11.2.9. RMSD

Una medida frecuente para cuantificar diferencias estructurales es el **RMSD** (*Root Mean Square Deviation*).

De forma conceptual, mide la distancia promedio entre posiciones correspondientes después de superponer las estructuras.

En general:

- RMSD pequeño → estructuras más parecidas;
- RMSD grande → mayores diferencias.

Sin embargo, debe interpretarse teniendo en cuenta:

- qué átomos se comparan;
- qué regiones se han alineado;
- tamaño de la proteína;
- flexibilidad.

---

## 11.2.10. Una representación debe responder a una pregunta

Ejemplos:

### Pregunta

¿Dónde está el ligando?

Representación adecuada:

```text
proteína: cartoon
ligando: sticks
```

### Pregunta

¿Cómo se organizan las subunidades?

Representación:

```text
cada cadena con un color distinto
```

### Pregunta

¿Existe una cavidad?

Representación:

```text
superficie molecular
```

La visualización debe diseñarse a partir del objetivo analítico.

---

# 11.3. Análisis de interacciones moleculares

## 11.3.1. Las estructuras funcionan mediante interacciones

La función molecular depende en gran medida de interacciones entre:

- átomos;
- residuos;
- cadenas;
- proteínas;
- ácidos nucleicos;
- ligandos;
- iones;
- agua.

El análisis estructural intenta identificar qué interacciones pueden contribuir a la estabilidad o al reconocimiento molecular.

---

## 11.3.2. Interacciones covalentes y no covalentes

Las interacciones pueden ser:

### Covalentes

Implican enlaces químicos fuertes.

Ejemplo:

- puentes disulfuro.

### No covalentes

Son fundamentales para la estructura y el reconocimiento.

Entre ellas:

- puentes de hidrógeno;
- interacciones electrostáticas;
- interacciones hidrofóbicas;
- fuerzas de van der Waals;
- interacciones aromáticas.

---

## 11.3.3. Puentes de hidrógeno

Un puente de hidrógeno se produce entre grupos químicos compatibles cuando existe una geometría adecuada.

Puede contribuir a:

- estructura secundaria;
- reconocimiento de ligandos;
- interfaces proteína-proteína;
- unión proteína-ADN.

Los visores pueden ayudar a identificar posibles puentes de hidrógeno.

---

## 11.3.4. Interacciones electrostáticas

Residuos cargados pueden atraerse o repelerse.

Por ejemplo:

- grupos con carga positiva;
- grupos con carga negativa.

Estas interacciones pueden influir en:

- estabilidad;
- unión;
- orientación de ligandos.

---

## 11.3.5. Interacciones hidrofóbicas

Los grupos hidrofóbicos tienden a evitar el contacto con el agua.

Este efecto contribuye significativamente al plegamiento de proteínas y a la formación de interfaces.

En proteínas globulares, muchos residuos hidrofóbicos se encuentran en el interior.

---

## 11.3.6. Fuerzas de van der Waals

Son interacciones débiles a corta distancia.

Aunque cada interacción individual es pequeña, muchas contribuciones pueden ser importantes para:

- empaquetamiento;
- complementariedad;
- estabilidad.

---

## 11.3.7. Puentes disulfuro

Dos residuos de cisteína pueden formar un enlace covalente:

```text
Cys — S — S — Cys
```

Estos enlaces pueden estabilizar determinadas estructuras proteicas.

Son especialmente frecuentes en algunas proteínas extracelulares.

---

## 11.3.8. Sitios de unión

Un ligando suele unirse en una región concreta:

- cavidad;
- bolsillo;
- surco;
- superficie.

El sitio de unión puede estar formado por residuos que aportan:

- carga;
- hidrofobicidad;
- geometría;
- enlaces de hidrógeno.

La función depende de la combinación de estas propiedades.

---

## 11.3.9. Interacción proteína-ligando

Para analizar un complejo proteína-ligando podemos preguntar:

1. ¿dónde está situado el ligando?
2. ¿qué residuos están cerca?
3. ¿qué tipos de interacción aparecen?
4. ¿existe complementariedad geométrica?
5. ¿la unión se produce en un sitio funcional conocido?

Una representación habitual es:

```text
proteína → cartoon
residuos del sitio → sticks
ligando → sticks o spheres
```

---

## 11.3.10. Interacciones proteína-proteína

En un complejo entre proteínas podemos estudiar la **interfaz**.

La interfaz está formada por los residuos de ambas cadenas que se encuentran en contacto.

Puede incluir:

- interacciones hidrofóbicas;
- puentes de hidrógeno;
- interacciones electrostáticas;
- complementariedad de superficies.

---

## 11.3.11. Interacciones con ácidos nucleicos

Las proteínas pueden reconocer ADN o ARN mediante:

- carga;
- forma;
- puentes de hidrógeno;
- contactos con bases;
- contactos con el esqueleto fosfato.

La visualización permite analizar qué regiones proteicas participan en la unión.

---

## 11.3.12. Distancia no equivale automáticamente a interacción

Dos átomos cercanos pueden ser candidatos a interacción.

Pero la distancia por sí sola no es suficiente.

También importan:

- orientación;
- naturaleza química;
- entorno;
- protonación;
- flexibilidad.

Por ello, un análisis visual es una primera aproximación.

---

# 11.4. Estructura y función

La principal utilidad del análisis estructural consiste en relacionar forma y función.

Podemos preguntarnos:

- ¿por qué una enzima reconoce determinado sustrato?
- ¿cómo una mutación puede alterar una interacción?
- ¿por qué un fármaco se une a una proteína?
- ¿cómo se forma un complejo?
- ¿qué región puede ser una diana terapéutica?

La estructura ayuda a generar explicaciones mecanísticas.

---

# 11.5. Ejemplo integrado: una proteína con ligando

Supongamos una estructura que contiene:

```text
proteína + ATP
```

Podemos seguir este análisis:

### 1. Representar la proteína como cartoon

Permite observar el plegamiento general.

### 2. Mostrar ATP como sticks

Permite localizar el ligando.

### 3. Seleccionar residuos próximos

Por ejemplo, residuos situados a una distancia pequeña del ATP.

### 4. Mostrar esos residuos como sticks

Permite analizar la geometría local.

### 5. Identificar contactos

Podemos buscar:

- puentes de hidrógeno;
- cargas complementarias;
- contactos hidrofóbicos.

### 6. Interpretar

Podemos proponer qué residuos participan en el reconocimiento del ATP.

El análisis no demuestra por sí solo la función de cada residuo, pero genera una interpretación estructural que puede contrastarse con información experimental.

---

# 11.6. Comparación de estructuras

Una misma proteína puede disponer de varias estructuras.

Podemos comparar:

```text
proteína libre
      vs
proteína + ligando
```

Si al superponerlas observamos que un dominio cambia de posición, podemos plantear que la unión está asociada con un cambio conformacional.

Pero debemos distinguir:

- diferencia estructural observada;
- interpretación funcional propuesta.

---

# 11.7. Limitaciones de la visualización estructural

## Estructura estática

Una estructura representa uno o varios estados, pero las biomoléculas son dinámicas.

## Condiciones experimentales

La estructura puede haberse obtenido en condiciones diferentes del entorno celular.

## Regiones ausentes

Algunas regiones flexibles pueden no estar resueltas.

## Resolución limitada

No todos los átomos están definidos con la misma precisión.

## Modelo frente a realidad

La representación visual es un modelo construido a partir de datos experimentales o predicciones.

---

# 11.8. Errores frecuentes

## Utilizar siempre la misma representación

Cada pregunta requiere una vista diferente.

## Confundir color con propiedad real

El color suele ser una elección del programa o del usuario.

## Asumir que proximidad significa interacción

Debe considerarse geometría y química.

## Interpretar una estructura como rígida

Las biomoléculas presentan dinámica conformacional.

## Ignorar cadenas o ligandos

Puede eliminar información esencial.

## Dar significado funcional a cualquier diferencia estructural

Una diferencia observada necesita evidencia y contexto.

## Confundir una figura atractiva con un análisis riguroso

La visualización es útil cuando responde a una pregunta concreta.

---

# 11.9. Cuestiones guía

1. ¿Por qué una misma estructura puede representarse de formas diferentes?
2. ¿Qué información destaca una representación cartoon?
3. ¿Cuándo sería más útil mostrar una superficie molecular?
4. ¿Qué utilidad tiene colorear por cadenas?
5. ¿Qué diferencia existe entre una figura estática y un visor interactivo?
6. ¿Qué información aporta una superposición estructural?
7. ¿Qué representa conceptualmente el RMSD?
8. ¿Qué tipos principales de interacciones no covalentes pueden observarse?
9. ¿Por qué una distancia corta no demuestra por sí sola una interacción?
10. ¿Qué información puede obtenerse de una interfaz proteína-proteína?
11. ¿Cómo puede relacionarse un sitio de unión con la función?
12. ¿Qué limitaciones debemos recordar al interpretar una estructura tridimensional?

---

# Ideas clave

- Las coordenadas estructurales necesitan herramientas de visualización para ser interpretadas.
- Una misma estructura admite múltiples representaciones.
- Cartoon permite comprender plegamiento y estructura secundaria.
- Sticks y bolas y varillas son útiles para analizar regiones locales y ligandos.
- Las superficies permiten estudiar forma, cavidades e interfaces.
- El color puede codificar información estructural o funcional.
- Los visores permiten seleccionar, medir y comparar estructuras.
- La superposición ayuda a detectar semejanzas y cambios conformacionales.
- Las interacciones moleculares dependen de geometría y propiedades químicas.
- Un contacto visual no constituye automáticamente una interacción funcional.
- La visualización es una herramienta de análisis, no únicamente de presentación.
- Toda interpretación estructural debe considerar las limitaciones del modelo.

---

# Conexión con el siguiente tema

En este tema hemos aprendido a explorar y analizar estructuras tridimensionales.

En el **Tema 12. Predicción estructural mediante inteligencia artificial** estudiaremos cómo obtener modelos estructurales cuando no existe una estructura experimental y analizaremos:

- fundamentos del modelado estructural;
- AlphaFold;
- medidas de confianza;
- limitaciones de los modelos predichos;
- aplicaciones emergentes de inteligencia artificial en Bioinformática estructural.
