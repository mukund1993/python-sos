from flask import Flask, redirect, render_template, request

app = Flask(__name__)
@app.route("/login")
def hello():
    appname = request.args['appname']
    return render_template('login.html', name=appname)

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        return redirect('http://127.0.0.1:5002/success', code=307)   