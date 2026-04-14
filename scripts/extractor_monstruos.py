import os
import glob
import re

# Palabras clave heurísticas para PNJs (en minúsculas para match case-insensitive)
PNJ_KEYWORDS = [
    "mago", "guerrero", "ladrón", "ladrona", "clérigo", "hechicero", "bárbaro", "arquero", 
    "acólito", "aprendiz", "guardia", "aldeano", "mercenario", "bandido", "pirata", 
    "sacerdote", "sacerdotisa", "caballero", "nigromante", "rey", "reina", "capitán", 
    "comandante", "líder", "nivel", "humano", "elfo", "enano", "mediano", "gnomo", 
    "asesino", "paladín", "druida", "monje", "bardo", "sectario", "fanático", "pnj"
]

def format_count_section(entities_dict):
    out = "\n## Apariciones en Aventuras\n\n"
    sorted_items = sorted(
        entities_dict.items(), 
        key=lambda item: (-len(item[1]['adventures']), item[0].lower())
    )
    for name, data in sorted_items:
        out += f"- **{name}**: {len(data['adventures'])}\n"
    return out

def is_pnj(name_or_desc):
    text = name_or_desc.lower()
    for kw in PNJ_KEYWORDS:
        # Check as a whole word to avoid false positives?
        # e.g., if kw is "rey", does "Brey" match? Yes, let's use word boundaries
        if re.search(rf'\b{kw}\b', text):
            return True
    return False

def clean_name(raw_name):
    n = raw_name.strip()
    # Eliminar cosas como (x5), (2), (1d3), (2d4+2), (ilimitadas) al final
    n = re.sub(r'\s*\(\s*(?:x|×)?\s*\d+d?\d*(?:\+\d+)?\s*\)$', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\s*\(\s*ilimitadas\s*\)$', '', n, flags=re.IGNORECASE)
    n = re.sub(r'\s*\(\s*\d+\s*\)$', '', n)
    return n.strip()

def extract():
    files = glob.glob('procesados/*-monstruos.md')
    
    monstruos = {}
    pnjs = {}
    
    for f in files:
        adventure_name = os.path.basename(f).replace('-monstruos.md', '')
        
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            
        # Parse blocks
        # Asumimos que un bloque empieza por la línea principal "**Name...**" o "**Name**"
        # y llega hasta que empieza el siguiente
        lines = content.split('\n')
        current_block = []
        raw_name_line = ""
        
        def process_entity(block, raw_line, adv_name):
            if not block: return
            
            # Extract name and desc
            m = re.match(r'^\*\*(.*?)\*\*(.*)', raw_line)
            if not m:
                # If there's no bold, maybe just take the line
                full_name = raw_line.strip()
                desc = ""
            else:
                full_name = m.group(1).strip()
                desc = m.group(2).strip()
                
            clean = clean_name(full_name)
            # The classification text includes the name and the text after it (like (Mago nivel 10))
            class_text = clean + " " + desc
            
            is_entity_pnj = is_pnj(class_text)
            
            target_dict = pnjs if is_entity_pnj else monstruos
            
            if clean not in target_dict:
                target_dict[clean] = {
                    'block': '\n'.join(block).strip(),
                    'adventures': {adv_name}
                }
            else:
                target_dict[clean]['adventures'].add(adv_name)
        
        for line in lines:
            if line.startswith('**'):
                if current_block:
                    process_entity(current_block, raw_name_line, adventure_name)
                current_block = [line]
                raw_name_line = line
            else:
                # If it's the title line # ... ignore it unless it's inside a block
                if line.startswith('#'):
                    continue
                if current_block:
                    current_block.append(line)
                    
        # Último bloque
        if current_block:
            process_entity(current_block, raw_name_line, adventure_name)
            
    # Función para generar el documento final
    def write_output(filename, entities, title):
        sorted_keys = sorted(entities.keys(), key=lambda x: x.lower())
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            
            for k in sorted_keys:
                data = entities[k]
                advs = sorted(list(data['adventures']))
                adv_str = ", ".join(advs)
                f.write(f"{data['block']}\n")
                f.write(f"- *Aventuras en las que aparece:* {adv_str}\n\n")
                f.write("---\n\n")
                
            f.write(format_count_section(entities))
            
    write_output('monstruos.md', monstruos, 'Monstruos')
    write_output('PNJs.md', pnjs, 'Personajes No Jugadores (PNJs)')
    
    print(f"Extraction completed. {len(monstruos)} monstruos, {len(pnjs)} PNJs.")

if __name__ == '__main__':
    extract()
