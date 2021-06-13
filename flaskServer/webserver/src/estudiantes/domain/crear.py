class CrearEstudiantes():
    def __init__(self, DB):
        self.DB = DB

    def run(self,nombre, apellido, celular,correo,clave,semestre):
        cursor = self.DB.cursor()
        cursor.execute('insert into estudiantes(nombres, apellidos,celular,correo,clave,semestre) values(?,?,?,?,?,?)', (nombre, apellido, celular,correo,clave,semestre))
        cursor.close()