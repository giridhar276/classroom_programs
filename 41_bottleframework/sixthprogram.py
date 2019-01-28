from bottle import error , route , run , abort


@error(404)
def not_found(error):
    return ' Ther enquired countent was not found'

@error(401)
def not_found(error):
    return 'You shall not pass!!'


@route('/')
def index():
    return 'welcome to bottle'

@route('/youshallnotpass')
def shallnotpass():
    abort(401)
 




run(host ="localhost" , port = 8080 , debug = True)
