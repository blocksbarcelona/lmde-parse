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

108 módulos PDF en total. Se procesan en orden cronológico inverso (más reciente primero). **100 procesados.**

| Módulo | Conjuros | Monstruos |
|--------|----------|-----------|
| b23-la-corona-del-nigromante | — | ✓ |
| miedoalaoscuridad | ✓ | ✓ |
| V3-el-ojo-de-sanna | — | ✓ |
| Pandemonium | — | ✓ |
| b21_el_destino_del_rey_mono | — | ✓ |
| b20-la-luz-de-valion | — | ✓ |
| el-despertar-2-el-templo-del-desierto | ✓ | ✓ |
| Ojos de Serpiente | — | ✓ |
| HojasGemelas | — | ✓ |
| Senderos en la Nieve | — | ✓ |
| el_espectro_de_las_tormentas | — | ✓ |
| atrapadoseneltiempo | — | ✓ |
| nuestroshermanoscaidosenbatalla | — | ✓ |
| el-despertar-1-el-tesoro-de-los-faraones | — | ✓ |
| traicion | — | ✓ |
| la-isla-del-terror | — | ✓ |
| b9-la-ultima-frontera | ✓ | ✓ |
| PS1-manual-de-psionica | — | ✓ |
| el-despertar-3-la-venganza-del-sacerdote | ✓ | ✓ |
| el-soberano-incapaz | — | ✓ |
| b8-la-tumba-de-hielo | — | ✓ |
| c3-el-jardin-negro | — | ✓ |
| profanacion-mejorado | — | ✓ |
| ig-nagor-mejorado | — | ✓ |
| c2-la-catacumba-de-los-espantos-de-kavaduz | ✓ | ✓ |
| ame-serpientes-entre-las-ramas | — | ✓ |
| la-hija-del-gigante-de-hielo | — | ✓ |
| no-profanaras-el-sueno-de-los-muertos | — | ✓ |
| el-tumulo-perdido-de-azgoz-el-testarudo | — | ✓ |
| el-valle-de-los-unicornios | — | ✓ |
| Leviatan | — | ✓ |
| laciudadperdidadegaran | — | ✓ |
| b2-la-isla-misteriosa | — | ✓ |
| mn2-la-balada-del-efimero-paladin | — | ✓ |
| b3-el-orbe-de-amonhtep | ✓ | ✓ |
| ct1-la-lagrima-de-zurah | — | ✓ |
| laespadaenlaroca | — | ✓ |
| b19-agitando-pozasdemugre | — | ✓ |
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
| s1-la-gesta-del-enano | — | ✓ |
| retorno-al-castillo-de-varania | — | ✓ |
| retorno-a-brookmere | — | ✓ |
| rastilon | — | ✓ |
| pozos-envenenados | — | ✓ |
| corona-de-sal | — | ✓ |
| la-torre-del-sabio | — | ✓ |
| ladrones-de-cadaveres | — | ✓ |
| lme-el-senuelo | — | ✓ |
| el-templo-del-dios-prohibido | — | ✓ |
| UnBuenVino | — | ✓ |
| Por_unas_Tinajas_de_Miel_2_revision | ✓ | ✓ |
| el_secreto_von_dragonov | ? | ? |
| la_tumba_de_jannus_el_cruel | — | ✓ |
| el-aprendiz-de-mago | — | ✓ |
| aprendiz-de-mago | — | ✓ |
| lme-los-cristales-de-vexlaor | — | ✓ |
| El_oro_de_las_Quebradas | — | ✓ |
| Justos | — | — |
| b18-la-perla-de-ayakashi | — | ✓ |
| v2 | — | — |
| Noches_de_venganza | — | ✓ |
| La_Cripta_de_las_Sombras | — | ✓ |
| la_estirpe_perdida | — | ✓ |
| LaTorreDimensional | ✓ | ✓ |
| ElPuebloBendecido | — | ✓ |
| k1-en-compania-de-cuervos | — | ✓ |
| c4-la-cupula-de-huesos-de-ixambel | ✓ | ✓ |
| b13-sangre-en-la-nieve | — | ✓ |
| justicia | — | ✓ |
| b1-los-clonadores-de-tavuun-17 | — | ✓ |
| G3-fronda-de-los-medianos | — | — |
| el-bosque-negro | — | ✓ |
| el-paramo | ✓ | ✓ |
| b16-la-piramide-del-faraon-negro | ✓ | ✓ |
| AELMDE_LaIslaRoja | — | ✓ |
| elultimocaballerodelaordenescarlata | — | ✓ |
| la-colina-del-avispon | — | ✓ |
| la-cala | — | ✓ |
| B4-muerte-en-la-mansion-del-mago-malifax | — | ✓ |
| b15-las-minas-del-elefante | — | ✓ |
| b5-incursion-a-la-tierra-del-dios-azul | — | ✓ |
| b11-las-cuevas-del-clan-atronador | — | ✓ |
| el-tumulo-del-rey-orco | — | ✓ |
| el-legado-de-mushasi | — | ✓ |
| laaldeaasoladaporlamuerte | — | ✓ |
| el_pantano_de_los_suspiros | — | ✓ |
| b7-presentes-sangrientos | — | ✓ |
| ho1-lo-que-el-ojo-no-ve | — | ✓ |
| el-signo-rojo | — | ✓ |
| b1-la-cripta-nefanda-de-uztun-el-maldito | — | ✓ |

✓ = tiene contenido extraído · — = sin stats propias, remite al manual base

## Fuente

Los módulos provienen del [Codex de la Marca del Este](https://codexdelamarca.com/), el repositorio oficial de aventuras y suplementos del juego. Pertenecen a sus respectivos autores y a *Aventuras en la Marca del Este*. Este repositorio contiene únicamente datos estructurados extraídos con fines de referencia y estudio.
