from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def gethome():
    name='eric'
    address='/users/'+name
    
    return redirect(address)

@app.route('/users/<username>')
def show_user_profile(username):
    
    return render_template("user.html",template_username = username)

app.run(debug=True)