# lmde-parse

Extracción automatizada de conjuros y monstruos de los módulos PDF de **La Marca del Este** (LMDE), el juego de rol de fantasía en español publicado por [Aventuras en la Marca del Este](https://www.marcadeleste.com/).

## Qué hay aquí

Para cada módulo PDF del juego se generan dos archivos Markdown:

- `<modulo>-conjuros.md` — Todos los conjuros con descripción mecánica (nivel, alcance, duración, efectos).
- `<modulo>-monstruos.md` — Todos los monstruos y criaturas con estadísticas de combate (DG, CA, ataques, daño, salvación, moral, habilidades especiales).

Si un módulo no contiene conjuros o monstruos propios (solo referencias al manual base), el archivo correspondiente lo indica con una nota breve.

## Estructura

```
lmde-parse/
├── README.md
├── requisitos-tecnicos-procesado.md   # Cómo se genera este contenido
└── procesados/
    ├── <modulo>-conjuros.md
    ├── <modulo>-monstruos.md
    └── ...
```

## Cómo se genera

El proceso está completamente automatizado usando **Claude Code** con la skill de **NotebookLM**:

1. Cada PDF se descarga desde un repositorio Git LFS.
2. Se sube a un notebook central de Google NotebookLM.
3. Claude consulta el documento (aislado por `source_id`) para extraer conjuros y monstruos.
4. Los resultados se guardan como Markdown estructurado.

Los detalles técnicos completos están en [`requisitos-tecnicos-procesado.md`](./requisitos-tecnicos-procesado.md).

## Estado

108 módulos PDF en total. Se procesan en orden cronológico inverso (más reciente primero).

| Módulo | Conjuros | Monstruos |
|--------|----------|-----------|
| y-la-navidad | ✓ | ✓ |
| xr1-la-ciudad-de-xorandor | ✓ | ✓ |
| vientos_de_desesperacion | ✓ | ✓ |
| vestireldungeon | — | — |
| un-buen-licor | — | — |
| tower_of_doom_capitulo_1 | — | — |
| tn3-el-corazon-de-la-oscuridad | ✓ | ✓ |
| tn2-el-feudo-en-llamas | ✓ | ✓ |
| tn1-pacto-de-cenizas | ✓ | ✓ |
| suplemento_reglas_ALMDE | — | — |
| sepultura-del-honor | — | ✓ |

✓ = tiene contenido extraído · — = sin stats propias, remite al manual base

## Fuente

Los módulos pertenecen a sus respectivos autores y a *Aventuras en la Marca del Este*. Este repositorio contiene únicamente datos estructurados extraídos con fines de referencia y estudio.
