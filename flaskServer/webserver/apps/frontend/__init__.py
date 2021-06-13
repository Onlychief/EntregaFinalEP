from flask import Flask, jsonify, render_template, request, redirect, url_for,Flask,jsonify,make_response, session, flash
from src.shared.infra.mariadb import DB
from src.estudiantes.app.listar import ListarEstudiantesCase

app = Flask(__name__, template_folder = 'views')

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listarEstudianteCase = ListarEstudiantesCase(DB)
    return render_template('estudiantes/ver_estudiantes.html', listarEstudiantesCase= listarEstudianteCase)
    
def create_app_frontend():
    app.run(debug=True, port=5000)