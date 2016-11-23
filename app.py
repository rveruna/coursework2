from flask import flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/welcome')
def welcome():
    return_template("welcome.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
