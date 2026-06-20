from scraper.constantes import DiaSemana

def cumple_filtro(filtros, grupo):
    if grupo.materia.id not in filtros.lista_materias:
        return False

    if grupo.modalidad not in filtros.modalidades:
        return False

    for dia in DiaSemana:
        for hora_inicio, hora_termino in grupo.horas[dia]:
            if not (hora_inicio >= filtros.hora_inicio_minima and hora_termino <= filtros.hora_termino_maxima):
                return False

    return True


def filtra_grupos(filtros, grupos):
    return [grupo for grupo in grupos if cumple_filtro(filtros, grupo)]

