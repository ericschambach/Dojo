from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
app.secret_key = 'd5ba3e16bb4c24ea5ff1a37100994e0f86e'

@app.route('/')
def home_page():
    if 'counter' not in session:
        session['counter'] = 0
    if 'add_value' not in session:
        session['add_value'] = False
    if session['add_value'] == False:
        session['counter'] = session['counter'] + 1
        count = session['counter']
    else:
        count = session['counter']
        session['add_value'] = False 
    return render_template('index.html',template_count = count)

@app.route('/process', methods=['POST'])
def form_validation():
    session["counter"] += 2
    session['add_value'] = True
    return redirect('/')

@app.route('/reset_views')
def reset_views():
    session.clear()
    return redirect('/')

app.run(debug=True)

#  SOLUTION GIVE
# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)
# app.secret_key = 'very secret'


# @app.route('/')
# def counter():
#     try:
#         session['counter'] += 1
#     except:
#         session['counter'] = 1
#     return render_template('index.html')

# @app.route('/add2', methods=['POST'])
# def increment():
#     print 'hello again'
#     session['counter'] += 1
#     return redirect('/')

# @app.route('/reset_count', methods=['POST'])
# def reset():
#     session['counter'] = 0
#     return redirect('/')

# app.run(debug=True)