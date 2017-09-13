from flask import Flask, session, request, redirect, render_template,flash
from mysqlconnection import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '54b0c58c7ce9f2a8b551351102ee0938'
mysql_connection = MySQLConnector(app,'practicetest')

@app.route('/')
def startpage():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    form_reproved = False
    name = request.form['username']
    email = request.form['email']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    if len(name) < 1:
        form_reproved = True
        flash("*Name cannot be empty!")
    if len(password)< 1:
        flash("*Password cannot be empty!")
        form_reproved = True
    if len(password)>= 1 and len(pass_confirm)< 1:
        flash("*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pass_confirm)>= 1) and password != pass_confirm:
        flash("*Passwords do not match!")
        form_reproved = True
    if password.isnumeric() == True or password.isalpha() == True or password.islower() == True or password.isupper() == True:
        flash('*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(email) < 1:
        flash('*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("*Invalid Email Address!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        parameters = {
        'parameter_name': name,
        'parameter_email': email,
        'parameter_password': password,
        }
        query = 'insert into users (name, email, password, created_at, updated_at) values (:parameter_name,:parameter_email,:parameter_password, NOW(), NOW())'
        try:
            mysql_connection.query_db(query, parameters)
        except:
            flash('User already exists!')
            return redirect('/')
        session['name'] = name
        session['email'] = email
        return redirect('/success')
    
@app.route('/login', methods=['POST'])
def login():
    login_name = request.form['username']
    if len(login_name) < 1:
        flash("*You have to provide a user name!")
        print 'success'
        return redirect('/')
    else:
        results = []
        login_password = md5.new(request.form['password']).hexdigest()
        parameters = {
        'parameter_name': login_name,
        'parameter_password': login_password,
        }
        query = 'select name from users where name = :parameter_name'
        mysql_connection.query_db(query, parameters)
        results = mysql_connection.query_db(query, parameters)
        if len(results) == 0:
            flash("*User name does not exist in our records!")
            return redirect('/')
        else:
            results = []
            query = 'select password from users where password = :parameter_password'
            mysql_connection.query_db(query, parameters)
            results = mysql_connection.query_db(query, parameters)
            if len(results) == 0:
                flash("*Password does not match our records!")
                return redirect('/')
            else:
                session['name'] = login_name
                return redirect ('/success')
                    
@app.route('/success')
def endpoint():
    if 'name' not in session:
        flash('*You are not logged in!')
        return redirect('/')
    else:
        return render_template('success.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return render_template('success.html')
    
app.run(debug=True)