import scraper
from scraper.modelos import Materia
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias, BloqueMaterias
from generator import genera_todos_los_horarios_validos
from filters.modelos import FiltrosGruposBuilder
from filters.opciones import opciones_programa, genera_lista_modalidades
from filters.filtrador_grupos import filtra_grupos

from utils.constantes import OPTATIVAS_FALTANTES
from utils.output import imprime_horarios, imprime_materias

from utils.horarios import crea_horarios 
from utils.utils import filtra_materias_por_bloque, obten_materias_faltantes

def main():
    materias = scraper.obtener_catalogo_materias(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id)

    materias_dict = {}
    for materia in materias:
        materias_dict[materia.id] = materia

    args = opciones_programa()
    numero_maximo_optativas = args.optativas

    filtros = FiltrosGruposBuilder().con_hora_inicio(args.hora_inicio).con_hora_termino(args.hora_termino).con_modalidades(genera_lista_modalidades(args.modalidades)).build()

    if args.materias:
        materias_a_usar = {id: materia for id, materia in materias_dict.items() if id in args.materias}
        horarios = crea_horarios(materias_a_usar, filtros, numero_maximo_optativas)
    else:
        materias_faltantes = obten_materias_faltantes(materias_dict)
        # no_optativas = filtra_materias_por_bloque(materias_faltantes, [BloqueMaterias.OPTATIVA], incluye=False)
        imprime_materias(materias_faltantes)
        horarios = crea_horarios(materias_faltantes, filtros, OPTATIVAS_FALTANTES)

    imprime_horarios(horarios)

if __name__ == "__main__":
    main()
