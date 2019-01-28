import sqlite3
con = sqlite3.connect('bucket.db')
with con:
    cur = con.cursor()
    con.execute("INSERT INTO bucket (wish,status) VALUES ('Living near Golden Gate Bridge',1)")
    con.commit()