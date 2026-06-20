from enum import Enum

class DiaSemana(Enum):
    LUNES     = (0, "lu", "Lunes")
    MARTES    = (1, "ma", "Martes")
    MIERCOLES = (2, "mi", "Miércoles")
    JUEVES    = (3, "ju", "Jueves")
    VIERNES   = (4, "vi", "Viernes")
    SABADO    = (5, "sa", "Sábado")
    DOMINGO   = (6, "do", "Domingo")

    def __init__(self, id_num, corto, largo):
        self.id = id_num
        self.corto = corto
        self.largo = largo

    @classmethod
    def desde_id(cls, id_num):
        for dia in cls:
            if dia.id == id_num:
                return dia
        raise ValueError(f"ID de día no válido: {id_num}")

class ModalidadGrupo(Enum):
    PRESENCIAL = "Presencial"
    VIRTUAL = "Virtual"
    MIXTA = "Mixta"
    DESCONOCIDA = "Desconocida"

class CarrerasFacultadDeCiencias(Enum):
    CIENCIAS_DE_LA_COMPUTACION = (1556, "Ciencias de la Computación")

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class BloqueMaterias(Enum):
    PRIMER_SEMESTRE = "Primer Semestre"
    SEGUNDO_SEMESTRE = "Segundo Semestre"
    TERCER_SEMESTRE = "Tercer Semestre"
    CUARTO_SEMESTRE = "Cuarto Semestre"
    QUINTO_SEMESTRE = "Quinto Semestre"
    SEXTO_SEMESTRE = "Sexto Semestre"
    SEPTIMO_SEMESTRE = "Septimo Semestre"
    OCTAVO_SEMESTRE = "Octavo Semestre"
    OPTATIVA = "Optativas"
    DESCONOCIDO = "Desconocido"

    @classmethod
    def from_string(cls, s):
        for bloque in cls:
            if bloque.value == s:
                return bloque
        return BloqueMaterias.DESCONOCIDO

SEMESTRE = "20271"


