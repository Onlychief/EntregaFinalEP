from src.docentes.domain.eliminar_programada import EliminarProgramada

class EliminarProgramadaCase:
    def __init__(self, DB):
        self.DB = DB  
    def run(self, id_clase):
        eliminarProgramada = EliminarProgramada(self.DB)
        eliminarProgramada.run(id_clase)
      