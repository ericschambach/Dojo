# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,'login.html')

def registration(request):
    first_name = str(request.POST['first_name'])
    last_name = str(request.POST['last_name'])
    email = str(request.POST['email'])
    password = request.POST['password']
    pw_confirm = request.POST['pw_confirm']
    form_reproved = False
    if len(first_name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*First Name has to be at least 3 characters!")
    if first_name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*First Name can only hold alphabetic characters!")
    if len(last_name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Last Name has to be at least 3 characters!")
    if last_name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Last Name can only hold alphabetic characters!")
    if len(password)< 4:
        messages.add_message(request, messages.ERROR, "*Password has to be at least 4 characters long!")
        form_reproved = True
    if len(password)>= 4 and len(pw_confirm)< 1:
        messages.add_message(request, messages.ERROR, "*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pw_confirm)>= 1) and password != pw_confirm:
        messages.add_message(request, messages.ERROR, "*Passwords do not match!")
        form_reproved = True
    if password.isnumeric() == True or password.isalpha() == True or password.islower() == True or password.isupper() == True:
        messages.add_message(request, messages.ERROR, '*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(request.POST['email']) < 1:
        messages.add_message(request, messages.ERROR, '*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        messages.add_message(request, messages.ERROR, "*Invalid Email Address!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    if form_reproved == True:
        return redirect('/')
    else:
        print password
        password = md5.new(password).hexdigest()
        print password
        register_user = User()
        register_user.add_user(first_name,last_name,email,password)
        request.session['first_name'] = first_name
        print 'last stop'
        return redirect('/homepage')

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
        try:
            user = User()
            username = user.select_one_user(email)
        except:
            messages.add_message(request, messages.ERROR,"*Username (e-mail) does not exist")
            return redirect('/')
        print username.email
        if username.password != password:
            messages.add_message(request, messages.ERROR,"*Password does not match username")
            return redirect('/')
        else:
            request.session['first_name'] = username.first_name
            return redirect('/homepage')

def homepage(request):
    if 'first_name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        username = request.session['first_name']
        print username
        context = {
            'results': username
        }
        return render(request,'homepage.html',context)

def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
