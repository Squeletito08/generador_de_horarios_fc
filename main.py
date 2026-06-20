import scraper
from scraper.modelos import Materia
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias

from generator import genera_todos_los_horarios_validos

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
    
    imprime_materias(materias)

    print("Introduce los ids de las materias a trabajar separadas por comas: ", end="")
    materias_a_usar = input().replace(" ", "").split(",")

    grupos = []

    for id_materia in materias_a_usar:
        grupos.extend(scraper.obtener_horarios_de_materia(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id, materias_dict[int(id_materia)]))

    horarios_validos = genera_todos_los_horarios_validos(grupos)

    print(f"Numero de horarios validos: {len(horarios_validos)}")

    for horario in horarios_validos:
        print("=" * 50)
        for grupo in horario:
            print(grupo)
            print()
        print()








if __name__ == "__main__":
    main()
