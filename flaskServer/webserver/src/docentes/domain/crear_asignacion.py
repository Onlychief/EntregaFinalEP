class CrearAsignaciones():

    def __init__(self, DB):
        self.DB = DB 
 
    def run(self, materia,fecha,hora_inicio,hora_final):
        cursor = self.DB.cursor()
        cursor.execute('insert into asignacion_espacios(espacio, fecha, hora_inicio, hora_fin) values(?,?,?,?)', (materia, fecha, hora_inicio, hora_final))
        cursor.close()