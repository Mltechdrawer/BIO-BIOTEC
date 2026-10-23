# Tema 12. Predicción estructural mediante inteligencia artificial

## Duración

**2 horas de teoría**

Este tema cierra el **Bloque IV. Bioinformática estructural y modelado computacional**.

De acuerdo con la estructura del curso, se organiza en tres apartados:

- **12.1. Modelado estructural.**
- **12.2. AlphaFold.**
- **12.3. Aplicaciones emergentes de IA en Bioinformática.**

---

## Objetivos de aprendizaje

Al finalizar este tema, el estudiante será capaz de:

- Explicar qué significa modelar computacionalmente una estructura biomolecular.
- Diferenciar entre modelado por homología, predicción *de novo* y métodos actuales basados en inteligencia artificial.
- Comprender qué problema resuelve AlphaFold y qué tipo de información produce.
- Interpretar las principales medidas de confianza de una predicción estructural.
- Diferenciar confianza local y confianza en la disposición relativa de dominios o cadenas.
- Reconocer las limitaciones de los modelos estructurales predichos.
- Explicar por qué un modelo de alta confianza no sustituye automáticamente a una estructura experimental.
- Comprender algunas aplicaciones actuales de IA en predicción de complejos, interacciones y diseño biomolecular.
- Valorar de forma crítica cuándo una predicción puede ser útil y cuándo necesita validación adicional.

---

# Introducción

Durante décadas, conocer la estructura tridimensional de una proteína dependió principalmente de técnicas experimentales como:

- cristalografía de rayos X;
- resonancia magnética nuclear;
- microscopía electrónica criogénica.

Estos métodos siguen siendo fundamentales, pero presentan limitaciones prácticas.

Determinar experimentalmente una estructura puede requerir:

- producir la proteína;
- purificarla;
- obtener condiciones experimentales adecuadas;
- recopilar datos;
- construir y validar el modelo.

Por ello, durante mucho tiempo existió una gran diferencia entre:

```text
número de secuencias conocidas
        >>
número de estructuras conocidas
```

El modelado computacional intentó reducir esa distancia.

La inteligencia artificial ha transformado profundamente este problema.

Hoy es posible obtener modelos estructurales de millones de proteínas con una calidad que, en muchos casos, permite formular hipótesis biológicas útiles.

Pero una cuestión será central durante todo el tema:

> **una estructura predicha es un modelo, no una observación experimental**

Por tanto, además de saber generar o consultar predicciones, debemos aprender a evaluar su confianza y sus limitaciones.

---

# 12.1. Modelado estructural

## 12.1.1. Qué significa modelar una estructura

El **modelado estructural** intenta obtener una representación tridimensional aproximada de una biomolécula mediante métodos computacionales.

La entrada puede ser, por ejemplo:

```text
secuencia de aminoácidos
```

y la salida:

```text
modelo tridimensional
```

El objetivo es estimar cómo podría organizarse la molécula en el espacio.

---

## 12.1.2. Por qué la secuencia contiene información estructural

La estructura de una proteína depende de su secuencia de aminoácidos y de las interacciones físicas y químicas entre sus residuos y el entorno.

Por ello, en principio:

```text
secuencia
   ↓
estructura
   ↓
función
```

Sin embargo, predecir la estructura a partir de la secuencia es extremadamente complejo.

El espacio de conformaciones posibles es enorme.

---

## 12.1.3. Modelado por homología

Antes del auge de los métodos modernos de IA, una estrategia muy utilizada era el **modelado por homología**.

La idea general es:

> proteínas con secuencias relacionadas suelen presentar estructuras relacionadas.

El flujo básico es:

```text
secuencia problema
      ↓
buscar una proteína homóloga con estructura conocida
      ↓
alinear ambas secuencias
      ↓
usar la estructura conocida como molde
      ↓
construir un modelo
```

---

## 12.1.4. Plantilla o template

La estructura conocida utilizada como referencia se denomina habitualmente **template**.

La calidad del modelo depende, entre otros factores, de:

- similitud entre secuencias;
- calidad del alineamiento;
- calidad experimental de la plantilla;
- presencia de inserciones o deleciones;
- diferencias entre dominios.

Si no existe una plantilla suficientemente relacionada, el modelado por homología pierde fiabilidad.

