
from bottle import run, route ,view , template , redirect

@route('/')
def index():
    return 'please authorize yourself!!!'

@route('/restricted')
def restricted():
    #authorization function
    redirect('/')

    
run(host = "localhost" , port = 8080, debug = True)
