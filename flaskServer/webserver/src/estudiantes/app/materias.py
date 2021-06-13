from src.estudiantes.domain.materias import ListarMaterias

class VerMateriasCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_semestre):
        listarMaterias = ListarMaterias(self.DB)
        return listarMaterias.run(id_semestre)