import scraper
from scraper.modelos import Materia
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias, BloqueMaterias
from generator import genera_todos_los_horarios_validos
from filters.modelos import FiltrosGruposBuilder
from filters.opciones import opciones_programa, genera_lista_modalidades
from filters.filtrador_grupos import filtra_grupos

from utils.output import imprime_horarios, imprime_materias_faltantes

def imprime_materias(materias):
    separador = "=" * 15
    print(f"{separador} {CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.nombre} {separador}")
    
    max_len_nombre = max(len(materia.nombre) for materia in materias) if materias else 30
    
    print(f"{'Asignatura':<{max_len_nombre}} | {'ID':<6}")
    print("-" * (max_len_nombre + 9))

    for materia in materias:
        print(f"{materia.nombre:<{max_len_nombre}} | {materia.id:<6}")

def main():
    materias = scraper.obtener_catalogo_materias(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id)

    materias_dict = {}
    for materia in materias:
        materias_dict[materia.id] = materia

    args = opciones_programa()
    numero_maximo_optativas = args.optativas

    filtros = FiltrosGruposBuilder(args.materias).con_hora_inicio(args.hora_inicio).con_hora_termino(args.hora_termino).con_modalidades(genera_lista_modalidades(args.modalidades)).build()
   
    materias_a_usar = filtros.lista_materias
    grupos = []

    for id_materia in materias_a_usar:
        grupos.extend(scraper.obtener_horarios_de_materia(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id, materias_dict[id_materia]))

    horarios_validos = genera_todos_los_horarios_validos(grupos, numero_maximo_optativas)
    imprime_horarios(horarios_validos)

    imprime_materias_faltantes(materias_dict)




if __name__ == "__main__":
    main()
