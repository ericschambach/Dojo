# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime
from datetime import datetime


def index(request):
    if 'results' not in request.session:
        context = {}
    else:
        context = request.session['results']
    return render(request,'index.html',context)

def make_results(request):
    if len(request.POST['new_word'])> 1:
        html_new_word = request.POST['new_word']
        html_color = request.POST['color']
        if 'results' not in request.session:
            resultlist = [{'word': html_new_word,
            'color': html_color}]
            request.session['results'] = {'listdicts':[]}
            return redirect('/')
        else:
            resultslist = [{'word': html_new_word,
            'color': html_color}]
            request.session['results']['listdicts']['word'].append('{}    - added on {}'.format(html_new_word,strftime("%b %d, %Y %H:%M %p",gmtime())))
            request.session.modified = True
            request.session['results']['listdicts']['color'].append('{}    - added on {}'.format(html_color,strftime("%b %d, %Y %H:%M %p",gmtime())))
            request.session.modified = True
            print request.session['results']
            return redirect('/')
        

def clear(request):
    request.session.clear()
    return redirect('/')
