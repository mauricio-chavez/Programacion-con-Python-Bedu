import os

from bottle import route, run, response, static_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


@route("/")
def index():
    response = {
        'mensaje': 'Hola mundo desde Python',
        'codigoRespuesta': 200
    }
    return response


@route("/foto-rick")
def archivo():
    return static_file('rick.jpg', root=STATIC_ROOT)


run(host="localhost", port=8080, reloader=True)
