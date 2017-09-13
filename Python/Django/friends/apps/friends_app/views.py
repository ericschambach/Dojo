# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime, localtime
from datetime import datetime,date
import time
import md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return redirect('/main')

def main(request):
    return render(request,'main.html')

def registration(request):
    name = str(request.POST['name'])
    email = str(request.POST['email'])
    alias = str(request.POST['alias'])
    password = request.POST['password']
    pw_confirm = request.POST['pw_confirm']
    form_reproved = False
    try:
        birthday = datetime.strptime(request.POST['birthday'], "%Y-%m-%d")
    except:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Include a date of birth")
    if len(name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Name has to be at least 3 characters!")
    if name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Name can only hold alphabetic characters!")
    if len(alias) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Alias has to be at least 3 characters!")
    if len(password)< 8:
        messages.add_message(request, messages.ERROR, "*Password has to be at least 8 characters long!")
        form_reproved = True
    if len(password)>= 8 and len(pw_confirm)< 1:
        messages.add_message(request, messages.ERROR, "*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pw_confirm)>= 1) and password != pw_confirm:
        messages.add_message(request, messages.ERROR, "*Passwords do not match!")
        form_reproved = True
    if len(request.POST['email']) < 1:
        messages.add_message(request, messages.ERROR, '*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        messages.add_message(request, messages.ERROR, "*Invalid Email Address!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        register_user = User()
        if register_user.select_one_user_by_email(email) is not False:
            messages.add_message(request, messages.ERROR, '*This e-mail belongs to a registered user! - Either Log In or register with another e-mail')
            return redirect('/')
        if register_user.select_one_user_by_alias(alias) is False:
            messages.add_message(request, messages.ERROR, '*This alias has already been added to an existing user! You will have to choose another one')
            return redirect('/')
        if birthday.date() > datetime.today().date():
            messages.add_message(request, messages.ERROR, '*Birthday date cannot be after today')
            return redirect('/')
        else:
            register_user.add_user(name,alias,email,password,birthday)
            request.session['id'] = register_user.get_last_User().id
            request.session['name'] = register_user.get_last_User().name
            request.session['email'] = register_user.get_last_User().email
            return redirect('/friends')

def login(request):
    email=str(request.POST['email'])
    password=(request.POST['password'])
    is_valid=True
    if len(email) < 1:
        messages.add_message(request, messages.ERROR,"*You have to provide an user name!")
        is_valid = False
    if len(password) < 1:
        messages.add_message(request, messages.ERROR,"*You have to provide a password!")
        is_valid = False
    if is_valid ==False:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        user = User()
        if user.select_one_user_by_email(email) is False:
            messages.add_message(request, messages.ERROR,"*Username (e-mail) does not exist")
            return redirect('/')
        else:
            username = user.select_one_user_by_email(email)
            if username.password != password:
                messages.add_message(request, messages.ERROR,"*Password does not match username")
                return redirect('/')
            else:
                request.session['name'] = username.name
                request.session['id'] = username.id
                request.session['email'] = username.email
                return redirect('/friends')

def friends(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        user = User()
        connections = user.get_connections(user.select_one_user_by_email(request.session['email']).alias)
        you = user.select_one_user_by_email(request.session['email'])
        conn_count = len(connections)
        all_users = user.select_all_users()
        non_connections = user.get_nonconnections(user.select_one_user_by_email(request.session['email']).alias,user.select_one_user_by_email(request.session['email']).id)
        context = {
            'you': you,
            'connections': connections,
            'users': all_users,
            'non_connections':non_connections,
            'conn_count':conn_count,
        }
        return render(request,'friends.html',context)

def make_connection(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        user = User()
        connection_id = request.POST['connection_id']
        connection = user.select_one_user_by_id(connection_id)
        user.new_connection(user.select_one_user_by_email(request.session['email']),user.select_one_user_by_id(connection_id))
        return redirect('/friends')

def remove_connection(request,id):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        user = User()
        connection_id = id
        connection = user.select_one_user_by_id(connection_id)
        user.remove_connection(user.select_one_user_by_email(request.session['email']),user.select_one_user_by_id(connection_id))
        return redirect('/friends')

def user(request,id):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        user = User
        user_id = int(id)
        user_profile = User.objects.get(id=user_id)
        context = {
            'user':user_profile,
        }
        return render(request,'user.html',context)

def clear(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        request.session.clear()
        return redirect('/')
    

# Create your views here.
