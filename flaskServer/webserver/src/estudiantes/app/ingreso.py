from src.estudiantes.domain.ingreso import IngresoEstudiantes
from flask import request
import hashlib

class IngresoEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):

        correo = request.form.get('correo')
        clave = request.form.get('clave')
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()
        ingresoEstudiantes = IngresoEstudiantes(self.DB)
        id_estudiante = ingresoEstudiantes.run(correo,claveEncriptada)
        return (id_estudiante)

      