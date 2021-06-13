class ObtenerIdMaterias():
    
    def __init__(self, DB):
        self.DB = DB

    def run(self, id_materia):
        cursor = self.DB.cursor()
        cursor.execute("select id, nombre from espacio_academico where id =?", [id_materia])
        data = cursor.fetchall()
        cursor.close() 
        return (data)