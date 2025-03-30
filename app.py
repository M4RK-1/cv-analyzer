from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/analyzer')
def analyzer():
    return render_template('analyzer.html', title="Analyzer")

@app.route('/login', methods=['GET', 'POST'])
def login():
    hashed = None
    if request.method == 'POST':
        password = request.form['password']
        hashed = hashlib.sha256(password.encode()).hexdigest()
    return render_template('login.html', title="Login", hashed=hashed)

@app.route('/register', methods=['GET', 'POST'])
def register():
    hashed = None
    if request.method == 'POST':
        password = request.form['password']
        hashed = hashlib.sha256(password.encode()).hexdigest()
    return render_template('register.html', title="Register", hashed=hashed)

@app.route('/placeholder')
def placeholder():
    return render_template('placeholder.html', title="Placeholder")

if __name__ == '__main__':
    app.run(debug=True)
