import sqlite3
con = sqlite3.connect('bucket.db')
con.execute("CREATE TABLE bucket (id INTEGER PRIMARY KEY, wish char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO bucket (wish,status) VALUES ('Flying over Golden Gate Bridge',0)")
con.execute("INSERT INTO bucket (wish,status) VALUES ('Wind surfing under Golden Gate Bridge',0)")
con.execute("INSERT INTO bucket (wish,status) VALUES ('Bungee jumping from Golden Gate Bridge',0)")
con.execute("INSERT INTO bucket (wish,status) VALUES ('Walking across Golden Gate Bridge',1)")
con.commit() 