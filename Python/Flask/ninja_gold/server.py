from flask import Flask, session, request, redirect, render_template
import random
import datetime

app = Flask(__name__)
app.secret_key = 'd5ba3e16bb4c24ea5ff1a3710095ahd594e0f86e'

@app.route('/')
def home_page():
    if 'my_gold' not in session:
        session['my_gold'] = 0
    if 'my_result' not in session:
        session['my_result'] = 0
    if 'result_log' not in session:
        session['result_log'] = []
    bet = session['result_log']
    gold = session['my_gold']
    return render_template('index.html',template_gold=gold,template_bet=bet)

@app.route('/process_money',methods=['POST'])
def calculate_coins():
    bet_type = (str(request.form.get('building')))
    results = {'farm':{'min': 10,'max':20},'cave':{'min': 5,'max':10},'house':{'min': 2,'max':5},'casino':{'min': -50,'max':50}}
    session['result'] = random.randint(results[bet_type]['min'],results[bet_type]['max'])
    session['my_gold'] = session['my_gold'] + session['result']
    time = datetime.datetime.now()
    if bet_type == 'casino' and session['result'] < 0:
        session['result_log'].append('Entered the {} and lost {} golds... Ouch! {}'.format(bet_type.capitalize(),abs(session['result']),time))
        session.modified = True
    if bet_type == 'casino' and session['result'] > 0:
        session['result_log'].append('Entered the {} and won {} golds... WOW! {}'.format(bet_type.capitalize(),session['result'],time))
        session.modified = True
    if bet_type == 'casino' and session['result'] == 0:
        session['result_log'].append('Entered the {} and no wins! {}'.format(bet_type.capitalize(),time))
        session.modified = True
    if bet_type != 'casino':
        session['result_log'].append('Earned {} golds from the {}! {}'.format(session['result'],bet_type.capitalize(),time))
        session.modified = True
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_views():
    session.clear()
    return redirect('/')


app.run(debug=True)