class AsistirAClase():
    def __init__(self, DB):
        self.DB = DB 
    def run(self,falta,espacio,estudiante,hora_entradaest,hora_salidaest):     
        cursor = self.DB.cursor()
        cursor.execute('insert into asistencia(falta, asignacion_espacios, estudiantes, hora_entradaest, hora_salidaest) values(?,?,?,?,?) ', (falta, espacio, estudiante, hora_entradaest, hora_salidaest))
        cursor.close()