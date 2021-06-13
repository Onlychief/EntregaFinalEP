class EliminarProgramada():
    
    def __init__(self, DB):
        self.DB = DB     
    def run(self, id_clase):   
        cursor = self.DB.cursor()
        cursor.execute('DELETE FROM asignacion_espacios WHERE id = ?', [id_clase])
        cursor.close()