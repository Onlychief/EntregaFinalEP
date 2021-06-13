from flask import render_template, request, redirect, url_for,Flask, session
from src.shared.infra.mariadb import DB
from src.estudiantes.app.listar  import *
from src.estudiantes.app.crear import *
from src.estudiantes.app.eliminar import *
from src.estudiantes.app.ingreso import *
from src.estudiantes.app.semestre import *
from src.estudiantes.app.materias import *
from src.estudiantes.app.programadas import *
from src.docentes.app.materias import *
from src.docentes.app.ingreso import *
from src.docentes.app.asignaciones import *
from src.docentes.app.crear_asignaciones import *
from src.docentes.app.obtener_id_materia import *
from src.docentes.app.eliminarprogramada import *
from src.asistencia.app.asistir_a_clase import *
from src.asistencia.app.ver_asistencia import *

app = Flask(__name__, template_folder = 'template')
app.secret_key = "Jhonyc"

@app.route('/inicio', methods =['GET'])
def inicio():
    if request.method == 'GET':
        return render_template('/docentes/inicio.html')

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listarEstudianteCase = ListarEstudiantesCase(DB)
    listarEstudianteCaselista = listarEstudianteCase.run()
    return render_template('/estudiantes/ver_estudiantes.html', listarEstudianteCaselista = listarEstudianteCaselista)

@app.route('/crear_estudiantes', methods=['POST','GET'])
def crear_estudiantes():
    if request.method == 'GET':
        return render_template('/estudiantes/registro.html')
    else:
        if request.method == 'POST':
            estudiantesModel = CrearEstudiantesCase(DB)
            estudiantesModel.run()
            return redirect(url_for('listar_estudiantes'))

@app.route('/estudiantes/eliminar/<id_estudiante>', methods =['GET', 'POST'])
def estudiantes_eliminar(id_estudiante):
    if request.method == 'GET':
        estudiantesModel = EliminarEstudiantesCase(DB)
        estudiantesModel.run(id_estudiante)
        return redirect(url_for('listar_estudiantes'))

@app.route('/ingreso_estudiantes', methods =['GET', 'POST'])
def login_estudiante():
    
    if request.method == 'GET':
        return render_template('/estudiantes/ingreso_estudiantes.html')
    else:
        estudiantesConsulta = IngresoEstudiantesCase(DB)
        id_estudiante =estudiantesConsulta.run()
        semestreConsulta = ConsultaSemestreCase(DB)
        id_semestre = semestreConsulta.run(id_estudiante)
        user = id_estudiante
        semestre = id_semestre
        session["user"] = user
        session["semestrea"] = semestre

        if user == "":
            return redirect(url_for("login_estudiante"))
        else:
            return redirect(url_for("ver_materias_semestre"))

@app.route('/ver_materias_semestre', methods =['GET', 'POST'])
def ver_materias_semestre():
    if "semestrea" in session:
        id_semestreA = session["semestrea"]

        if request.method == 'GET':
            verMaterias = VerMateriasCase(DB)
            materias_semestre = verMaterias.run(id_semestreA)
            return render_template('estudiantes/ver_materias_semestre.html', materias_semestre = materias_semestre)
    else:
        return redirect(url_for('login_estudiante'))

@app.route('/clases_programadas', methods =['GET', 'POST'])
def clases_programadas():
    if "semestrea" in session:
        id_semestre = session["semestrea"]
        if request.method == 'GET':
            clasesModel = VerProgramadasCase(DB)
            asignaciones = clasesModel.run(id_semestre)
            return render_template('estudiantes/ver_asignaciones.html', asignaciones = asignaciones)
    else:
        return redirect(url_for('login_estudiante'))

@app.route('/ingreso_docente', methods =['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('/docentes/ingreso_docente.html')
    else:
        docentesModel = IngresoDocentesCase(DB)
        id_docente = docentesModel.run()
        docente = id_docente
        session["docente"] = docente
        if docente == "":
           return redirect(url_for("login"))
        else:
            return redirect(url_for("ver_materias_docente"))

@app.route('/ver_materias_docente', methods =['GET', 'POST'])
def ver_materias_docente():
    if "docente" in session:
        id_docente = session["docente"]
        if request.method == 'GET':
            materiasDocente = VerMateriasDocenteCase(DB)
            materias = materiasDocente.run(id_docente)
        return render_template('docentes/ver_materias.html', materias = materias)
    else:
        return redirect(url_for('login'))

@app.route('/ver_asignaciones', methods =['GET', 'POST'])
def ver_asignaciones():
    if "docente" in session:
        if request.method == 'GET':
            asignacionesModel = ListarAsignacionesCase(DB)
            asignaciones = asignacionesModel.run()
            return render_template('docentes/ver_asignaciones.html', asignaciones = asignaciones)
    else: 
        return redirect(url_for('login'))

@app.route('/docentes/espacios/<id_materia>', methods = ['POST', 'GET'])
def obtener_materia(id_materia):
    docentesModel = ObtenerIdMateriasCase(DB)
    lista = docentesModel.run(id_materia)
    return render_template('docentes/asignarespacio.html', contact = lista[0])

@app.route('/docentes/asignar_espacio/<id_materia>', methods=['POST'])
def asignar_espacio(id_materia):
    if request.method == 'POST':
        docentesModel = CrearAsignacionesCase(DB)
        docentesModel.run(id_materia)
        return redirect(url_for('ver_asignaciones'))

@app.route('/clases_programadas/eliminar/<id_clase>', methods =['GET', 'POST'])
def eliminar_clase(id_clase):
    if request.method == 'GET':
        docentesModel = EliminarProgramadaCase(DB)
        docentesModel.run(id_clase)
        return redirect(url_for('ver_asignaciones'))

@app.route('/asistencia/asistir_a_clase/<id_espacio>', methods = ['POST', 'GET'])
def asistir_a_clase(id_espacio):

    if "user" in session:
        id_estudiante = session["user"]
        asistencia = AsistirAClaseCase(DB)
        asistencia.run(id_espacio,id_estudiante)
        return render_template('estudiantes/revisando_temas.html')

@app.route('/id_para_asistencia/<id_espacio>', methods = ['POST', 'GET'])
def revisar_asistencia(id_espacio):
    if request.method == 'POST':
        session["idespacio"] = id_espacio
        return redirect(url_for('ver_asistencia'))

@app.route('/ver_asistencia', methods = ['POST', 'GET'])
def ver_asistencia():
    if "idespacio" in session:
        id_espacio = session["idespacio"]  
        if request.method == 'GET':
            asistencia = VerAsistenciaCase(DB)
            asistencias = asistencia.run(id_espacio)
            return render_template('docentes/ver_asistencias.html', asistencias = asistencias )
    else:
        return redirect(url_for('login'))   

def create_app_api():
    app.run(debug=True, port=5000, host="0.0.0.0")