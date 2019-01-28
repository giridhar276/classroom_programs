from bottle import route, run, template, request

try:
    import simplejson as json
except ImportError:
    import json

HOST = 'localhost'

test_dic = {
    'protocol': ['protocol1','protocol2','protocol3'],
    'service':['s1','s2','s3'],
    'plugin': ['plug1','plug2','plug3'],
    'result':[1,0,1]
}

number_of_test_cases = len(test_dic['result'])

@route('/page1')
def serve_homepage():
    return template('disp_table',rows = test_dic, cases = number_of_test_cases)

@route('/new')
def add_new():
    return template('add_case_post')

@route('/new', method='POST')
def add_new():
    p = request.forms.get('protocol')
    with open('test.json', 'w') as f:
        json.dump(test_dic, f)
    print('p=',p)

run(host=HOST, port=8080, debug=True)