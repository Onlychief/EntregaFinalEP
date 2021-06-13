class IngresoEstudiantes():
    def __init__(self, DB):
        self.DB = DB

    def run(self, correo, clave):
        cursor = self.DB.cursor()
        cursor.execute('select id from estudiantes WHERE correo=? AND clave =?', (correo,clave))
        id_usuario = cursor.fetchall()
        cursor.close()
        elid = str(id_usuario)

        caracteres = (")","(","'",",","[","]")
        id_limpio = ""

        for letters in elid:
            if letters not in caracteres:
                id_limpio = id_limpio + letters
        return (id_limpio)