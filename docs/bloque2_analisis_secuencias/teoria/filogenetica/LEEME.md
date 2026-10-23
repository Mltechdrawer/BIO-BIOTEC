# Material docente: COX1 y UPGMA

Abre `construccion_arbol_filogenetico.md` para la explicación, resultados, árbol y GIF.

**Para publicar en GitHub Pages:** conserva juntos el Markdown y la carpeta `imagenes/`. Los demás archivos permiten al alumnado descargar y reproducir el análisis.

**Para reproducir:** `pip install biopython matplotlib numpy pillow`, luego `python procesar_datos.py` y `python generar_animacion.py` desde esta carpeta. No requiere Internet ni MAFFT. Los registros originales están en `genbank/`.

El alineamiento es global progresivo anclado a humano, no un alineamiento MAFFT. Las distancias p excluyen huecos por pareja. El árbol es una hipótesis de un solo gen y UPGMA presupone reloj molecular.
