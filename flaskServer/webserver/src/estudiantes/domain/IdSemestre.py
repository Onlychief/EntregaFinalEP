class idSemestre():
    def __init__(self, DB):
        self.DB = DB
 
    def run(self, semestre):
        cursor = self.DB.cursor()
        cursor.execute('select id from semestre where desc_semestre =?', [semestre])
        id_semestre = cursor.fetchall()
        cursor.close()
        elid = str(id_semestre)

        caracteres = (")","(","'",",","[","]")
        id_limpio = ""

        for letters in elid:
            if letters not in caracteres:
                id_limpio = id_limpio + letters
        return (id_limpio)