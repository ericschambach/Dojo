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
    alias = str(request.POST['alias'])
    email = str(request.POST['email'])
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
        messages.add_message(request, messages.ERROR, "*Password has to be at least 4 characters long!")
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
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        register_user = User()
        if register_user.select_one_user_by_email(email) is not False:
            messages.add_message(request, messages.ERROR, '*This e-mail belongs to a registered user! - Either Log In or register with another e-mail')
            return redirect('/')
        else:
            register_user.add_user(name,alias,email,password,birthday)
            request.session['name'] = register_user.get_last_User().name
            request.session['alias'] = register_user.get_last_User().alias
            request.session['email'] = register_user.get_last_User().email
            return redirect('/quotes')

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
                request.session['alias'] = username.alias
                request.session['email'] = username.email
                return redirect('/quotes')

def homepage(request):
    if 'name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        quote = Quote()
        user = User()
        user_mail = request.session['email']
        all_quotes = quote.select_all_quote()
        like = Like()
        alias = request.session['alias']
        favorites = like.select_all_likes()
        context = {
            'alias': alias,
            'quotes':all_quotes,
            'favorites':favorites,
            'email': user_mail
        }
        return render(request,'homepage.html',context)

def quote_process(request):
    quote = Quote()
    user = User()
    text = str(request.POST['quote_message'])
    author = str(request.POST['new_quote_author'])
    email = request.session['email']
    quote.add_quote(text,author,user.select_one_user_by_email(email))
    return redirect('/quotes')

def users(request,id):
    user_id = id
    quote = Quote()
    user = User()
    like = Like()
    favorites = like.select_all_likes()
    this_user = user.select_one_user_by_id(user_id)
    creator = quote.select_quotes_by_creator(user.select_one_user_by_id(user_id))
    total_created = quote.select_quotes_by_creator(user.select_one_user_by_id(user_id)).count()
    context = {
        'creator' : creator,
        'user': this_user,
        'count':total_created,
        'favorites': favorites
    }
    return render(request,'author.html',context)

def add_to_list(request):
    user = User()
    quote = Quote()
    like = Like()
    email = request.session['email']
    quote_id = int(request.POST['quote_id'])
    like.create_liked_quote(user.select_one_user_by_email(email),quote.select_one_quote(quote_id))
    return redirect ('/quotes')

def clear(request):
    if 'name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    request.session.clear()
    return redirect('/')
    

# Create your views here.
