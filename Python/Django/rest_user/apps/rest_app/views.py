# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import re
from .models import User

def home(request):
    return redirect('/users')

def new_user(request):
    return render(request,'new_user.html')

def user_list(request):
    select_users = User()
    users = select_users.select_all_users()
    context = {
        'results': users
    }
    return render(request,'userlist.html',context)

def register(request):
    print 'request route'
    first_name = str(request.POST['html_first_name'])
    last_name = str(request.POST['html_last_name'])
    email = str(request.POST['html_email'])
    isvalid = True
    if len(first_name) < 3:
        isvalid = False
    if len(last_name) < 3:
        isvalid = False
    if len(email) < 3:
        isvalid = False
    if isvalid == False:
        print ('Go back')
        return redirect('/users/new')
    else:
        register_user = User()
        register_user.add_user(first_name,last_name,email)
        print 'if worked!'
        print type(first_name)
        return redirect('/users')

def user_information(request,id):
    if request.method == 'POST':
        edit_first_name = str(request.POST['html_first_name'])
        edit_last_name = str(request.POST['html_last_name'])
        edit_email = str(request.POST['html_email'])
        input_id = id
        user = User()
        user_edit = user.select_one_user(input_id)
        context = {
            'results': user_edit
        }
        if len(edit_first_name) >= 3:
            user_edit.first_name=edit_first_name
            user_edit.save()
        if len(edit_last_name) >= 3:
            user_edit.last_name=edit_last_name
            user_edit.save()
        if len(edit_email) >= 3:
            user_edit.email=edit_email
            user_edit.save()
        address = '/users/'+str(id)
        return redirect(address)
    else:
        input_id = id
        user = User()
        users = user.select_one_user(input_id)
        context = {
            'results': users
        }
        return render(request,'userdetails.html',context)

def edit_user(request,id):
    input_id = id
    user = User()
    users = user.select_one_user(input_id)
    context = {
        'results': users
    }
    return render(request,'edit_user.html',context)

def end_user(request,id):
    input_id = id
    user = User()
    end_user = user.select_one_user(input_id)
    end_user.delete()
    return redirect('/users')


# Create your views here.
