from flask import Flask, session, request, redirect, render_template,flash
from mysqlconnection import MySQLConnector
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
#app.secret_key to enable 'POST' method
app.secret_key = '54b0c58c7ce9f2a8b551351102ee0938'
mysql_connection = MySQLConnector(app,'wall')

#main registering or logging in page
@app.route('/')
def startpage():
    return render_template('login.html')

#route to registering validation address
@app.route('/register', methods=['POST'])
def register():
    #create variables holding the information 'inputed' from user trying to register
    first_name = str(request.form['first_name'])
    last_name = str(request.form['last_name'])
    email = request.form['email']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    #create variable to check whether all information from the input fields match set requirements, if any does not, it will hold a True to being NOT accurate/acceptable
    form_reproved = False
    #run checks on every parameter of the form
    if len(first_name) < 1:
        form_reproved = True
        flash("*First name cannot be empty!")
    if len(last_name) < 1:
        form_reproved = True
        flash("*Last name cannot be empty!")
    if len(password)< 1:
        flash("*Password cannot be empty!")
        form_reproved = True
    if len(password)>= 1 and len(pass_confirm)< 1:
        flash("*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pass_confirm)>= 1) and password != pass_confirm:
        flash("*Passwords do not match!")
        form_reproved = True
    if password.isnumeric() == True or password.isalpha() == True or password.islower() == True or password.isupper() == True:
        flash('*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(email) < 1:
        flash('*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        flash("*Invalid Email Address!")
        form_reproved = True
        #if any of the information from user is unacceptable and the information have been rejected, send the user back to login/registration page with appropriate warnings
    if form_reproved == True:
        return redirect('/')
    else:
        #if all information is ok, hash the password before including in the database
        password = md5.new(password).hexdigest()
        #create the dictionary to hold information to be included in the SQL insert query
        parameters = {
        'parameter_first_name': first_name,
        'parameter_last_name': last_name,
        'parameter_email': email,
        'parameter_password': password,
        }
        #create variable with SQL insert query
        query = 'insert into users (first_name, last_name, email, password, created_at, updated_at) values (:parameter_first_name,:parameter_last_name,:parameter_email,:parameter_password, NOW(), NOW())'
        #use try/except method to run query including information into database
        try:
            user_id = mysql_connection.query_db(query, parameters)
        except:
            #if it fails, send user back to login page with warning on user already being present
            flash('User already exists!')
            return redirect('/')
        #create a variable which will create an unique variable to become the user's homeaddress
        user_id = str(user_id)
        homeaddress= first_name+last_name+user_id
        homeaddress=homeaddress.lower()
        #include the home address and userid in the parameter's dictionary
        parameters = {
        'parameter_first_name': first_name,
        'parameter_last_name': last_name,
        'parameter_email': email,
        'parameter_password': password,
        'parameter_homeaddress': homeaddress,
        'parameter_user_id': user_id,
        }
        #add the homeaddress unique parameter in the user's database
        query = 'update users set homeaddress = :parameter_homeaddress where id=:parameter_user_id'
        mysql_connection.query_db(query, parameters)
        #add the homeaddress unique parameter in the list of addresses database
        query = 'insert into site_pages (user_id, page, created_at, updated_at) values (:parameter_user_id,:parameter_homeaddress, NOW(), NOW())'
        mysql_connection.query_db(query, parameters)
        #if everything went fine in the insert information into the database, create according session variables and redirect user to wall page
        session['user_id'] = user_id
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['homeaddress'] = homeaddress
        address = '/wall/'+homeaddress
        return redirect(address)

#route to log in validation address  
@app.route('/login', methods=['POST'])
def login():
    #get submited username - e-mail address being the case
    login_username = request.form['username']
    #if field is empty, return flash message stating so - back to login page
    if len(login_username) < 1:
        flash("*You have to provide a user name!")
        return redirect('/')
    else:
        #set the results form which will include the results from the query
        results = []
        #hash the 'inputed' password to match the hashed in the database
        login_password = md5.new(request.form['password']).hexdigest()
        #create the dictionary to have values for the SQL query
        parameters = {
        'parameter_username': login_username,
        'parameter_password': login_password,
        }
        #create variable holding the SQL query - in this case to match the e-mails 
        query = 'select first_name from users where email = :parameter_username'
        #save query to variable
        results = mysql_connection.query_db(query, parameters)
        #in case e-mail do not match the one in the database, send user back to login page with a warning message
        if len(results) == 0:
            flash("*User name does not exist in our records!")
            return redirect('/')
        else:
            #in case e-mails match, try to match passwords
            results = []
            query = 'select id,first_name, last_name,homeaddress from users where email = :parameter_username and password = :parameter_password'
            mysql_connection.query_db(query, parameters)
            results = mysql_connection.query_db(query, parameters)
            #in case passwords don't match, send user back to query page with warning
            if len(results) == 0:
                flash("*Password does not match our records!")
                return redirect('/')
            #in case passwords match, create session variables with essential information send user to wall page
            else:
                session['user_id'] = results[0]['id']
                session['first_name'] = results[0]['first_name']
                session['last_name'] = results[0]['last_name']
                session['homeaddress']=results[0]['homeaddress']
                homeaddress=session['homeaddress']
                address = '/wall/'+homeaddress
                #create address variable so each user has its unique page address (firstname+lastname+id) -> eg wall/johnblack1
                return redirect(address)
                    
@app.route('/wall/<homeaddress>',methods=['GET','POST'])
def endpoint(homeaddress):
    #make sure they are logged in to access pages inside the site
    if 'first_name' and 'user_id' and 'homeaddress' not in session:
        session.clear()
        flash('*You need to log in first!')
        return redirect('/')
    else:
        homeaddress=session['homeaddress']
        #get the user id for the logged user
        user_id = session['user_id']
        #In case information has come from a submit information form
        if request.method == 'POST':
            post_type = str(request.form['posttype'])
            print post_type
            if post_type == 'message':
                new_message = request.form['new_message']
                parameters = {
                'parameter_new_message': new_message,
                'parameter_user_id': user_id,
                }
                #check if text is over 3 characterss
                if len(new_message) <= 3:
                    flash('Messages need to be longer than 3 characters')
                    address = '/wall/'+homeaddress
                    return redirect(address)
                #if text is over 3 characters, insert the text in to 'messages' database
                else:
                    query = 'insert into messages (user_id,message,created_at,updated_at) values (:parameter_user_id,:parameter_new_message,NOW(), NOW())'
                    message_id = mysql_connection.query_db(query, parameters)
                    address = '/wall/'+homeaddress
                    return redirect(address)
            if post_type == 'message_post':
                print 'got to the right if'
                new_post = request.form['new_post']
                message_id = request.form['message_id']
                #check if text is over 2 characterss
                if len(new_post) <= 2:
                    flash('Posts need to be longer than 2 characters')
                    address = '/wall/'+homeaddress
                    return redirect(address)
                #if text is less than characters, insert the text in to 'messages' database
                if len(new_post) > 255:
                    flash('Posts can have a maximum of 255 characters')
                    address = '/wall/'+homeaddress
                    return redirect(address)
                else:
                    message_id = format.get['message_id']
                    parameters = {
                    'parameter_new_post': new_post,
                    'parameter_user_id': user_id,
                    'parameter_message_id': message_id,
                    }     
                    query = 'insert into comments (user_id,message_id,comment,created_at,updated_at) values (:parameter_user_id,:parameter_message_id,:parameter_new_post,NOW(), NOW())'
                    mysql_connection.query_db(query, parameters)
                    address = '/wall/'+homeaddress
                    return redirect(address)            
        #in case visiting the page without submitting information, load all messages for viewing                
        else:
            message_empty = True
            posted_messages = []
            first_name=session['first_name']
            query = 'select users.first_name, users.last_name, messages.id, messages.message, messages.created_at FROM users JOIN messages ON users.id=messages.user_id'
            posted_messages = mysql_connection.query_db(query)
            posted_comments = []
            query = 'select users.first_name, users.last_name, comments.message_id, messages.message, comments.comment, comments.created_at FROM users JOIN messages ON users.id=messages.user_id JOIN comments ON messages.id=comments.message_id'
            posted_comments = mysql_connection.query_db(query)
            #if there are messages, load all messages
            if len(posted_messages) > 0:
                message_empty = False
                return render_template('wall.html',template_first_name=first_name,template_posted_messages=posted_messages,template_posted_comments=posted_comments,template_message_empty=message_empty)       
            #else, there is no message to be viewed
            else:
                return render_template('wall.html',template_first_name=first_name,template_message_empty=message_empty,template_homeaddress=homeaddress)

#log out by clearing session and sending user back to login page    
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
    
app.run(debug=True)