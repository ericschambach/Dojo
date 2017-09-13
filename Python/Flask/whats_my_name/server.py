from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def make_form():

    return render_template("index.html")

@app.route("/process", methods=['POST'])
def get_form_info():
    server_username = request.form['user_username']
    server_password = request.form['user_password']

    return redirect('/')


app.run(debug=True)