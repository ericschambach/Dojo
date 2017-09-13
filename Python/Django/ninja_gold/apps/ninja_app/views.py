# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect
import random
import datetime

def index(request):
    if 'my_gold' not in request.session:
        request.session['my_gold'] = 0
    if 'my_result' not in request.session:
        request.session['my_result'] = 0
    if 'result_log' not in request.session:
        request.session['result_log'] = []

    
    bet = request.session['result_log']
    gold = request.session['my_gold']
    context = {
        'html_bet':bet,
        'html_gold':gold
    }
    return render(request,'index.html',context)

def calculate_coins(request):
    bet_type = (str(request.POST['building']))
    results = {'farm':{'min': 10,'max':20},'cave':{'min': 5,'max':10},'house':{'min': 2,'max':5},'casino':{'min': -50,'max':50}}
    request.session['result'] = random.randint(results[bet_type]['min'],results[bet_type]['max'])
    request.session['my_gold'] = request.session['my_gold'] + request.session['result']
    time = datetime.datetime.now()
    if bet_type == 'casino' and request.session['result'] < 0:
        request.session['result_log'].append('Entered the {} and lost {} golds... Ouch! {}'.format(bet_type.capitalize(),abs(request.session['result']),time))
        request.session.modified = True
    if bet_type == 'casino' and request.session['result'] > 0:
        request.session['result_log'].append('Entered the {} and won {} golds... WOW! {}'.format(bet_type.capitalize(),request.session['result'],time))
        request.session.modified = True
    if bet_type == 'casino' and request.session['result'] == 0:
        request.session['result_log'].append('Entered the {} and no wins! {}'.format(bet_type.capitalize(),time))
        request.session.modified = True
    if bet_type != 'casino':
        request.session['result_log'].append('Earned {} golds from the {}! {}'.format(request.session['result'],bet_type.capitalize(),time))
        request.session.modified = True
    return redirect('/')

def clear_coins(request):
    request.session.clear()
    return redirect('/')