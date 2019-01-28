from bottle import error , route , run

 
@error(404)
def not_found(error):
    return ' Ther enquired countent was not found'

@route('/')
def index():
    return 'welcome to bottle'

run(host ="localhost" , port = 8080 , debug = True)
