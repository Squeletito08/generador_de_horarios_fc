from .constantes import MATERIAS_CURSADAS_PATH

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

def filtra_materias_por_bloque(materias, bloque):
    return {id: materia for id, materia in materias.items() if materia.bloque == bloque}    






