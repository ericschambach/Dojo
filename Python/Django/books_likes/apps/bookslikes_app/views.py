# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return HttpResponse('Hello')
    

# Create your views here.
