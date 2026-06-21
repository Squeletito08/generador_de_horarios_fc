from .constantes import MATERIAS_CURSADAS_PATH
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


