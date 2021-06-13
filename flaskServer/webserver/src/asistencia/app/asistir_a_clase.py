from src.asistencia.domain.asistir_a_clase import AsistirAClase
from datetime import datetime
import time

class AsistirAClaseCase:
    def __init__(self, DB):
        self.DB = DB
    def run (self, id_espacio,id_estudiante):

        hora_entrada = time.strftime('%H:%M:%S', time.localtime())
        hora_salida = time.strftime('%H:%M:%S', time.localtime())
        asistencia = AsistirAClase(self.DB)
        asistencia.run("Asistió", id_espacio, id_estudiante, hora_entrada, hora_salida)