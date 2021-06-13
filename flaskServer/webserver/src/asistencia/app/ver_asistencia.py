from src.asistencia.domain.ver_asistencia import VerAsistencia

class VerAsistenciaCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self, id_espacio):
        asistencia = VerAsistencia(self.DB)
        return(asistencia.run(id_espacio))