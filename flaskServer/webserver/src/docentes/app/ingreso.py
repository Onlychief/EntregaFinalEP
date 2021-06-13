from src.docentes.domain.ingreso import IngresoDocentes
from flask import request
import hashlib

class IngresoDocentesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        correo = request.form.get('correo')
        clave = request.form.get('clave')
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()
        ingresoDocentes = IngresoDocentes(self.DB)
        id_docente = ingresoDocentes.run(correo,claveEncriptada)
        return (id_docente)