# Neighbor-Joining interactivo

Coloca esta carpeta completa en `docs/bloque2_analisis_secuencias/teoria/neighbor_joining_interactivo/`.

Desde `metodos_upgma_neighbor_joining.md`, que está también dentro de `teoria/`, enlaza con Markdown (MkDocs resuelve el destino relativo a la fuente):

```markdown
[Explorar Neighbor-Joining paso a paso](neighbor_joining_interactivo/index.html)
```

Si usas un enlace HTML crudo en el Markdown publicado, el navegador lo resuelve desde la URL de la página generada, por lo que necesitas `../`:

```html
<a href="../neighbor_joining_interactivo/index.html" target="_blank" rel="noopener noreferrer">Explorar Neighbor-Joining paso a paso</a>
```

Los valores de la matriz son ficticios y coinciden con el ejemplo UPGMA: HC=2, HG=6, HO=10, CG=6, CO=10, GO=10. La matriz Q presenta un empate (HC y GO); se elige HC como criterio didáctico. El árbol NJ no está enraizado. No es necesario Python ni conexión a Internet.
