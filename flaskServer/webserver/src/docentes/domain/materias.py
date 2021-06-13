class ListarMateriasDocente():
    
    def __init__(self, DB):
        self.DB = DB

    def run(self,id_docente):
        cursor = self.DB.cursor()
        cursor.execute ('select espacio_academico.id, espacio_academico.nombre, espacio_academico.semestre, semestre.desc_semestre from espacio_academico JOIN semestre ON espacio_academico.semestre = semestre.id where espacio_academico.docente = ?', [id_docente])
        materias = cursor.fetchall()
        cursor.close()
        return(materias)