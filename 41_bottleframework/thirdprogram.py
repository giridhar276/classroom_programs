
from bottle import run, route ,view , template

@route('/')
@view('helloworld') 
def index():
    return dict(name = 'Stranger')

run(host = "localhost" , port = 8080, debug = True)
