import argparse
from datetime import datetime
from .modelos import FiltrosGrupos, FiltrosGruposBuilder
from scraper.constantes import ModalidadGrupo

def validar_hora(cadena_hora):
    try:
        return datetime.strptime(cadena_hora, "%H:%M").time()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Formato de hora no válido: '{cadena_hora}'. Debe ser HH:MM (ej. 07:30)")

def genera_lista_modalidades(modalidades):
    set_modalidades = set()

    for modalidad in modalidades:
        match modalidad:
            case "p":
                set_modalidades.add(ModalidadGrupo.PRESENCIAL)
            case "v":
                set_modalidades.add(ModalidadGrupo.VIRTUAL)
            case "m":
                set_modalidades.add(ModalidadGrupo.MIXTA)

    if set_modalidades:
        return list(set_modalidades)
    return None

def opciones_programa():
    parser = argparse.ArgumentParser(
        prog="Generador de horarios Facultad de Ciencias",
        description="Filtra y genera combinaciones de horarios sin colisiones."
    ) 
    
    parser.add_argument(
        "-hi", "--hora-inicio", 
        type=validar_hora,
        default="07:00", 
        help="A partir de qué hora pueden comenzar las clases (formato HH:MM)"
    )
    
    parser.add_argument(
        "-ht", "--hora-termino", 
        type=validar_hora,
        default="22:00",  
        help="Hasta qué hora pueden terminar las clases (formato HH:MM)"
    )
    
    parser.add_argument(
        "-mo", "--modalidades", 
        nargs="+", 
        choices=["p", "v", "m"], 
        default=["p", "v", "m"],
        help="Modalidades a considerar: (p)resencial, (v)irtual, (m)ixta"
    )

    parser.add_argument(
            "-op", "--optativas",
            type=int,
            default=1,
            help="Máximo número de optativas a considerar en un horario"
            )

    parser.add_argument(
            "-ma",
            "--materias", 
            nargs="+",
            type=int,
            required=True,
            help="Lista de materias (ids) a considerar"
    )

    args = parser.parse_args()
    return args

