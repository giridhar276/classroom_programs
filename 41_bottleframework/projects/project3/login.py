from bottle import get, post, request, run, route

@route('/login')
def lg():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
# fake check, always returns True
def check_login(u,p):
    return True

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>You are logged in.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080)
