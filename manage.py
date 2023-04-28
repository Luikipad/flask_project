from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Employee registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Employee information page
@app.route('/information')
def information():
	con = sqlite3.connect("database.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from students")
	rows = cur.fetchall();
	return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)

