from src.docentes.domain.obtener_id_materia import ObtenerIdMaterias

class ObtenerIdMateriasCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_materia):
        docentesModel = ObtenerIdMaterias(self.DB)
        return (docentesModel.run(id_materia))