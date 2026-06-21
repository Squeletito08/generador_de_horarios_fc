from .constantes import RESET,BOLD,GREEN,CYAN,YELLOW,GRAY,MATERIAS_CURSADAS_PATH
from scraper.constantes import BloqueMaterias, CarrerasFacultadDeCiencias
from .utils import obten_materias_faltantes, filtra_materias_por_semestre

def _generar_cabecera_centrada(texto, ancho_total=80, simbolo="=", color_borde=GRAY, color_texto=BOLD+CYAN):
    espacio_disponible = max(0, ancho_total - len(texto) - 2)
    mitad = espacio_disponible // 2
    
    borde_izq = simbolo * mitad
    borde_der = simbolo * (espacio_disponible - mitad) 
    
    linea = f"{color_borde}{borde_izq}{RESET} {color_texto}{texto}{RESET} {color_borde}{borde_der}{RESET}"
    return linea, color_borde + (simbolo * ancho_total) + RESET


def imprime_materias_faltantes(materias):
    materias_faltantes = obten_materias_faltantes(materias)
    imprime_materias(materias_faltantes)

def imprime_materias(materias):
    materias_por_semestre = filtra_materias_por_semestre(materias)

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
