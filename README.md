# EntregaFinalEP
El codigo se incluye para que se puede revisar la estructura hexagonal.
Se debe ejecutar el archivo docker-compose.yml para que corran los contenedores del api y de la bd

Pasos para Ejecución

Ejecutar el archivo main.py, ubicado en la carpeta raiz del proyecto.
Ingresar por el navegador usando localhost:5000/inicio
Existen dos formas de ingresar: Rol de docentes y Rol de estudiantes. 3.1 Manejo de Rol de docentes: Se debe usar las credenciales: correo: jhony@gmail.com clave: 123 El rol de docentes puede asignar espacios academicos a sus materias y gestionar a los alumnos, registro y eliminación. Al asignar un espacio académico con hora y fecha, este aparecerá disponible para todos los estudiantes que cursen el mismo semestre con el que este relacionada la materia
Materias Semestre IX Ingles VII Proyectos

Materias Semestre X Electiva Profesional 1 y 2 Materia Prueba

Todas las materias menos Ingles VII estan relacionadas al docente Jhonatan, y apareceran disponibles para asignarles un espacio academico una vez se haya logeado.

3.2 Manejo de Rol de estudiante: Hay dos estudiantes disponibles para hacer pruebas

Estudiante inscrito a semestre X:
correo: prueba25@hotmail.com
clave: 123

Estudiante inscrito a semestre IX:
correo: jhon9@hotmail.com
clave: 123
En cuanto los estudiantes se logueen, podran ver las materias relacionadas con el semestre al que están inscritos. En la misma plataforma hay un botón llamado "ver clases programadas", en la cual aparecerán los espacios asignados por los docentes, siempre y cuando estén relacionadas con el mismo semestre del estudiante y cuya fecha y hora de finalización no sean menores a las fechas y hora actual.

Junto a cada clase programada hay un botón con la etiqueta "Asistir", al hacer clic se direccionara a una pagina simple html la cual no influye en la programacion.

Una vez marcada la asistencia del estudiante, se puede regresar a localhost:5000/inicio e ingresar como docente

Se debe usar las credenciales: correo: jhony@gmail.com clave: 123

Se hace clic en el boton "Ver Asignaciones" y una vez ahi se clickea el botón "Revisar Asistencia". Aparecerán en el listado todos los estudiantes que ingresaron con su usuario e hicieron click en el boton "Asistir"
