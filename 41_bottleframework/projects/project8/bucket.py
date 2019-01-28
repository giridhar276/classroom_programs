import sqlite3
from bottle import route, run

@route('/bucket')
def bucket_list():
    conn = sqlite3.connect('bucket.db')
    c = conn.cursor()
    c.execute("SELECT id, wish FROM bucket")
    result = c.fetchall()
 
    return str(result)

run(host='localhost', reloader = True ,port=8080)
