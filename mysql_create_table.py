import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="password", database="flask_db")
cur = conn.cursor()

cmd = "CREATE TABLE students (\
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    name VARCHAR(30) NOT NULL,\
    addr VARCHAR(30), \
    city VARCHAR(30), \
    zip VARCHAR(30))"

cur.execute(cmd)
conn.close()
