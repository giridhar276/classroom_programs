# bucket.py
import sqlite3
from bottle import route, run, template

HOST = 'localhost'
PORT = 8080

@route('/bucket')
def bucket_list():
    conn = sqlite3.connect('bucket.db')
    c = conn.cursor()
    c.execute("SELECT id, wish FROM bucket")
    result = c.fetchall()
    c.close()
    return template('wish_table', rows=result)

run(host=HOST, port=PORT, debug=True)
