from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/greetings/')
def greetings():
    return "How are you doing?"

@app.route('/greetings/christmas')
def christmas():
    return "Merry Christmas!"

@app.route('/greetings/newyear')
def newyear():
    return "Happy New Year!"

if __name__ == '__main__':
    app.run(debug=True)

