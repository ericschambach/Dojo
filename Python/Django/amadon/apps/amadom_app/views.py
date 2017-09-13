# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return redirect('/amadon')

def home(request):
    return render(request,"index.html")

def process(request):
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
    if 'total_price' not in request.session:
        request.session['total_price'] = 0
    items = [
    {
        "id": 1,
        "name": "Dojo T-Shirt",
        "price": 19.99,
    },
    {
        "id": 2,
        "name": "Dojo Sweater",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Dojo Cup",
        "price": 4.99
    },
    {
        "id": 4,
        "name": "Algorithm Book",
        "price": 49.99
    }]
    request.session["price"] = float(request.POST['price'])
    request.session["quantity"] = int(request.POST['quantity'])
    request.session['total_quantity'] = request.session['total_quantity'] + request.session["quantity"]
    request.session['total_price'] = request.session['total_price'] + (request.session["price"] * request.session["quantity"])
    return redirect('/checkout')

def checkout(request):
    if 'price' not in request.session:
        return redirect('/')
    else:
        price = request.session["price"]
        quantity = request.session['quantity']
        total_quantity = request.session['total_quantity']
        total_price = request.session['total_price']
        context = {
            'html_price': price,
            'html_quantity': quantity,
            'html_total_price': total_price,
            'html_total_quantity': total_quantity
        }
        return render(request,'checkout.html',context)

def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
