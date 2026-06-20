import scraper
from scraper.modelos import Materia
from scraper.constantes import SEMESTRE, CarrerasFacultadDeCiencias

def main():
    materias = scraper.obtener_catalogo_materias(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id)
    grupos = []
    for materia in materias:
        grupos.extend(scraper.obtener_horarios_de_materia(SEMESTRE, CarrerasFacultadDeCiencias.CIENCIAS_DE_LA_COMPUTACION.id, materia))

    for grupo in grupos:
        print(grupo)
        print()

if __name__ == "__main__":
    main()
