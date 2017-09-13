from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'session key'
mysql_connection = MySQLConnector(app,'addemailsdb')

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/addvalue', methods=['POST'])
def create(): 
form_reproved = False
    if len(request.form['user_username']) < 1:
        form_reproved = True
        flash("*Name cannot be empty!")
    if len(request.form['password'])< 1:
        flash("*Password cannot be empty!")
        form_reproved = True
    if len(request.form['password'])>= 1 and len(request.form['password_confirmation'])< 1:
        flash("*Please confirm password!")
        form_reproved = True
    if (len(request.form['password'])>= 1 and len(request.form['password_confirmation'])>= 1) and request.form['password'] != request.form['password_confirmation']:
        flash("*Passwords do not match!")
        form_reproved = True
    if request.form['password'].isnumeric() == True or request.form['password'].isalpha() == True or request.form['password'].islower() == True or request.form['password'].isupper() == True:
        flash('*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(request.form['email']) < 1:
        flash('*Email cannot be blank!')
        form_reproved = True
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("*Invalid Email Address!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    if form_reproved == False:
    else:
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['email'] = request.form['pw_confirm']
        parameters = {
        'parameter_email': session['email'],
        }
        query = 'insert into emails (email, created_at, updated_at) values (:parameter_email, NOW(), NOW())'
        mysql_connection.query_db(query, parameters)
        return redirect('/emailpass')

@app.route('/emailpass')
def resultpage():
    email = session["email"]
    session.clear()
    results = []
    query = 'select email, created_at from emails'
    results = mysql_connection.query_db(query)
    return render_template('results.html',template_email=email,template_results=results)

@app.route('/clear', methods=['POST'])
def backtostart():
    session.clear()
    return redirect('/')

app.run(debug=True)