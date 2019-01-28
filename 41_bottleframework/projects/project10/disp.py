from bottle import route, run, template

HOST = 'localhost'

test = {
    'protocol': ['protocol1','protocol2','protocol3'],
    'service':['s1','s2','s3'],
    'plugin': ['plug1','plug2','plug3'],
    'result':[1,0,1]
}

number_of_test_cases = len(test['result'])

@route('/page1')
def serve_homepage():
    return template('disp_table',rows = test, cases = number_of_test_cases)

@route('/new')
def add_new():
    return template('add_case')

run(host=HOST, port=8080, debug=True)
