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
    return render(request,'index.html')

# def main(request):
#     return render(request,'main.html')

def registration(request):
    name = str(request.POST['name'])
    email = str(request.POST['email'])
    password = request.POST['password']
    pw_confirm = request.POST['pw_confirm']
    birthday = datetime.strptime(request.POST['app_date'], "%Y-%m-%d")

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
    try:
        birthday = datetime.strptime(request.POST['app_date'], "%Y-%m-%d")
    except:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*You have to include your birthday!")
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        register_user = User()
        if register_user.select_one_user_by_email(email) is not False:
            messages.add_message(request, messages.ERROR, '*This e-mail belongs to a registered user! - Either Log In or register with another e-mail')
            return redirect('/')
        else:
            register_user.add_user(name,email,password,birthday)
            request.session['id'] = register_user.get_last_User().name
            request.session['name'] = register_user.get_last_User().name
            request.session['email'] = register_user.get_last_User().email
            return redirect('/appointments')

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
                return redirect('/appointments')

def appointment(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        email = request.session['email']
        user = User()
        you = user.select_one_user_by_email(email)
        appointment = Appointment()
        appointments_today = appointment.filter_appointments_by_logged_user(user.select_one_user_by_email(email))
        later_appointments = appointment.filter_appointments_by_logged_user(user.select_one_user_by_email(email))
        
        for i in appointments_today:
            if i.appointment.date() > datetime.today().date() or i.appointment.date() < datetime.today().date():
                i.appointment = 'Not'
        for i in later_appointments:
            if i.appointment.date() == datetime.today().date() or i.appointment.date() < datetime.today().date():
                i.appointment = 'Not'
                print i.appointment

        context = {
            'appoint':appointments_today,
            'logged': you,
            'later': later_appointments,
            'today': datetime.today().date(),
            'time_now':datetime.now().time(),
        }
        return render(request,'homepage.html',context)

def add_appointment(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        
        email = request.session['email']
        tasks = request.POST['tasks']
        is_valid = True
        if len(tasks)<1:            
            messages.add_message(request, messages.ERROR,"*You have to provide a comment for tasks!")
            is_valid = False    
        try:
            app_date = datetime.strptime(request.POST['app_date'], "%Y-%m-%d")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide a date for the appointment!")
            is_valid = False
        try:
            app_time = datetime.strptime(request.POST['app_time'], "%H:%M")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide time of the day!")
        if is_valid ==False:
            return redirect('/appointments')
        else:
            if datetime.today().date() > app_date.date():
                messages.add_message(request, messages.ERROR,"*Appointment day cannot be from earlier than today!")
                is_valid = False
            if datetime.now().time() > app_time.time() and datetime.today().date() == app_date.date():
                messages.add_message(request, messages.ERROR,"*Appoiment time cannot be before now!")
                is_valid = False
            if is_valid ==False:
                return redirect('/appointments')
            else:
                app_final = datetime.combine(datetime.date(app_date), datetime.time(app_time))
                user = User()
                appointment = Appointment()
                app_id = request.POST['app_id']
                user.select_one_user_by_email(email)
                appointment.add_appointment(tasks,app_final,user.select_one_user_by_email(email))
                return redirect('/appointments')

def update(request,id):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        id_input = id
        appointment = Appointment()
        yourappointment = appointment.select_one_appointment(id_input)
        context = {
            'appointment':yourappointment,
        }
        return render(request,'update_page.html',context)

def update_process(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        app_id = int(request.POST['app_id'])
        appointment = Appointment()
        yourappointment = appointment.select_one_appointment(app_id)
        new_tasks = request.POST['tasks']
        new_status = request.POST['tasks']
        is_valid = True
        if len(new_tasks)<1:
            new_tasks = yourappointment.task
            messages.add_message(request, messages.ERROR, "*You have not changed tasks field!")
        if len(new_status)<1:
            new_status = yourappointment.status
            messages.add_message(request, messages.ERROR, "*You have not changed status field!")
        try:
            app_date = datetime.strptime(request.POST['app_date'], "%Y-%m-%d")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide a date for the appointment!")
            is_valid = False
        try:
            app_time = datetime.strptime(request.POST['app_time'], "%H:%M")
        except:
            messages.add_message(request, messages.ERROR,"*You have to provide time of the day!")
            is_valid = False
        if is_valid ==False:
            return redirect('/appointments/'+str(app_id))
        else:
            if datetime.today().date() > app_date.date():
                messages.add_message(request, messages.ERROR,"*Appointment day cannot be from earlier than today!")
                is_valid = False
            if datetime.now().time() > app_time.time() and datetime.today().date() == app_date.date():
                messages.add_message(request, messages.ERROR,"*Appoiment time cannot be before now!")
                is_valid = False
            if is_valid ==False:
                return redirect('/appointments/'+str(app_id))
            else:
                app_final = datetime.combine(datetime.date(app_date), datetime.time(app_time))
                appointment.update_appointment(new_tasks,new_status,app_final,app_id)
                return redirect('/appointments')

def delete_appointment(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        id_input = request.POST['app_id']
        appointment = Appointment()
        appointment.delete_appointment(id_input)
        return redirect('/appointments')

def clear(request):
    if 'email' not in request.session and 'name' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        request.session.clear()
        return redirect('/')

# Create your views here.
