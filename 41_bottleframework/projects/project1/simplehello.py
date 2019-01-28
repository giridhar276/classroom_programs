from bottle import route, run
import os

@route('/')
def hello():
    return '<h1>This is the homepage</h1>'


@route('/hello')
def hello():
    
    username = os.getlogin()
    string = '<h1> ' + "hello " + username + " this is the hello page" + " </h1>"
    return string

run(host='localhost', port=8080, reloader = True ,debug=True)
