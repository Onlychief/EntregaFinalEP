from src.docentes.domain.asignaciones import ListarAsignaciones

class ListarAsignacionesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        listarAsignaciones = ListarAsignaciones(self.DB)
        return listarAsignaciones.run()