# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    unique_id = get_random_string(length=14)
    context = {
        'html_count': request.session['count'],
        'html_unique_id': unique_id
    }
    return render(request,'index.html',context)

def reset_count(request):
    request.session.clear()
    return redirect('/')

    

# Create your views here.
