# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<h3>Hello World</h3>')

# Create your views here.
