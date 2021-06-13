class ListarAsignaciones():
    def __init__(self, DB):
        self.DB = DB 
 
    def run(self):
        cursor = self.DB.cursor()
        cursor.execute("select asignacion_espacios.id, asignacion_espacios.espacio, asignacion_espacios.fecha, asignacion_espacios.hora_inicio, asignacion_espacios.hora_fin, espacio_academico.nombre from asignacion_espacios JOIN espacio_academico ON asignacion_espacios.espacio=espacio_academico.id")
        data = cursor.fetchall()
        cursor.close() 
        return (data)