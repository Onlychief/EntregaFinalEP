from src.docentes.domain.crear_asignacion import CrearAsignaciones
from src.docentes.domain.obtener_id_materia import ObtenerIdMaterias
from flask import request

class CrearAsignacionesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_materia):
        fecha = request.form.get('fecha')
        hora_inicio = request.form.get('hora_inicio')
        hora_final = request.form.get('hora_final')
        asignar_Espacio = CrearAsignaciones(self.DB)
        return (asignar_Espacio.run(id_materia,fecha, hora_inicio,hora_final))      
        
        
        
       