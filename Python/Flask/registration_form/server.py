from flask import Flask, session, request, redirect, render_template, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'b37e16c620c055cf8207b999e3270e9b'


@app.route('/')
def make_survey():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def form_validation():
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
    if request.form['user_location'] == 'Choose here':
        flash("*Please select a location!")
        form_reproved = True
    if request.form['user_language'] == 'Choose here':
        flash("*Please select a language!")
        form_reproved = True
    if len(request.form['user_description']) > 120:
        flash("*Comment section cannot exceed 120 characters!")
        form_reproved = True
    if len(request.form['user_description']) < 1:
        flash("*Please leave a comment!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    elif form_reproved == False:
        session["user_username"] = request.form['user_username']
        session['email'] = request.form['email']
        session["user_location"] = request.form['user_location']
        session["user_language"] = request.form['user_language']
        session["user_description"] = request.form['user_description']
        # session['birthday'] = request.form["birthday"]
        return redirect('/results')

@app.route('/results')
def form_results():
    username = session["user_username"]
    usermail = session['email']
    password = 'Password is ok'
    location = session["user_location"]
    language = session["user_language"]
    # birthday = request.form["birthday"]
    description = session["user_description"]

    return render_template('registration_results.html',template_username = username,template_mail=usermail,template_password=password,template_location=location,template_language=language,template_description=description)

@app.route('/clear', methods=['POST'])
def clear_views():
    session.clear()
    return redirect('/')

app.run(debug=True)