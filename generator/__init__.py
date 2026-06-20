from scraper.constantes import DiaSemana 

def se_intersectan_intervalos(a, b, c, d):
    return max(a, c) < min(b, d)

def se_intersectan_horarios(lista_grupos, nuevo_grupo):
    for grupo in lista_grupos:
        for dia in DiaSemana:
            if grupo.horas.get(dia) and nuevo_grupo.horas.get(dia):
                for a, b in grupo.horas[dia]:
                    for c, d in nuevo_grupo.horas[dia]:
                        if se_intersectan_intervalos(a, b, c, d):
                            return True
    return False

def agrega_grupo(lista_grupos_actuales, grupos, idx, ids_materias, grupos_finales):
    if lista_grupos_actuales:
        grupos_finales.append(lista_grupos_actuales)

    for i in range(idx, len(grupos)):
        grupo = grupos[i]

        if grupo.materia.id in ids_materias:
            continue

        if not se_intersectan_horarios(lista_grupos_actuales, grupo):
            nuevos_grupos = lista_grupos_actuales + [grupo]
            nuevas_materias = ids_materias | {grupo.materia.id} 
            agrega_grupo(nuevos_grupos, grupos, i + 1, nuevas_materias, grupos_finales)


def genera_todos_los_horarios_validos(grupos):
    horarios_validos = []
    agrega_grupo([], grupos, 0, set(), horarios_validos)
    return horarios_validos
