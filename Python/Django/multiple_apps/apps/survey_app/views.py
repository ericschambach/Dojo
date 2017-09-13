# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('display placeholder for users to create a new user record')

def new(request):
    return HttpResponse('display placeholder for users to create a new user record')