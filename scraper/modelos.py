from .constantes import DiaSemana  
from functools import total_ordering

class Materia:
    def __init__(self, nombre, id_materia):
        self.nombre = nombre 
        self.id = id_materia 

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"

    def __repr__(self):
        return f"Materia(id={self.id}, nombre='{self.nombre}')"

@total_ordering
class Horario:
    def __init__(self, hora_inicio, hora_termino):
        self.dias_clase = [False] * len(DiaSemana)
        self.hora_inicio = hora_inicio  
        self.hora_termino = hora_termino 

    def __str__(self):
        dias = [DiaSemana.desde_id(i).corto for i, da_clase in enumerate(self.dias_clase) if da_clase]
        dias_str = ",".join(dias) if dias else "Sin días asignados"
        
        str_inicio = self.hora_inicio.strftime("%H:%M") if self.hora_inicio else "--:--"
        str_termino = self.hora_termino.strftime("%H:%M") if self.hora_termino else "--:--"
        
        return f"[{dias_str}] {str_inicio} - {str_termino}"

    def __repr__(self):
        return f"Horario({self.hora_inicio} a {self.hora_termino})"

    def __eq__(self, other):
        if not isinstance(other, Horario):
            return NotImplemented
        return self.dias_clase == other.dias_clase and self.hora_inicio == other.hora_inicio and self.hora_termino == other.hora_termino

    def __lt__(self, other):
        if not isinstance(other, Horario):
            return NotImplemented
        return self.hora_termino <= other.hora_inicio 


class Profesor:
    def __init__(self, nombre, primer_apellido, segundo_apellido, cargo_profesor="Profesor"):
        self.nombre = nombre 
        self.primer_apellido = primer_apellido 
        self.segundo_apellido = segundo_apellido
        self.cargo_profesor = cargo_profesor

    def __str__(self):
        apellido_2 = f" {self.segundo_apellido}" if self.segundo_apellido else ""
        nombre_completo = f"{self.nombre} {self.primer_apellido}{apellido_2}".strip()
        
        if not nombre_completo: 
            return f"[{self.cargo_profesor}]"
            
        return f"[{self.cargo_profesor}] {nombre_completo}"

    def __repr__(self):
        return f"Profesor(nombre='{self.nombre}', cargo='{self.cargo_profesor}')"


class Grupo:
    def __init__(self, materia, id_grupo, clave, cupo, tiene_presentacion):
        self.materia = materia  
        self.id = id_grupo
        self.clave = clave
        self.cupo = cupo
        self.tiene_presentacion = tiene_presentacion
        self.profesores = []
        self.horas = {dia: [] for dia in DiaSemana}

    def agrega_profesor(self, profesor, horario):
        self.profesores.append((profesor, horario))
        self._agrega_horas(horario)

    def _agrega_horas(self, horario):
        for dia in DiaSemana:
            if horario.dias_clase[dia.id]:
                self.horas[dia].append((horario.hora_inicio, horario.hora_termino))

    def __str__(self):
        presentacion = "Sí" if self.tiene_presentacion else "No"

        lineas_profesores = []
        for prof, hor in self.profesores:
            lineas_profesores.append(f"    - {prof} -> {hor}")
        profesores_str = "\n".join(lineas_profesores) if lineas_profesores else "    - Sin profesores asignados"

        return (
            f"Grupo {self.clave} | Materia: {self.materia.nombre}\n"
            f"  Cupo: {self.cupo} | Presentación: {presentacion}\n"
            f"  Asignaciones:\n{profesores_str}"
        )

    def __repr__(self):
        return f"Grupo(clave='{self.clave}', materia_id={self.materia.id})"
