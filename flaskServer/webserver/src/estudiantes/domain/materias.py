class ListarMaterias():

    def __init__(self, DB):
        self.DB = DB

    def run(self, id_semestre):
        cursor = self.DB.cursor()
        cursor.execute ('select espacio_academico.id, espacio_academico.nombre, espacio_academico.semestre, espacio_academico.docente, semestre.desc_semestre from espacio_academico JOIN semestre ON espacio_academico.semestre=semestre.id WHERE espacio_academico.semestre = ? ', [id_semestre])
        materias_por_semestre = cursor.fetchall()
        cursor.close()
        return(materias_por_semestre)