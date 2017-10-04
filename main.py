from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True  


@app.route("/", methods=['POST', 'GET'])
def index():
     return render_template('login.html', title="Signup")


@app.route('/signup', methods=['POST','GET'])
def validate_login():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    username_error=''
    password_error=''
    vpassword_error=''
    email_error=''

    if len(username) < 3 or len(username) > 20 or " " in username: 
       username=''
       password=''
       vpassword=''
       username_error = 'Not a valid username'
    
    if len(password) < 3 or len(password) > 20 or " " in password: 
       password=''
       vpassword=''
       password_error = 'Not a valid password'

    if password != vpassword: 
       vpassword=''
       vpassword_error = 'Please verify password'
    if len(email) > 0:
        if len(email) < 3 or  len(email) > 20 or " " in email or '@' not in email or "." not in email:
           email=''
           password=''
           vpassword=''
           email_error = 'Not a valid email'

 
    if not username_error and not password_error and not vpassword_error and not email_error:
       return redirect('/logged_in?username=' + username)
    else:
       return render_template('login.html',username_error=username_error,
          password_error=password_error,
          vpassword_error=vpassword_error,
          email_error=email_error,
          username=username,
          password=password,
          vpassword=vpassword,
          email=email)
@app.route('/logged_in')
def logged_in():
    username = request.args.get('username')
    return render_template('logged_in.html', username=username)

app.run() 