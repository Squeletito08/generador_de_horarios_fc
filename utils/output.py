from .constantes import RESET,BOLD,GREEN,CYAN,YELLOW,GRAY,MATERIAS_CURSADAS_PATH
from scraper.constantes import BloqueMaterias

def _obten_ids_de_materias_cursadas():
    ids_materias = []
    with open(MATERIAS_CURSADAS_PATH, "r") as file:
        for line in file: 
            id = line.strip()
            ids_materias.append(int(id))
    return ids_materias

def obten_materias_faltantes(materias):
    materias_cursadas = set(_obten_ids_de_materias_cursadas())
    ids_faltantes = materias.keys() - materias_cursadas
    return {id_materia: materias[id_materia] for id_materia in ids_faltantes}

def filtra_materias_por_bloque(materias, bloques, incluye=True):
    return {
        id_mat: mat 
        for id_mat, mat in materias.items() 
        if (mat.bloque in bloques) == incluye
    }

def filtra_materias_por_semestre(materias):
    materias_por_semestre = {bloque: [] for bloque in BloqueMaterias}
    for _, materia in materias.items():
        materias_por_semestre[materia.bloque].append(materia)
    return materias_por_semestre

def _generar_cabecera_centrada(texto, ancho_total=80, simbolo="=", color_borde=GRAY, color_texto=BOLD+CYAN):
    espacio_disponible = max(0, ancho_total - len(texto) - 2)
    mitad = espacio_disponible // 2
    
    borde_izq = simbolo * mitad
    borde_der = simbolo * (espacio_disponible - mitad) 
    
    linea = f"{color_borde}{borde_izq}{RESET} {color_texto}{texto}{RESET} {color_borde}{borde_der}{RESET}"
    return linea, color_borde + (simbolo * ancho_total) + RESET


def imprime_materias_faltantes(materias):
    materias_faltantes = obten_materias_faltantes(materias)
    materias_por_semestre = filtra_materias_por_semestre(materias_faltantes)

    for semestre, lista_materias in materias_por_semestre.items():
        if not lista_materias:
            continue 
        cabecera, linea_cierre = _generar_cabecera_centrada(semestre.value, ancho_total=70, simbolo="=")
        
        print(cabecera)
        for materia in lista_materias:
            print(f"  {GRAY}[{materia.id}]{RESET} {materia.nombre}")
        print(linea_cierre)
        print()


def imprime_horarios(horarios):
    for ctd, horario in enumerate(horarios, 1):
        texto_horario = f"OPCIÓN DE HORARIO #{ctd}"
        
        cabecera, linea_cierre = _generar_cabecera_centrada(
            texto_horario, ancho_total=75, simbolo="*", color_borde=YELLOW, color_texto=BOLD+YELLOW
        )
        
        print(cabecera)
        print() 
        
        for grupo in horario:
            grupo_str = str(grupo).replace("\n", "\n  ")
            print(f"  {grupo_str}")
            print()
            
        print(linea_cierre)
        print()
