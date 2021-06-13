from src.estudiantes.domain.semestre import ConsultaSemestre

class ConsultaSemestreCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self, id_estudiante):
        consultaSemestre = ConsultaSemestre(self.DB)
        id_semestre = consultaSemestre.run(id_estudiante)
        return (id_semestre)