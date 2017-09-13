from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = 'b37e16c620c055cf8207b999e3270e9b'

@app.route('/')
def make_survey():
    return render_template("survey.html")

@app.route('/process', methods=['POST'])
def form_validation():
    session["user_username"] = request.form['user_username']
    session["user_location"] = request.form['user_location']
    session["user_language"] = request.form['user_language']
    session["user_description"] = request.form['user_description']
    return redirect('/surveyresults')

@app.route('/surveyresults')
def form_results():
    
    return render_template('/surveyresults.html')

app.run(debug=True)