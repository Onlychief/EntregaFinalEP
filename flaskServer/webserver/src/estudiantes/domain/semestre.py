class ConsultaSemestre():
    def __init__(self, DB):
        self.DB = DB

    def run (self, id_estudiante):
        cursor = self.DB.cursor()
        cursor.execute('select semestre from estudiantes where id =?', [id_estudiante])
        id_semestre = cursor.fetchall()
        cursor.close()
        elid = str(id_semestre)

        caracteres = (")","(","'",",","[","]")
        id_limpio = ""

        for letters in elid:
            if letters not in caracteres:
                id_limpio = id_limpio + letters
        return (id_limpio)