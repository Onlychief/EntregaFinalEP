from src.estudiantes.domain.eliminar import EliminarEstudiantes

class EliminarEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_estudiante):
        eliminarEstudiantes = EliminarEstudiantes(self.DB)
        eliminarEstudiantes.run(id_estudiante)