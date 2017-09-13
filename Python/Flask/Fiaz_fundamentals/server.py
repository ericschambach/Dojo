from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/some_route')
# def another_function():
#     print "dog"
#     return render_template('show.html')

# @app.route('/sample_redirect')
# def this_will_never_return_html_exclamation_point():
#     print "$$$$$$"
#     return redirect('/some_route')

# @app.route('/square/<number>')
# def square_function(number):
#     square = int(number)*int(number)
#     return render_template('square.html', something_else = square)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def fake_authentication_do_not_hardcode_stuff_like_this():
    server_username = request.form['html_username']
    server_password = request.form['html_password']

    if server_password == 'safe_password':
        return redirect('/home')
    else:
        return redirect('/login')

@app.route('/home')
def home():
    return render_template('home.html', template_username = 'fiaz.sami', template_password = 'NEVER DISPLAY A USER PASSWORD!')

app.run(debug=True)