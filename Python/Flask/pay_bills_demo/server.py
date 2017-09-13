from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'd5ba3e16bb4c24ea5f1a37100994e0f86e'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay_bills')
def pay_bills():
    if 'paid_bills' not in session:
        session['paid_bills'] = []
    # print '-' * 100
    # print session['paid_bills']
    return render_template('pay_bills.html')

@app.route('/process_bills', methods=['POST'])
def process_bills():
    company_name = request.form['html_company_name']
    amount = request.form['html_amount']
    payment = {
        'company_name': company_name,
        'amount': amount
    }
    
    paid_bills = session['paid_bills']
    paid_bills.append(payment)
    session['paid_bills'] = paid_bills

    # print '-' * 100
    # print session['paid_bills']
    return redirect('/pay_bills')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/authenticate', methods=['POST'])
# def fake_authentication_do_not_hardcode_stuff_like_this():
#     server_username = request.form['html_username']
#     server_password = request.form['html_password']

#     if server_password == 'safe_password':
#         return redirect('/home')
#     else:
#         return redirect('/login')

# @app.route('/home')
# def home():
#     return render_template('home.html', template_username = 'fiaz.sami', template_password = 'NEVER DISPLAY A USER PASSWORD!')

@app.route('/reset_bills')
def reset_bills():
    session.clear()
    return redirect('/pay_bills')



app.run(debug=True)