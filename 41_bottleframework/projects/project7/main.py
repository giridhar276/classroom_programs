from bottle import Bottle, route, run, static_file, template
import time

app = Bottle()

HOST = 'localhost'

@app.route('/api/status')
def api_status():
    return {'status':'online', 'servertime':time.time()}

run(app, host=HOST, port=8080, debug=True)
