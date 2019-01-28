from bottle import get, post , run , delete

@get('/')
def index():
    return 'Welcome to bottle project'

@post('/')
def index_post():
    return 'Welcome from post to bottle project'

@delete('/')
def index_delete():
    return 'Welcome from DELTE to bottle proejct'

run(host ='localhost' , port = 8080 , debug = True)
