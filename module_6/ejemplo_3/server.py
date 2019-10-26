from bottle import route, run, template,  response, static_file


respuesta = {
    'mensaje': 'Hola mundo desde Python',
    'codigoRespuesta': 200
}

@route("/")
def index():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    return respuesta

@route("/python")
def archivo():
    return static_file('rick.jpg', root='/Users/mauriciochavez/bedu_python/module_6/ejemplo_3/static')


run(host="localhost", port=8080, reloader=True)
