import json
from datetime import datetime
from bs4 import BeautifulSoup
from .modelos import Materia, Grupo, Profesor, Horario
from .constantes import DiaSemana

def _extraer_json_de_script(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    script_tag = soup.find("script", type="application/json")

    if not script_tag or not script_tag.string:
        raise ValueError("No se encontró la etiqueta <script type='application/json'>")

    return json.loads(script_tag.string)

def extraer_materias(html_content):
    data_json = _extraer_json_de_script(html_content)
    materias_con_codigo = []
    grupos_por_plan = data_json["querygruposplan"]["data"]["grupos_por_plan"]

    for grupo in grupos_por_plan:
        for bloque in grupo["plan__grupos_bloque"]:
            materia_data = bloque["asignatura__asignatura"]
            materia_objeto = Materia(
                nombre=materia_data["asignatura__nombre"],
                id_materia=materia_data["asignatura__id"]
            )
            materias_con_codigo.append(materia_objeto)

    return materias_con_codigo

def crea_grupo(json_grupo, materia):
    return Grupo(
        materia=materia,
        id_grupo=json_grupo.get("grupo__id"),
        clave=json_grupo.get("grupo__clave"),
        cupo=json_grupo.get("grupo__cupo", 0),
        tiene_presentacion=json_grupo.get("grupo__tiene_presentacion", False)
    )

def obtener_cargo_profesor(profesor_data):
    horarios = profesor_data.get("profesor__horarios", [])
    if not horarios:
        return "Profesor"
    return horarios[0].get("grupo__cargo", {}).get("cargo__nombre_corto", "Profesor")

def crea_profesor(profesor_data):
    persona = profesor_data.get("profesor__persona")

    if not persona:
        return None

    cargo = obtener_cargo_profesor(profesor_data)

    primer_apellido = persona.get("persona__apellido_1") or ""
    segundo_apellido = persona.get("persona__apellido_2") or ""

    if persona:
        return Profesor(
            nombre=persona.get("persona__nombre", "").strip(),
            primer_apellido=primer_apellido.strip(),
            segundo_apellido=segundo_apellido.strip(), 
            cargo_profesor=cargo
        )

    return Profesor(nombre=cargo, primer_apellido="", segundo_apellido="", cargo_profesor=cargo)

def transforma_hora_a_tiempo(string_hora):
    if not string_hora:
        return None
    return datetime.strptime(string_hora, "%H:%M:%S").time()

def crea_horario(profesor_data):
    horarios = profesor_data.get("profesor__horarios", [])
    if not horarios:
        return None

    primer_horario = horarios[0]
    hora_inicio_str = primer_horario.get("profesor_horario__hora_inicio")
    hora_termino_str = primer_horario.get("profesor_horario__hora_termino")
    if not hora_inicio_str or not hora_termino_str:
        return None

    hora_inicio = transforma_hora_a_tiempo(hora_inicio_str)
    hora_termino = transforma_hora_a_tiempo(hora_termino_str)
    nuevo_horario = Horario(hora_inicio, hora_termino)

    for dia_semana in DiaSemana:
        da_clase = primer_horario.get(f"profesor_horario__{dia_semana.corto}", False)
        nuevo_horario.dias_clase[dia_semana.id] = da_clase

    return nuevo_horario

def extraer_horarios(html_materia_content, materia):
    data_json = _extraer_json_de_script(html_materia_content)
    grupos_por_asignatura = data_json["queryhorarios"]["data"]["grupos_por_asignatura"]
    grupos = []

    for grupo_data in grupos_por_asignatura:
        grupo = crea_grupo(grupo_data["grupo__grupo"], materia)
        for profesor_data in grupo_data.get("grupo__profesores", []):
            nuevo_profesor = crea_profesor(profesor_data)
            nuevo_horario = crea_horario(profesor_data)
            if nuevo_horario:
                grupo.agrega_profesor(nuevo_profesor, nuevo_horario)
        grupos.append(grupo)

    return grupos
