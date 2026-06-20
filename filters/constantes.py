from datetime import datetime 
from scraper.constantes import ModalidadGrupo

HORA_INICIO_MINIMA =  datetime.strptime("07:00", "%H:%M").time() 
HORA_TERMINO_MAXIMA = datetime.strptime("22:00", "%H:%M").time()
TODAS_LAS_MODALIDADES = [ModalidadGrupo.PRESENCIAL, ModalidadGrupo.VIRTUAL, ModalidadGrupo.MIXTA]