---

## 12.1.5. Modelado de novo

Otra estrategia intenta predecir la estructura sin utilizar directamente una única plantilla estructural cercana.

Históricamente, estos métodos podían basarse en:

- principios físicos;
- búsqueda conformacional;
- fragmentos estructurales;
- funciones de energía.

El problema es computacionalmente muy complejo.

---

## 12.1.6. La información evolutiva

Las proteínas relacionadas evolucionan acumulando cambios.

Algunas posiciones pueden variar de forma coordinada.

Por ejemplo, si un cambio en una posición altera una interacción estructural, otra posición puede cambiar para compensarlo.

Estas **correlaciones evolutivas** aportan información sobre qué residuos podrían estar próximos en la estructura tridimensional.

Los métodos modernos de predicción aprovechan este tipo de información.

---

## 12.1.7. Alineamientos múltiples como fuente de información

Un alineamiento múltiple de secuencias puede revelar:

- posiciones conservadas;
- posiciones variables;
- patrones de coevolución.

Por tanto, conceptos trabajados en el Bloque II reaparecen aquí con una nueva finalidad.

El alineamiento ya no se utiliza únicamente para estudiar relaciones evolutivas.

También puede aportar señales útiles para inferir estructura.

---

# 12.2. AlphaFold

## 12.2.1. El problema que aborda

AlphaFold fue desarrollado para predecir la estructura tridimensional de proteínas a partir de su secuencia.

Su impacto fue especialmente importante porque consiguió mejorar notablemente la precisión de la predicción estructural en muchos casos.

El avance se hizo especialmente visible en la competición internacional **CASP** (*Critical Assessment of Structure Prediction*).

---

## 12.2.2. AlphaFold 2

AlphaFold 2 introdujo una arquitectura de aprendizaje profundo capaz de combinar distintas fuentes de información.

A nivel conceptual utiliza información procedente de:

- secuencia;
- relaciones evolutivas;
- alineamientos múltiples;
- patrones aprendidos de estructuras conocidas.

No necesitamos estudiar en este curso todos los detalles internos de la arquitectura.

Lo importante es comprender que:

> **no busca simplemente una proteína parecida y copia su estructura**

El modelo aprende relaciones complejas entre secuencia y geometría tridimensional.

---

## 12.2.3. De la secuencia al modelo

Conceptualmente:

```text
secuencia
   ↓
información evolutiva
   ↓
representación aprendida por el modelo
   ↓
restricciones geométricas
   ↓
coordenadas tridimensionales
```

La salida principal es un conjunto de coordenadas atómicas que puede visualizarse como cualquier otra estructura.

---

## 12.2.4. AlphaFold Protein Structure Database

Las predicciones pueden consultarse mediante **AlphaFold Protein Structure Database (AlphaFold DB)**.

Recurso:

https://alphafold.ebi.ac.uk/

La base de datos permite buscar modelos asociados a proteínas y consultar:

- estructura predicha;
- secuencia;
- anotación procedente de UniProt;
- confianza local;
- error alineado predicho;
- dominios;
- modelos similares.

---

## 12.2.5. Predicción no significa certeza

Una de las aportaciones más importantes de AlphaFold no es únicamente producir una estructura.

También produce estimaciones de **confianza**.

Esto permite distinguir:

- regiones predichas con alta confianza;
- regiones inciertas;
- posiciones relativas de dominios poco fiables.

Por ello, interpretar AlphaFold exige mirar más que la imagen tridimensional.

---

## 12.2.6. pLDDT

Una de las principales medidas es **pLDDT**.

Es una estimación de confianza por residuo.

Sus valores se encuentran aproximadamente entre:

```text
0 y 100
```

De forma orientativa:

- **pLDDT > 90**: confianza muy alta;
- **70–90**: buena confianza;
- **50–70**: baja confianza;
- **< 50**: región muy poco fiable.

---

## 12.2.7. Interpretación del color

Los modelos de AlphaFold suelen colorearse según pLDDT.

Esto permite reconocer visualmente:

- regiones muy fiables;
- regiones intermedias;
- regiones con baja confianza.

Es importante comprender que el color no representa una propiedad química.

Representa la confianza del modelo.

---

## 12.2.8. Baja confianza no siempre significa error

