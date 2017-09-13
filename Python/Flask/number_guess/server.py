from flask import Flask, session, request, redirect, render_template
import random

app = Flask(__name__)
app.secret_key = 'd5ba3e16bb4c24ea5ff1a371009ahd594e0f86e'

@app.route('/')
def guess_page():
    if 'game_status' not in session:
            session['game_status'] = 'start'
    if 'warning' not in session:
        session['warning'] = 'waiting'
    warning=session['warning']
    game_status = session['game_status']
    return render_template("index.html",template_status = game_status,template_warning=warning)


@app.route('/game', methods=['POST'])
def game_engine():
    if 'cpu_number' not in session:
        session['cpu_number'] = random.randrange(1,101)
    session['playerNumber'] = int(request.form.get('player_guess'))
    if session['playerNumber'] == session['cpu_number']:
        session['game_status'] = 'won'
        session['warning'] = str(session['playerNumber'])+' was the right number!'
    elif session['playerNumber'] < session['cpu_number']:
        session['game_status'] = 'low'
        session['warning'] = 'Too low!'
    elif session['playerNumber'] > session['cpu_number']:
        session['game_status'] = 'high'
        session['warning'] = 'Too High!'
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_views():
    session.clear()
    return redirect('/')

app.run(debug=True)