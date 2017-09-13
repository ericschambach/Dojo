# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime, localtime
from datetime import datetime,date
import time
import md5

def main(request):
    context = {}
    return render(request,'main.html')

def registration(request):
    name = str(request.POST['name'])
    username = str(request.POST['username'])
    password = request.POST['password']
    pw_confirm = request.POST['pw_confirm']
    form_reproved = False
    if len(name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Name has to be at least 3 characters!")
    if name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Name can only hold alphabetic characters!")
    if len(username) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Username has to be at least 3 characters!")
    if len(password)< 8:
        messages.add_message(request, messages.ERROR, "*Password has to be at least 8 characters long!")
        form_reproved = True
    if len(password)>= 8 and len(pw_confirm)< 1:
        messages.add_message(request, messages.ERROR, "*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pw_confirm)>= 1) and password != pw_confirm:
        messages.add_message(request, messages.ERROR, "*Passwords do not match!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        register_user = User()
        if register_user.select_one_user_by_username(username) is not False:
            messages.add_message(request, messages.ERROR, '*This e-mail belongs to a registered user! - Either Log In or register with another e-mail')
            return redirect('/')
        else:
            register_user.add_user(name,username,password)
            request.session['name'] = register_user.get_last_User().name
            request.session['username'] = register_user.get_last_User().username
            request.session['id'] = register_user.get_last_User().id
    return redirect('/dashboard')

def login(request):
    username=str(request.POST['username'])
    password=(request.POST['password'])
    is_valid=True
    if len(username) < 1:
        messages.add_message(request, messages.ERROR,"*You have to provide an username!")
        is_valid = False
    if len(password) < 1:
        messages.add_message(request, messages.ERROR,"*You have to provide a password!")
        is_valid = False
    if is_valid ==False:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        user = User()
        if user.select_one_user_by_username(username) is False:
            messages.add_message(request, messages.ERROR,"*Username (e-mail) does not exist")
            return redirect('/')
        else:
            logged_user = user.select_one_user_by_username(username)
            if logged_user.password != password:
                messages.add_message(request, messages.ERROR,"*Password does not match username")
                return redirect('/')
            else:
                request.session['name'] = logged_user.name
                request.session['username'] = logged_user.username
                request.session['id'] = logged_user.id
                return redirect('/dashboard')

def dashboard(request):
    if 'name' not in request.session and 'username' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        user = User()
        item = Item()
        yourself = user.select_one_user_by_username(request.session['username'])
        your_items = item.filter_other_users_wishlist(user.select_one_user_by_username(request.session['username']).id)
        other_items = item.get_other_users_wishlist(user.select_one_user_by_username(request.session['username']).id)
        # yourtrips = trip.filter_all_your_trips(yourself.id)
        # yourname = request.session['name'] 
        context = {
            'you': yourself,
            'items': your_items,
            'other': other_items,
        }
        return render(request,'dashboard.html',context)

def add_item(request):
    return render(request,'create_item.html')

def add_to_wish(request):
    username = request.session['username']
    new_item = str(request.POST['item'])
    user = User()
    item = Item()
    item.new_join_table(item.select_one_item(new_item),user.select_one_user_by_username(username))
    return redirect('/dashboard')

def add_travels_process(request):
    if 'name' not in request.session and 'username' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        username = request.session['username']
        new_item = str(request.POST['item'])
        is_valid = True
        if len(new_item) < 1:
            messages.add_message(request, messages.ERROR,"*You have to an item name!")
            is_valid = False
        if is_valid ==False:
            return redirect('/wish_items/create')
        else:
            user = User()
            item = Item()
            user_creator = user.select_one_user_by_username(username)
            item.create_item(user.select_one_user_by_username(username),new_item)
            item_input = item.get_last_item()
            item.new_join_table(item.get_last_item(),user.select_one_user_by_username(username))
            return redirect('/dashboard')

def destination(request,id):
    if 'name' not in request.session and 'username' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    destination_id = int(id)
    user = User()
    trip = Trip()
    yourself = user.select_one_user_by_username(str(request.session['username']))
    this_trip = trip.select_one_trip(destination_id)
    trip_filter = trip.filter_other_users_in_trip(destination_id,yourself.id)
    yourname = request.session['name'] 
    context = {
        'you': yourself,
        'trip': this_trip,
        'filter': trip_filter
    }
    return render(request,'destination.html',context)

# def join_trip(request):
#     if 'name' not in request.session and 'username' not in request.session:
#         messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
#         return redirect('/')
#     username = request.session['username']
#     user = User()
#     trip = Trip()
#     this_trip = int(request.POST['this_trip'])
#     new_traveler = user.select_one_user_by_username(username)
#     trip_input = trip.select_one_trip(this_trip)
#     trip.new_join_table(trip_input,new_traveler)
#     address = '/travels/destination/'+str(this_trip)
#     return redirect(address)

def clear(request):
    if 'name' not in request.session and 'username' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    request.session.clear()
    return redirect('/')

# Create your views here.