Una región con pLDDT bajo puede corresponder a:

- región desordenada;
- linker flexible;
- extremo móvil;
- región cuya conformación depende de una interacción;
- región mal predicha.

Por tanto:

> **baja confianza no equivale automáticamente a “modelo incorrecto”**

Puede indicar que la región no adopta una única estructura estable de forma aislada.

---

## 12.2.9. Predicted Aligned Error

Otra medida fundamental es **PAE** (*Predicted Aligned Error*).

PAE ayuda a evaluar la confianza en la posición relativa entre distintas regiones.

Por ejemplo, una proteína puede tener:

- dominio A bien predicho;
- dominio B bien predicho;

pero AlphaFold puede no estar seguro de cómo se orientan entre sí.

---

## 12.2.10. Cómo leer PAE conceptualmente

PAE suele representarse mediante una matriz.

Cada punto informa sobre el error esperado en la posición de una región respecto a otra.

De forma conceptual:

```text
PAE bajo
→ posición relativa más fiable

PAE alto
→ posición relativa incierta
```

---

## 12.2.11. Confianza local frente a organización global

Esta distinción es fundamental.

Puede ocurrir:

```text
dominio A → pLDDT alto
dominio B → pLDDT alto
orientación A-B → PAE alto
```

En ese caso:

- cada dominio puede estar bien modelado;
- la relación espacial entre ellos puede ser incierta.

Por ello, mirar solo pLDDT es insuficiente.

---

## 12.2.12. Modelos y estructuras experimentales

Un modelo AlphaFold puede parecer visualmente muy convincente.

Pero no debe interpretarse igual que una estructura experimental.

Una estructura experimental está respaldada por datos físicos.

Una predicción está respaldada por:

- un modelo computacional;
- información aprendida;
- estimaciones de confianza.

Ambas son útiles, pero representan tipos de evidencia diferentes.

---

## 12.2.13. Comparación con PDB

Antes de interpretar una predicción puede ser útil comprobar si existe una estructura experimental relacionada.

Podemos comparar:

```text
modelo AlphaFold
       vs
estructura PDB
```

Esto permite:

- validar regiones;
- comparar dominios;
- detectar diferencias;
- evaluar la utilidad del modelo.

---

## 12.2.14. Regiones ausentes en estructuras experimentales

Un aspecto interesante es que AlphaFold puede producir coordenadas para toda la secuencia.

En una estructura experimental algunas regiones pueden faltar porque:

- son flexibles;
- no se resolvieron;
- no estaban presentes en la construcción experimental.

Pero que AlphaFold proporcione coordenadas para esas regiones no significa que sean fiables.

La confianza debe evaluarse.

---

# 12.3. Aplicaciones emergentes de IA en Bioinformática

## 12.3.1. Más allá de una proteína aislada

La predicción estructural moderna ya no se limita a una única cadena.

Uno de los objetivos actuales es predecir:

- complejos proteína-proteína;
- proteína-ADN;
- proteína-ARN;
- proteína-ligando;
- complejos con iones;
- ensamblajes biomoleculares.

---

## 12.3.2. AlphaFold-Multimer

AlphaFold-Multimer extendió el enfoque a complejos formados por varias cadenas proteicas.

Esto permite estudiar hipótesis sobre:

- oligomerización;
- interfaces;
- interacciones proteína-proteína.

En este contexto, la confianza en una cadena individual no es suficiente.

También debemos evaluar la confianza de la interfaz.

---

## 12.3.3. Confianza en interfaces

En complejos pueden utilizarse medidas específicas, como:

- **ipTM**;
- medidas derivadas de PAE;
- otros indicadores de confianza de interfaces.

El principio importante es:

> **una proteína puede estar bien modelada y, aun así, la interacción entre cadenas ser incierta**

---

## 12.3.4. AlphaFold 3

AlphaFold 3 amplió el problema de predicción conjunta hacia complejos biomoleculares más diversos.

Puede modelar sistemas que incluyen:

- proteínas;
- ácidos nucleicos;
- moléculas pequeñas;
- iones;
- residuos modificados.

Esto acerca la predicción estructural a problemas de interacción biomolecular mucho más amplios.

---

## 12.3.5. Interacciones con ligandos

