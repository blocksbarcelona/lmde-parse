# Requisitos Técnicos — Procesado de PDFs de La Marca del Este

## Objetivo

Extraer automáticamente la información de conjuros y monstruos con estadísticas mecánicas de los módulos PDF del juego de rol *La Marca del Este* (LMDE), guardando los resultados como archivos Markdown estructurados.

---

## Entorno de trabajo

| Elemento | Valor |
|----------|-------|
| Herramienta principal | Claude Code CLI |
| Versión Claude Code | 2.1.104 |
| Modelo | claude-sonnet-4-6 |
| Sistema operativo | macOS (darwin arm64) |
| Shell | bash |
| Repositorio fuente | `codexlmde` |
| Carpeta de salida | `procesados/` |

---

## Dependencias externas

### 1. Git LFS

Los PDFs están almacenados como punteros Git LFS (~133 bytes cada uno). Sin LFS, los archivos descargados no son PDFs válidos.

```bash
# Instalación (macOS)
brew install git-lfs

# Inicialización en el repositorio
cd /ruta/al/repo
git lfs install

# Descarga de un PDF concreto antes de subirlo a NotebookLM
git lfs pull --include="codex/content/es/posts/downloads/<archivo>.pdf"

# Verificación (debe mostrar tamaño real, no 133 bytes)
ls -lh codex/content/es/posts/downloads/<archivo>.pdf
```

**Versión usada:** git-lfs/3.7.1

### 2. notebooklm-py

CLI de Python para automatizar Google NotebookLM. Se usa para subir PDFs, esperar a que se procesen y hacer consultas de extracción.

```bash
# Instalación desde PyPI
pip install notebooklm-py

# Instalación de la skill para Claude Code
notebooklm skill install

# Autenticación (abre el navegador para OAuth con Google)
notebooklm login

# Verificación
notebooklm list
```

**Versión usada:** notebooklm-py 0.3.3

---

## Skills de Claude Code necesarias

### notebooklm (skill instalada)

Skill que expone los comandos de `notebooklm-py` dentro del flujo de Claude Code. Se activa automáticamente cuando se usan comandos `notebooklm`.

**Comandos utilizados en este proyecto:**

| Comando | Uso |
|---------|-----|
| `notebooklm use <notebook_id>` | Establece el notebook activo |
| `notebooklm source add <ruta_pdf> --json` | Sube un PDF y devuelve su `source_id` |
| `notebooklm source wait <source_id> --timeout 300` | Espera a que el PDF esté procesado |
| `notebooklm source list --json` | Lista todos los sources con sus IDs |
| `notebooklm ask "<consulta>" -s <source_id>` | Hace una pregunta limitada a un source concreto |

---

## Notebook central de NotebookLM

Se usa **un único notebook** para todos los libros. Los sources se acumulan y se usa el flag `-s <source_id>` para aislar las consultas al PDF que se está procesando en cada momento.

| Campo | Valor |
|-------|-------|
| Nombre | La Marca del Este - Procesador |
| Notebook ID | `7d383414-68ec-4e76-a226-c63a5091e5bc` |

---

## Archivos excluidos

El archivo `no-procesar.md` (en la raíz de este repositorio) lista los archivos que **no deben procesarse** por estar fuera del scope: manuales de reglas, bestiarios y suplementos genéricos.

**Al inicio de cada sesión**, leer `no-procesar.md` antes de determinar el siguiente archivo a procesar.

---

## Flujo de procesado por PDF

```
0. Leer no-procesar.md y excluir esos archivos de la cola de procesado.

1. notebooklm use 7d383414-68ec-4e76-a226-c63a5091e5bc
   notebooklm source add "<ruta_absoluta_al_pdf>" --json
   # → anota el source_id devuelto

2. notebooklm source wait <source_id> --timeout 300

3. (en paralelo)
   notebooklm ask "Extrae todos los conjuros con descripción mecánica..." -s <source_id>
   notebooklm ask "Extrae todas las criaturas con estadísticas de combate..." -s <source_id>

4. Crear archivos en local:
   procesados/<nombre-pdf>-conjuros.md
   procesados/<nombre-pdf>-monstruos.md

5. Push a GitHub: SOLO cuando el usuario lo solicite explícitamente.
   (Se procesan varios PDFs en local antes de hacer push)
```

### Prompts de extracción

**Conjuros:**
> Extrae todos los conjuros con descripción mecánica (alcance, duración, efectos) de este documento. Para cada conjuro incluye: nombre, nivel, clase (mago/clérigo/etc.), alcance, duración y descripción completa del efecto. Si no hay conjuros con estadísticas mecánicas, responde solo: "No hay conjuros con estadísticas en este documento."

**Monstruos:**
> Extrae todas las criaturas y monstruos con estadísticas de combate (DG/HD, CA, ataques, daño, salvación, moral, movimiento, habilidades especiales) de este documento. Para cada uno incluye todos sus datos. Si no hay monstruos con estadísticas, responde solo: "No hay monstruos con estadísticas en este documento."

---

## Reglas de contenido

- Si un documento **no tiene conjuros con stats**, el archivo `-conjuros.md` contiene solo una nota breve indicándolo.
- Si un documento **no tiene monstruos con stats**, el archivo `-monstruos.md` contiene solo una nota breve indicándolo.
- Si un documento **no tiene ni conjuros ni monstruos con stats**, se anota brevemente y se pasa al siguiente sin más desarrollo.
- No se añade información extra más allá de lo que aparece en el PDF.

---

## Orden de procesado

Los PDFs se procesan en orden de fecha de modificación inverso (más reciente primero):

```bash
ls -lt codex/content/es/posts/downloads/*.pdf | awk '{print $NF}' | sed 's|.*/||'
```

---

## Estructura de archivos de salida

```
procesados/
├── <nombre-modulo>-conjuros.md
├── <nombre-modulo>-monstruos.md
└── ...
```

Cada par de archivos corresponde a un PDF. Nombre del archivo = nombre del PDF sin extensión + `-conjuros` o `-monstruos`.

---

## Memoria persistente de Claude Code

El procedimiento y contexto del proyecto se guardan en:

```
~/.claude/projects/memory/
├── MEMORY.md                              # Índice de memorias
└── project_procedimiento_procesado_pdfs.md  # Procedimiento completo
```

Este sistema de memoria permite retomar el trabajo en sesiones futuras sin perder el contexto.

---

## Post-Procesado: Extracción de Monstruos y PNJs

Una vez generados los documentos en la carpeta `procesados/`, se utiliza un script en Python (`scripts/extractor_monstruos.py`) para consolidar y clasificar todas las entidades de los archivos `-monstruos.md` en dos categorías:
1. **PNJs**: Se identifican aplicando una heurística de palabras clave referidas a clases humanoides (ej: mago, guerrero, ladrón, aldeano, etc.) en su nombre o texto adjunto. El resultado se guarda en `PNJs.md`.
2. **Monstruos**: El resto de las entidades, guardadas en `monstruos.md`.

Ambos archivos generados en la raíz recogen de forma desduplicada cada entidad, el bloque íntegro de sus variables mecánicas, y las aventuras específicas en las que aparecen. Al final de los documentos se anexa un listado ordenado descendentemente por frecuencia de aparición.

---

## Resumen de PDFs procesados

108 PDFs en total. Se van procesando en sesiones sucesivas de Claude Code, retomando siempre desde el siguiente PDF pendiente según el orden cronológico inverso.
