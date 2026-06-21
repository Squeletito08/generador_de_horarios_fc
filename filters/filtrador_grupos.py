from scraper.constantes import DiaSemana

def cumple_filtro(filtros, grupo):
    if grupo.modalidad not in filtros.modalidades:
        return False

    for dia in DiaSemana:
        # Voy a ignorar los fines de semana (sabdo xd)
        if dia == DiaSemana.DOMINGO or dia == DiaSemana.SABADO:
            continue
        for hora_inicio, hora_termino in grupo.horas[dia]:
            if not (hora_inicio >= filtros.hora_inicio_minima and hora_termino <= filtros.hora_termino_maxima):
                return False

    return True


def filtra_grupos(filtros, grupos):
    return [grupo for grupo in grupos if cumple_filtro(filtros, grupo)]

