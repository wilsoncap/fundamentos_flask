from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

#conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba_21'

conexion = MySQL(app)

@app.before_request
def before_request():
  print('Antes de la peticion....')

@app.after_request
def after_request(response):
  print('Despues de la peticion')
  return response



@app.route('/')#decorador
def index():#ruta esta enlazada con el decorador
  # return "<h1>hola mundo, aqui estoy aprendiedo algo nuevo....Upss</h1>"
  cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'Javascript']
  data={
    'titulo':'My app_flask',
    'Bienvenida':'Saludos',
    'cursos':cursos,
    'numero_cursos': len(cursos)
  }
  return render_template('index.html', data=data)

##"""
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
  data={
    'titulo':'Contacto',
    'nombre': nombre,
    'edad': edad
  }
  return render_template('contacto.html', data=data)
##"""

def query_string():#query_string?param1=Wilson&param2=33
  print(request)# objeto requestr , dentro del modelo C/S este es la peticion que se le hace al servidor
  print(request.args)
  print(request.args.get('param1'))
  print(request.args.get('param2'))
  p1 = request.args.get('param1')
  p2 = request.args.get('param2')
  data={
    'arg1': p1,
    'arg2': p2

  }
  return render_template('query_string.html', data=data)

@app.route('/cursos')
def listar_cursos():
  data = {}

  try:
    cursor = conexion.connection.cursor()
    sql = 'SELECT Coprod, Nomcurso, Credcurso FROM cursos ORDER BY Nomcurso ASC'
    cursor.execute(sql)
    cursos = cursor.fetchall()
    print(cursos)
    data['cursos'] = cursos
    data['mensaje'] = 'Exitoso en la conexion'
  except Exception as ex:
    data['mensaje'] ='Error...'
  return jsonify(data)


@app.route('/mostrarcursos')
def show_cursos():
  #cursos = get('http//127.0.0.1:5000/cursos').json()


def pagina_no_encontrada(error):
  # return render_template('404.html'), 404
  return redirect(url_for('index'))


if __name__=='__main__':
  app.add_url_rule('/query_string', view_func=query_string)# enlazar funcion hacia la url'query_string', no necesariamente tienen que tener el mismo nombre
  app.register_error_handler(404, pagina_no_encontrada)
  app.run(debug=True, port=5000)


# py -m pip install virtualenv  --> para crear entorno virtual globalmente
# Virtualenv -p python3 env, otro_nombre  --> para crear entorno virtual localmente
# pip list -->para ver lo que hay en la ruta actual
# pip install flask --> para insalar flask
# .\env\Scripts\Activate --> para entrar al entorno virual donde podemos instalar paquetes, librerias y framework
# deactivate --> para salir del entorno virtual
# pip freeze > requirements.txt --> crea un archivo con todos los paquetes del proyecto para que se puedan migrar a otro proyecto
# pip install -r requirements.txt --> para instalar los paquetes en otro proyecto
# python .\app\app.py --> se ejecuta en el entorno virtual
# python.exe pip install --upgrade pip
# python .\src\app.py
# pip list --outdated --> para ver los paquetes que estan desactualizados
# pip show "nombre del paquete" --> para ver toda la informacion mas detallada del paquete
# pip check "nombre del paquete" --> sirve para ver si el paquete tiene algun faltante de otra dependencia o estas esten rotas
# pip install flask-sqlalchemy --> modulo para comunicarse con base de datos
# pip install flask-marshmallow --> modulo para definir squemas en nuestra base de datos
# pip install marshmallow-sqlalchemy --> librerias que trabajan entre ellas mismas
# pip install pymysql -->modulo para poder crear conexion con la base de datos