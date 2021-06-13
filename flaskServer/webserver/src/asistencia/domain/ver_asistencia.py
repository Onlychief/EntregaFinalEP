class VerAsistencia():
    def __init__(self, DB):
        self.DB = DB 
    def run(self, id_espacio):
        cursor = self.DB.cursor()
        cursor.execute ('select asistencia.id, asistencia.falta, asistencia.estudiantes, asistencia.hora_entradaest, asistencia.hora_salidaest, estudiantes.nombres, estudiantes.apellidos from asistencia JOIN estudiantes ON asistencia.estudiantes=estudiantes.id WHERE asignacion_espacios = ?',[id_espacio])
        materias = cursor.fetchall()
        cursor.close()
        return(materias)