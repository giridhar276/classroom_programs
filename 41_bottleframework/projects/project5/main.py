from bottle import route, run, static_file, template

HOST = 'localhost'
 
@route('/')
def serve_homepage():
    return template('main.html')

run(host=HOST, port=8080,reloader = True , debug=True)
