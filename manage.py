from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_student():
   return render_template('student.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         EmpID = request.form['EmpID']
         EmpName = request.form['EmpName']
         EmpGender = request.form['EmpGender']
         EmpPhone = request.form['EmpPhone']
         EmpBdate = request.form['EmpBdate']
         
         with sql.connect(host="localhost", user="flask", password="password", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employee (EmpID,EmpName,EmpGender,EmpPhone,EmpBdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(EmpID,EmpName,EmpGender,EmpPhone,EmpBdate)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.htm",msg = msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="password", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from employee")
      rows = cur.fetchall()

   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