Una aplicación especialmente relevante es estudiar posibles complejos entre proteínas y pequeñas moléculas.

Esto puede resultar útil en:

- descubrimiento de fármacos;
- priorización de compuestos;
- análisis de sitios de unión;
- generación de hipótesis.

Sin embargo, una pose predicha no debe confundirse con evidencia experimental de unión.

---

## 12.3.6. Diseño de proteínas

La IA también se utiliza para diseñar nuevas proteínas.

El problema cambia de dirección.

En predicción estructural:

```text
secuencia
   ↓
estructura
```

En diseño:

```text
estructura o función deseada
        ↓
secuencia candidata
```

El objetivo puede ser crear proteínas con:

- nuevas funciones;
- mayor estabilidad;
- capacidad de unión;
- actividad enzimática;
- propiedades biotecnológicas.

---

## 12.3.7. Modelos generativos

Los modelos generativos pueden proponer:

- nuevas secuencias;
- nuevas estructuras;
- variantes de proteínas;
- posibles complejos.

Esto amplía el espacio que puede explorarse computacionalmente.

Pero cualquier propuesta debe validarse.

---

## 12.3.8. Ingeniería de proteínas

En Biotecnología, estas técnicas pueden apoyar:

- diseño de enzimas;
- optimización de proteínas;
- anticuerpos;
- biosensores;
- proteínas de unión;
- desarrollo de biomateriales.

La combinación de predicción, diseño y experimentación puede acelerar ciclos de ingeniería.

---

## 12.3.9. Predicción y medicina

Los modelos estructurales también pueden ayudar a estudiar:

- efecto de variantes;
- posibles mecanismos moleculares;
- sitios de unión;
- proteínas asociadas a enfermedades.

Pero una predicción estructural por sí sola no determina:

- patogenicidad;
- eficacia terapéutica;
- seguridad de un compuesto.

---

# 12.4. Qué puede hacer bien AlphaFold

En muchos casos, AlphaFold puede proporcionar modelos útiles de:

- dominios globulares;
- estructuras conservadas;
- regiones con abundante información evolutiva;
- plegamientos proteicos.

Puede ser especialmente útil cuando:

- no existe estructura experimental;
- queremos formular una hipótesis;
- necesitamos localizar dominios;
- queremos diseñar experimentos;
- queremos comparar una proteína con otras estructuras.

---

# 12.5. Qué puede resultar problemático

Hay situaciones que requieren especial cautela.

## Regiones intrínsecamente desordenadas

Pueden no tener una estructura estable única.

## Regiones flexibles

La conformación puede cambiar.

## Orientación entre dominios

Puede ser incierta aunque cada dominio sea correcto.

## Complejos

La interfaz puede no estar bien predicha.

## Estados conformacionales

Una proteína puede adoptar varios estados funcionales.

## Ligandos y entorno

La estructura puede depender de:

- ligando;
- membrana;
- pH;
- modificaciones;
- otras proteínas.

---

# 12.6. Una proteína no tiene necesariamente una única estructura

Una proteína puede existir en diferentes estados:

```text
abierta
cerrada
activa
inactiva
unida
libre
```

Un modelo predicho representa una posibilidad estructural.

No necesariamente describe todos los estados funcionales.

Esta idea conecta con lo estudiado en el Tema 11 sobre dinámica y cambio conformacional.

---

# 12.7. Ejemplo de interpretación de un modelo AlphaFold

Supongamos que observamos una proteína predicha.

### Región 1

```text
pLDDT = 95
```

Podemos considerarla una región de alta confianza.

### Región 2

```text
pLDDT = 45
```

Debe interpretarse con mucha cautela.

### Dos dominios

Ambos presentan pLDDT alto, pero el PAE entre ellos es elevado.

Conclusión:

- los dominios individuales pueden estar bien predichos;
- su orientación relativa es incierta.

Esta conclusión es mucho más rigurosa que afirmar simplemente:

> “AlphaFold ha predicho correctamente la proteína”.

---

# 12.8. Flujo responsable de trabajo

Un flujo básico podría ser:

```text
secuencia
   ↓
buscar estructura experimental
   ↓
consultar modelo predicho
   ↓
examinar pLDDT
   ↓
examinar PAE
   ↓
identificar dominios
   ↓
comparar con evidencia disponible
   ↓
formular hipótesis
   ↓
validar
```

