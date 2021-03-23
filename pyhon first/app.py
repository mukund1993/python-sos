from flask import Flask,render_template,redirect,request, session
app = Flask(__name__)
app.secret_key = "abc"
@app.route('/')
def index():
    if 'username' in session:
        return redirect('/success' )
    return render_template('home.html')  

@app.route('/login')
def hello_world():
    return redirect('http://127.0.0.1:5000/login?appname=myfirstapp', code=307 )

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method == 'POST':
        session['username'] = request.form['uname']
    username = session['username']
    return render_template('success.html', name=username)  


    