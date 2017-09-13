from flask import Flask, session, request, redirect, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'session key'
mysql_connection = MySQLConnector(app, 'world')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['session_name'] = request.form['html_name']
        session['session_year'] = request.form['html_year']
        return redirect('/')
    else:
        results = []
        if 'session_name' in session:
            parameters = {
                'parameter_name': session['session_name'],
                'parameter_year': session['session_year']
            }
            query = 'select name, indep_year, head_of_state from countries where name = :parameter_name AND indep_year > :parameter_year'
            results = mysql_connection.query_db(query, parameters)
            session.clear()
        else:
            query = 'select name, indep_year, head_of_state from countries'
            results = mysql_connection.query_db(query)

        return render_template('index.html', countries=results)

app.run(debug=True)