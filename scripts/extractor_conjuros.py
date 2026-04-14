import os
import glob
import re

def format_count_section(entities_dict):
    out = "\n## Apariciones en Aventuras\n\n"
    sorted_items = sorted(
        entities_dict.items(), 
        key=lambda item: (-len(item[1]['adventures']), item[0].lower())
    )
    for name, data in sorted_items:
        out += f"- **{name}**: {len(data['adventures'])}\n"
    return out

def extract_conjuros():
    files = glob.glob('procesados/*-conjuros.md')
    conjuros = {}
    
    for f in files:
        adventure_name = os.path.basename(f).replace('-conjuros.md', '')
        
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            
        # Saltamos archivos vacíos o que digan explícitamente que no hay conjuros
        if "No hay conjuros" in content or "no contiene conjuros" in content.lower():
            continue
            
        lines = content.split('\n')
        current_block = []
        current_name = ""
        
        def process_entity(block, name, adv_name):
            if not block or not name: return
            
            clean = name.strip()
            level = 99
            for line in block:
                # Busca el nivel numérico
                if "nivel" in line.lower():
                    m = re.search(r'Nivel.*?(\d+)', line, re.IGNORECASE)
                    if m:
                        level = int(m.group(1))
                        break
            
            if clean not in conjuros:
                conjuros[clean] = {
                    'block': '\n'.join(block).strip(),
                    'adventures': {adv_name},
                    'level': level
                }
            else:
                conjuros[clean]['adventures'].add(adv_name)
        
        for line in lines:
            if line.startswith('## '):
                # Si ya estábamos procesando un conjuro, guardarlo
                if current_block:
                    process_entity(current_block, current_name, adventure_name)
                
                current_name = line.replace('## ', '').strip()
                current_block = [line]
            elif line.startswith('---'):
                # Fin explícito del conjuro
                if current_block:
                    process_entity(current_block, current_name, adventure_name)
                current_block = []
                current_name = ""
            else:
                # Titulos h1 omitidos
                if line.startswith('# ') and not current_block:
                    continue
                if current_block:
                    current_block.append(line)
                    
        # Último bloque
        if current_block:
            process_entity(current_block, current_name, adventure_name)
            
    # Escribir salida
    # Ordenar por el nivel del conjuro de forma ascendente, y luego alfabéticamente
    sorted_keys = sorted(conjuros.keys(), key=lambda x: (conjuros[x]['level'], x.lower()))
    
    with open('conjuros.md', 'w', encoding='utf-8') as f:
        f.write("# Conjuros\n\n")
        
        for k in sorted_keys:
            data = conjuros[k]
            advs = sorted(list(data['adventures']))
            adv_str = ", ".join(advs)
            
            # Quitar posibles lineas --- finales del bloque que se han colado (no debería por el split)
            f.write(f"{data['block']}\n")
            f.write(f"- *Aventuras en las que aparece:* {adv_str}\n\n")
            f.write("---\n\n")
            
        f.write(format_count_section(conjuros))

    print(f"Extraction completed. {len(conjuros)} conjuros extraídos.")

if __name__ == '__main__':
    extract_conjuros()
