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

**124 módulos identificados** — 108 PDFs directos + 16 desde archivos .rar/.zip.
**124 procesados**. **0 pendientes**.

| Módulo | Fuente | Conjuros | Monstruos |
|--------|--------|----------|-----------|
| x3-la-taiga-maldita | .rar | — | ✓ |
| x2-el-arca-de-los-mil-inviernos | .rar | — | ✓ |
| v1-el-castillo-prohibido-de-la-reina-de-sangre | .rar | — | ✓ |
| una-extrana-enfermedad | .rar | — | ✓ |
| rescate-en-torrealba | .rar | ✓ | ✓ |
| la-llamada-de-los-dioses | .rar | — | ✓ |
| mn1-marjalnegro | .rar | — | ✓ |
| G2-alameda | .rar | — | ✓ |
| G1-un-paseo-por-el-campo | .rar | — | ✓ |
| el-tesoro-de-caliope | .rar | — | ✓ |
| el-presidio-de-ibn-firnas | .rar | — | ✓ |
| el-dedalo-de-la-casa-syldi | .rar | — | ✓ |
| el-castillo-de-piedra-negra | .rar | — | ✓ |
| b22-el-dios-del-rio | .rar | — | ✓ |
| b17-el-bucaro-de-alabastro | .rar | — | ✓ |
| b14-vileza-en-el-bastion-de-los-bandidos | .rar | — | ✓ |
| b6-tiempo-fuera-del-tiempo | .rar | — | ✓ |
| b12-el-monasterio-del-dragon-dormido | .rar | — | ✓ |
| la-tumba-de-los-horrores | .zip | — | ✓ |
| elultimoviaje | .zip | — | — |
| la-montana-soberana-v2 | PDF | — | ✓ |
| la-caida-de-los-justos | PDF | — | ✓ |
| el-santuario-olvidado-v2 | PDF | — | ✓ |
| el-legado-perdido | PDF | — | ✓ |
| b23-la-corona-del-nigromante | PDF | — | ✓ |
| miedoalaoscuridad | PDF | ✓ | ✓ |
| V3-el-ojo-de-sanna | PDF | — | ✓ |
| Pandemonium | PDF | — | ✓ |
| b21_el_destino_del_rey_mono | PDF | — | ✓ |
| b20-la-luz-de-valion | PDF | — | ✓ |
| el-despertar-2-el-templo-del-desierto | PDF | ✓ | ✓ |
| Ojos de Serpiente | PDF | — | ✓ |
| HojasGemelas | PDF | — | ✓ |
| Senderos en la Nieve | PDF | — | ✓ |
| el_espectro_de_las_tormentas | PDF | — | ✓ |
| atrapadoseneltiempo | PDF | — | ✓ |
| nuestroshermanoscaidosenbatalla | PDF | — | ✓ |
| el-despertar-1-el-tesoro-de-los-faraones | PDF | — | ✓ |
| traicion | PDF | — | ✓ |
| la-isla-del-terror | PDF | — | ✓ |
| b9-la-ultima-frontera | PDF | ✓ | ✓ |
| PS1-manual-de-psionica | PDF | — | ✓ |
| el-despertar-3-la-venganza-del-sacerdote | PDF | ✓ | ✓ |
| el-soberano-incapaz | PDF | — | ✓ |
| b8-la-tumba-de-hielo | PDF | — | ✓ |
| c3-el-jardin-negro | PDF | — | ✓ |
| profanacion-mejorado | PDF | — | ✓ |
| ig-nagor-mejorado | PDF | — | ✓ |
| c2-la-catacumba-de-los-espantos-de-kavaduz | PDF | ✓ | ✓ |
| ame-serpientes-entre-las-ramas | PDF | — | ✓ |
| la-hija-del-gigante-de-hielo | PDF | — | ✓ |
| no-profanaras-el-sueno-de-los-muertos | PDF | — | ✓ |
| el-tumulo-perdido-de-azgoz-el-testarudo | PDF | — | ✓ |
| el-valle-de-los-unicornios | PDF | — | ✓ |
| Leviatan | PDF | — | ✓ |
| laciudadperdidadegaran | PDF | — | ✓ |
| b2-la-isla-misteriosa | PDF | — | ✓ |
| mn2-la-balada-del-efimero-paladin | PDF | — | ✓ |
| b3-el-orbe-de-amonhtep | PDF | ✓ | ✓ |
| ct1-la-lagrima-de-zurah | PDF | — | ✓ |
| laespadaenlaroca | PDF | — | ✓ |
| b19-agitando-pozasdemugre | PDF | — | ✓ |
| y-la-navidad | PDF | ✓ | ✓ |
| xr1-la-ciudad-de-xorandor | PDF | ✓ | ✓ |
| vientos_de_desesperacion | PDF | ✓ | ✓ |
| vestireldungeon | PDF | — | — |
| un-buen-licor | PDF | — | — |
| tower_of_doom_capitulo_1 | PDF | — | — |
| tn3-el-corazon-de-la-oscuridad | PDF | ✓ | ✓ |
| tn2-el-feudo-en-llamas | PDF | ✓ | ✓ |
| tn1-pacto-de-cenizas | PDF | ✓ | ✓ |
| suplemento_reglas_ALMDE | PDF | — | — |
| sepultura-del-honor | PDF | — | ✓ |
| s1-la-gesta-del-enano | PDF | — | ✓ |
| retorno-al-castillo-de-varania | PDF | — | ✓ |
| retorno-a-brookmere | PDF | — | ✓ |
| rastilon | PDF | — | ✓ |
| pozos-envenenados | PDF | — | ✓ |
| corona-de-sal | PDF | — | ✓ |
| la-torre-del-sabio | PDF | — | ✓ |
| ladrones-de-cadaveres | PDF | — | ✓ |
| lme-el-senuelo | PDF | — | ✓ |
| el-templo-del-dios-prohibido | PDF | — | ✓ |
| UnBuenVino | PDF | — | ✓ |
| Por_unas_Tinajas_de_Miel_2_revision | PDF | ✓ | ✓ |
| el_secreto_von_dragonov | PDF | ? | ? |
| la_tumba_de_jannus_el_cruel | PDF | — | ✓ |
| el-aprendiz-de-mago | PDF | — | ✓ |
| aprendiz-de-mago | PDF | — | ✓ |
| lme-los-cristales-de-vexlaor | PDF | — | ✓ |
| El_oro_de_las_Quebradas | PDF | — | ✓ |
| Justos | PDF | — | — |
| b18-la-perla-de-ayakashi | PDF | — | ✓ |
| v2 | PDF | — | — |
| Noches_de_venganza | PDF | — | ✓ |
| La_Cripta_de_las_Sombras | PDF | — | ✓ |
| la_estirpe_perdida | PDF | — | ✓ |
| LaTorreDimensional | PDF | ✓ | ✓ |
| ElPuebloBendecido | PDF | — | ✓ |
| k1-en-compania-de-cuervos | PDF | — | ✓ |
| c4-la-cupula-de-huesos-de-ixambel | PDF | ✓ | ✓ |
| b13-sangre-en-la-nieve | PDF | — | ✓ |
| justicia | PDF | — | ✓ |
| b1-los-clonadores-de-tavuun-17 | PDF | — | ✓ |
| G3-fronda-de-los-medianos | PDF | — | — |
| el-bosque-negro | PDF | — | ✓ |
| el-paramo | PDF | ✓ | ✓ |
| b16-la-piramide-del-faraon-negro | PDF | ✓ | ✓ |
| AELMDE_LaIslaRoja | PDF | — | ✓ |
| elultimocaballerodelaordenescarlata | PDF | — | ✓ |
| la-colina-del-avispon | PDF | — | ✓ |
| la-cala | PDF | — | ✓ |
| B4-muerte-en-la-mansion-del-mago-malifax | PDF | — | ✓ |
| b15-las-minas-del-elefante | PDF | — | ✓ |
| b5-incursion-a-la-tierra-del-dios-azul | PDF | — | ✓ |
| b11-las-cuevas-del-clan-atronador | PDF | — | ✓ |
| el-tumulo-del-rey-orco | PDF | — | ✓ |
| el-legado-de-mushasi | PDF | — | ✓ |
| laaldeaasoladaporlamuerte | PDF | — | ✓ |
| el_pantano_de_los_suspiros | PDF | — | ✓ |
| b7-presentes-sangrientos | PDF | — | ✓ |
| ho1-lo-que-el-ojo-no-ve | PDF | — | ✓ |
| el-signo-rojo | PDF | — | ✓ |
| b1-la-cripta-nefanda-de-uztun-el-maldito | PDF | — | ✓ |

**Sin pendientes** — todos los módulos están procesados.

✓ = tiene contenido extraído · — = sin stats propias · ⏳ = pendiente · ? = PDF escaneado, no procesable

## Fuente

Los módulos provienen del [Codex de la Marca del Este](https://codexdelamarca.com/), el repositorio oficial de aventuras y suplementos del juego. Pertenecen a sus respectivos autores y a *Aventuras en la Marca del Este*. Este repositorio contiene únicamente datos estructurados extraídos con fines de referencia y estudio.
