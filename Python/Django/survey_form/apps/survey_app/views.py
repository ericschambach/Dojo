# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return render(request,"index.html")

def form_validation(request):
    if len(request.POST['user_username']) < 1 or len(request.POST['user_description']) > 120:
        if len(request.POST['user_username']) < 1:
            # flash("*Name cannot be empty!")
            return redirect('/')                
        if len(request.POST['user_description']) > 120:
            # flash("*Comment section cannot exceed 120 characters!")
            return redirect('/')
    request.session["user_username"] = request.POST['user_username']
    request.session["user_location"] = request.POST['user_location']
    request.session["user_language"] = request.POST['user_language']
    request.session["user_description"] = request.POST['user_description']
    return redirect('/results')

def form_results(request):
    username = request.session["user_username"]
    location = request.session["user_location"]
    language = request.session["user_language"]
    description = request.session["user_description"]
    context = {
        'html_username': username,
        'html_location': location,
        'html_language': language,
        'html_description': description
    }
    return render(request,'results.html',context)

def backtosurvey(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
