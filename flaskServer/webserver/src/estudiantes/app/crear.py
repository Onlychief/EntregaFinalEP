from src.estudiantes.domain.crear import CrearEstudiantes
from src.estudiantes.domain.IdSemestre import idSemestre
from flask import request
import hashlib

class CrearEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        celular = request.form.get('celular')
        correo = request.form.get('correo')
        clave = request.form.get('clave')
        semestref = request.form.get('semestre')
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()

        creandoEstudiantes = CrearEstudiantes(self.DB)
        consultarIdSemestre = idSemestre(self.DB)
        
        semestre = consultarIdSemestre.run(semestref)
        creandoEstudiantes.run(nombre, apellido, celular, correo, claveEncriptada,semestre)