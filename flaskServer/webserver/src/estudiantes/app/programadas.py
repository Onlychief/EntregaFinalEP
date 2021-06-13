from src.estudiantes.domain.programadas import ClasesProgramadas
from datetime import datetime
import time

class VerProgramadasCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_semestre):
        fecha_actual = datetime.now().date()
        hora_fin = time.strftime('%H:%M:%S', time.localtime())
        listarProgramadas = ClasesProgramadas(self.DB)
        return(listarProgramadas.run(fecha_actual, hora_fin,int(id_semestre)))
