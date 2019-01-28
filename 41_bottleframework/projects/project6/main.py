from bottle import route, run, static_file, template

HOST = 'localhost'


@route('/')
def serve_homepage():
    l1 = "my list A - l1"
    l2 = "my list A - l2"
    l3 = "my list A - l3"
    return template('main.tpl', A1=l1, A2=l2, A3=l3)

run(host=HOST, port=8080,reloader= True, debug=True)

'''
from bottle import route, run, static_file, template

HOST = 'localhost'


@route('/page1')
def serve_homepage():
    l1 = "my list A - l1"
    l2 = "my list A - l2"
    l3 = "my list A - l3"
    return template('main.tpl', A1=l1, A2=l2, A3=l3)

@route('/page2')
def serve_homepage():
    l1 = "my list B - l1"
    l2 = "my list B - l2"
    l3 = "my list B - l3"
    return template('main.tpl', A1=l1, A2=l2, A3=l3)


run(host=HOST, port=8080,reloader = True , debug=True)
'''


'''
from bottle import route, run, static_file, template

HOST = 'localhost'

@route('/static/')
def server_static(filepath):
    return static_file(filepath, root='/home/k/TEST/Py/Bottle/')

@route('/page1')
def serve_homepage():
    l1 = "my list A - l1"
    l2 = "my list A - l2"
    l3 = "my list A - l3"
    list = [l1,l2,l3]
    return template('main.tpl', A=list)

@route('/page2')
def serve_homepage():
    l1 = "my list B - l1"
    l2 = "my list B - l2"
    l3 = "my list B - l3"
    list = [l1,l2,l3]
    return template('main.tpl', A=list)

run(host=HOST, port=8080, debug=True)
'''

''' changes in html as below
<li>{{A[0]}}</li>
<li>{{A[1]}}</li>
<li>{{A[2]}}</li>
'''
