class EliminarEstudiantes():
    def __init__(self, DB):
        self.DB = DB

    def run(self, id_estudiante):   
        cursor = self.DB.cursor()
        cursor.execute('DELETE FROM estudiantes WHERE id = ?', [id_estudiante])
        cursor.close()