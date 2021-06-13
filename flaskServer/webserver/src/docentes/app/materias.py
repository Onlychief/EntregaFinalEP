from src.docentes.domain.materias import ListarMateriasDocente

class VerMateriasDocenteCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_docente):
        listarMaterias = ListarMateriasDocente(self.DB)
        return listarMaterias.run(id_docente)