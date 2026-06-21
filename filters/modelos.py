from scraper.constantes import ModalidadGrupo
from .constantes import HORA_INICIO_MINIMA, HORA_TERMINO_MAXIMA, TODAS_LAS_MODALIDADES

class FiltrosGrupos:
    def __init__(self): 
        self.hora_inicio_minima = HORA_INICIO_MINIMA
        self.hora_termino_maxima = HORA_TERMINO_MAXIMA
        self.modalidades = TODAS_LAS_MODALIDADES

    def __str__(self):
        return (f"Inicio >= {self.hora_inicio_minima}, "
                f"Término <= {self.hora_termino_maxima}, "
                f"Modalidades: {self.modalidades}")


class FiltrosGruposBuilder:
    def __init__(self):
        self._filtros = FiltrosGrupos()

    def con_hora_inicio(self, hora):
        if hora is not None:
            self._filtros.hora_inicio_minima = hora
        return self  

    def con_hora_termino(self, hora):
        if hora is not None:
            self._filtros.hora_termino_maxima = hora
        return self

    def con_modalidades(self, modalidades):
        if modalidades is not None:
            self._filtros.modalidades = modalidades
        return self

    def build(self):
        return self._filtros
