import posixpath
import requests

BASE_URL = "https://www.fciencias.unam.mx"
DOCENCIA = "docencia"
HORARIOS = "horarios"
INDICEPLAN = "indiceplan"

def obtener_html_indice(semestre, id_carrera):
    url = posixpath.join(BASE_URL, DOCENCIA, HORARIOS, INDICEPLAN, str(semestre), str(id_carrera))
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def obtener_html_materia(semestre, id_carrera, materia):
    url_materia = posixpath.join(BASE_URL, DOCENCIA, HORARIOS, str(semestre), str(id_carrera), str(materia.id))
    response = requests.get(url_materia)
    response.raise_for_status()
    return response.text
