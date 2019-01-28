from bottle import get, post, request, run, route , template

@route('/login')
def lg():
    return template('index.html')
    

# fake check, always returns True
def check_login(u,p):
    return True

@route('/login', method='POST')
def do_login():
    username = request.forms.get('user')
    print(username)
    password = request.forms.get('password')
    print(password)
    if check_login(username, password):
        return "<p>You are logged in.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080)
