class ClasesProgramadas():
    
    def __init__(self, DB):
        self.DB = DB

    def run(self,fecha_actual,hora_fin,id_semestre):
        cursor = self.DB.cursor()
        cursor.execute("select asignacion_espacios.id, asignacion_espacios.espacio, asignacion_espacios.fecha, asignacion_espacios.hora_inicio, asignacion_espacios.hora_fin, espacio_academico.nombre, espacio_academico.semestre from asignacion_espacios JOIN espacio_academico ON asignacion_espacios.espacio=espacio_academico.id WHERE fecha >= ? AND hora_fin > ? AND espacio_academico.semestre=?",[fecha_actual, hora_fin,id_semestre])
        data = cursor.fetchall()
        cursor.close() 
        return (data)