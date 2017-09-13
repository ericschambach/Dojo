from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'session key'
mysql_connection = MySQLConnector(app,'addfriendsdb')

@app.route('/')
def homepage():
    results = []
    query = 'select first_name, last_name, age, created_at from friends'
    results = mysql_connection.query_db(query)
    return render_template('index.html',friends=results)

@app.route('/addvalue', methods=['POST'])
def create():
    session['firstname'] = request.form['first_name']
    session['lastname'] = request.form['last_name']
    session['age'] = request.form['age']
    if 'firstname' in session:
        parameters = {
        'parameter_firstname': session['firstname'],
        'parameter_lastname': session['lastname'],
        'parameter_age': session['age'],
        }
        query = 'insert into friends (first_name, last_name, age, created_at, updated_at) values (:parameter_firstname,:parameter_lastname,:parameter_age, NOW(), NOW())'
        mysql_connection.query_db(query, parameters)
        session.clear()
    return redirect('/')


app.run(debug=True)