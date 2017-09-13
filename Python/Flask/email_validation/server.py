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
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("*Invalid Email Address!")
        return redirect('/')
    else:
        session['email'] = request.form['email']
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