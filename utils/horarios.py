from .utils import obten_materias_faltantes 
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias
from scraper import obtener_horarios_de_materia
from filters.filtrador_grupos import filtra_grupos
from generator import genera_todos_los_horarios_validos
from .constantes import OPTATIVAS_FALTANTES

def crea_horarios(materias, filtros, numero_maximo_optativas):
    grupos = []

    for _, materia in materias.items():
        grupos.extend(obtener_horarios_de_materia(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id, materia))
    grupos = filtra_grupos(filtros, grupos)

    return genera_todos_los_horarios_validos(grupos, numero_maximo_optativas)






