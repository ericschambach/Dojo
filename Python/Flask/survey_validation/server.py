from flask import Flask, session, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = 'b37e16c620c055cf8207b999e3270e9b'

@app.route('/')
def make_survey():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def form_validation():
    if len(request.form['user_username']) < 1 or len(request.form['user_description']) > 120:
        if len(request.form['user_username']) < 1:
            flash("*Name cannot be empty!")
        if len(request.form['user_description']) > 120:
            flash("*Comment section cannot exceed 120 characters!")
        return redirect('/')
    session["user_username"] = request.form['user_username']
    session["user_location"] = request.form['user_location']
    session["user_language"] = request.form['user_language']
    session["user_description"] = request.form['user_description']
    return redirect('/results')

@app.route('/results')
def form_results():
    username = session["user_username"]
    location = session["user_location"]
    language = session["user_language"]
    description = session["user_description"]
    return render_template('/results.html',template_username = username,template_location=location,template_language=language,template_description=description)

@app.route('/clear', methods=['POST'])
def clear_views():
    session.clear()
    return redirect('/')

app.run(debug=True)