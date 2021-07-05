from flask import Flask, render_template, request

app = Flask(__name__)

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

def query_string():
  print(request)# objeto requestr , dentro del modelo C/S este es la peticion que se le hace al servidor
  print(request.args)
  print(request.args.get('param1'))
  print(request.args.get('param2'))
  return 'Ok Wilson vas bien'

def pagina_no_encontrada(error):
  return render_template('404.html'), 404


if __name__=='__main__':
  app.add_url_rule('/query_string', view_func=query_string)# enlazar funcion hacia la url'query_string', no necesariamente tienen que tener el mismo nombre
  app.register_error_handler(404, pagina_no_encontrada)
  app.run(debug=True, port=5000)

# Virtualenv -p python3 env
# pip list
# .\env\Scripts\Activate --> para entrar al entorno virual donde podemos instalar paquetes, librerias y framework
# deactivate --> para salir del entorno virtual
# pip freeze > requirements.txt --> crea un archivo con todos los paquetes del proyecto para que se puedan migrar a otro proyecto
# pip install -r requirements.txt --> para instalar los paquetes en otro proyecto
# python .\app\app.py
# python.exe pip install --upgrade pip
# python .\src\app.py
# pip list --outdated --> para ver los paquetes que estan desactualizados
# pip show "nombre del paquete" --> para ver toda la informacion mas detallada del paquete
# pip check "nombre del paquete" --> sirve para ver si el paquete tiene algun faltante de otra dependencia o estas esten rotas