---

# 12.9. Predicción y validación experimental

La predicción puede ayudar a decidir:

- qué mutación estudiar;
- qué dominio expresar;
- qué residuo modificar;
- qué interacción comprobar;
- qué experimento diseñar.

Por tanto, uno de los usos más potentes de la IA es:

> **generar hipótesis estructurales que orienten la experimentación**

No sustituir necesariamente la experimentación.

---

# 12.10. Reproducibilidad

Cuando se utiliza un modelo predicho conviene registrar:

- secuencia utilizada;
- identificador;
- herramienta;
- versión;
- fecha;
- modelo seleccionado;
- métricas de confianza;
- parámetros, cuando proceda.

Esto permite interpretar y reproducir el análisis.

---

# 12.11. Errores frecuentes

## Considerar que AlphaFold “resolvió” experimentalmente una estructura

AlphaFold predice modelos.

## Interpretar toda la estructura con la misma confianza

La confianza puede variar residuo a residuo.

## Ignorar PAE

Unos dominios bien predichos pueden estar mal orientados entre sí.

## Asumir que pLDDT bajo significa necesariamente error

Puede reflejar desorden o flexibilidad.

## Confundir un complejo predicho con una interacción demostrada

Una predicción necesita validación.

## Usar un modelo como prueba de función

La estructura puede apoyar una hipótesis, no demostrar automáticamente una función.

## Ignorar estados alternativos

Las proteínas son dinámicas.

## No comparar con estructuras experimentales existentes

Puede perderse información esencial.

---

# 12.12. Cuestiones guía

1. ¿Qué diferencia existe entre modelado por homología y predicción estructural moderna?
2. ¿Qué papel tiene la información evolutiva en la predicción?
3. ¿Qué produce AlphaFold como resultado?
4. ¿Qué representa pLDDT?
5. ¿Qué significa una región con pLDDT bajo?
6. ¿Qué información aporta PAE?
7. ¿Cómo puede ser posible que dos dominios estén bien predichos pero su orientación relativa no?
8. ¿Qué diferencia existe entre una estructura experimental y un modelo AlphaFold?
9. ¿Qué tipo de sistemas puede abordar AlphaFold 3?
10. ¿Por qué una interacción predicha no constituye evidencia experimental?
11. ¿Qué aplicaciones puede tener la IA en ingeniería de proteínas?
12. ¿Qué información debe conservarse para utilizar un modelo de forma reproducible?

---

# Ideas clave

- El modelado estructural intenta obtener una representación tridimensional a partir de información computacional.
- El modelado por homología utiliza estructuras conocidas como plantilla.
- Los métodos modernos de IA integran secuencia, información evolutiva y patrones estructurales.
- AlphaFold produce modelos estructurales y estimaciones de confianza.
- pLDDT mide confianza local por residuo.
- PAE ayuda a evaluar confianza en posiciones relativas entre regiones.
- Una región de baja confianza puede corresponder a flexibilidad o desorden.
- Un modelo predicho no equivale a una estructura experimental.
- La predicción de complejos requiere evaluar también la confianza de interfaces.
- AlphaFold 3 amplía la predicción a complejos con proteínas, ácidos nucleicos, ligandos e iones.
- La IA también se utiliza para diseño e ingeniería de proteínas.
- Toda predicción debe interpretarse con evidencia, contexto y validación.

---

# Cierre del Bloque IV

Este tema completa el **Bloque IV. Bioinformática estructural y modelado computacional**.

La progresión del bloque ha sido:

**Tema 10 → localizar y comprender cómo se representan las estructuras**

**Tema 11 → visualizar y analizar estructuras e interacciones**

**Tema 12 → modelar y predecir estructuras mediante métodos computacionales e inteligencia artificial**

La lógica global puede resumirse así:

> **representar → visualizar → analizar → predecir → validar**

Con este bloque se completa también el recorrido conceptual de la asignatura:

```text
información biológica
        ↓
secuencias
        ↓
función
        ↓
estructura
        ↓
modelado y predicción
```

La Bioinformática aparece así como un proceso integrado que conecta datos, algoritmos, conocimiento biológico y herramientas computacionales para formular y contrastar hipótesis.
