import argparse
from datetime import datetime
from .modelos import FiltrosGrupos, FiltrosGruposBuilder

def validar_hora(cadena_hora):
    try:
        return datetime.strptime(cadena_hora, "%H:%M").time()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Formato de hora no válido: '{cadena_hora}'. Debe ser HH:MM (ej. 07:30)")

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
            "materias", 
            nargs="+",
            type=int,
            help="Lista de materias (ids) a considerar"
    )

    args = parser.parse_args()

    return FiltrosGruposBuilder(args.materias).con_hora_inicio(args.hora_inicio).con_hora_termino(args.hora_termino).con_modalidades(args.modalidades).build()
    


