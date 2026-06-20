from .fetcher import obtener_html_indice, obtener_html_materia
from .parser import extraer_materias, extraer_horarios

def obtener_catalogo_materias(semestre, id_carrera):
    html = obtener_html_indice(semestre, id_carrera)
    return extraer_materias(html)

def obtener_horarios_de_materia(semestre, id_carrera, materia):
    html = obtener_html_materia(semestre, id_carrera, materia)
    return extraer_horarios(html, materia)
