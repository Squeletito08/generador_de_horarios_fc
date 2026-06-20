import scraper
from scraper.modelos import Materia
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias
from generator import genera_todos_los_horarios_validos
from filters.opciones import opciones_programa
from filters.filtrador_grupos import filtra_grupos

def imprime_materias(materias):
    separador = "=" * 15
    print(f"{separador} {CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.nombre} {separador}")
    
    max_len_nombre = max(len(materia.nombre) for materia in materias) if materias else 30
    
    print(f"{'Asignatura':<{max_len_nombre}} | {'ID':<6}")
    print("-" * (max_len_nombre + 9))

    for materia in materias:
        print(f"{materia.nombre:<{max_len_nombre}} | {materia.id:<6}")

def main():
    materias = scraper.obtener_catalogo_materias(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id)

    materias_dict = {}
    for materia in materias:
        materias_dict[materia.id] = materia
    
    filtros = opciones_programa()

    materias_a_usar = filtros.lista_materias
    grupos = []

    for id_materia in materias_a_usar:
        grupos.extend(scraper.obtener_horarios_de_materia(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id, materias_dict[id_materia]))

    grupos = filtra_grupos(filtros, grupos)
    horarios_validos = genera_todos_los_horarios_validos(grupos)

    for horario in horarios_validos:
        print("=" * 100)
        for grupo in horario:
            print(grupo)
            print()








if __name__ == "__main__":
    main()
