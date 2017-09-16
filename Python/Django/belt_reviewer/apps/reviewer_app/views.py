# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime, localtime
import md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request,'login.html')

def registration(request):
    first_name = str(request.POST['first_name'])
    last_name = str(request.POST['last_name'])
    email = str(request.POST['email'])
    password = request.POST['password']
    pw_confirm = request.POST['pw_confirm']
    form_reproved = False
    if len(first_name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*First Name has to be at least 3 characters!")
    if first_name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*First Name can only hold alphabetic characters!")
    if len(last_name) < 3:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Last Name has to be at least 3 characters!")
    if last_name.isalpha == False:
        form_reproved = True
        messages.add_message(request, messages.ERROR, "*Last Name can only hold alphabetic characters!")
    if len(password)< 4:
        messages.add_message(request, messages.ERROR, "*Password has to be at least 4 characters long!")
        form_reproved = True
    if len(password)>= 4 and len(pw_confirm)< 1:
        messages.add_message(request, messages.ERROR, "*Please confirm password!")
        form_reproved = True
    if (len(password)>= 1 and len(pw_confirm)>= 1) and password != pw_confirm:
        messages.add_message(request, messages.ERROR, "*Passwords do not match!")
        form_reproved = True
    if password.isnumeric() == True or password.isalpha() == True or password.islower() == True or password.isupper() == True:
        messages.add_message(request, messages.ERROR, '*Password is requred to have at least 1 uppercase, 1 lowercase letter and 1 numeric value!')
        form_reproved = True
    if len(request.POST['email']) < 1:
        messages.add_message(request, messages.ERROR, '*Email cannot be blank!')
        form_reproved = True
    if len(email) < 1 or not EMAIL_REGEX.match(email):
        messages.add_message(request, messages.ERROR, "*Invalid Email Address!")
        form_reproved = True
    if form_reproved == True:
        return redirect('/')
    if form_reproved == True:
        return redirect('/')
    else:
        password = md5.new(password).hexdigest()
        register_user = User()
        if register_user.select_one_user_by_email(email) is not False:
            messages.add_message(request, messages.ERROR, '*This e-mail belongs to a registered user! - Either Log In or register with another e-mail')
            return redirect('/')
        else:
            register_user.add_user(first_name,last_name,email,password)
            request.session['first_name'] = register_user.get_last_User().first_name
            request.session['email'] = register_user.get_last_User().email
            return redirect('/books')

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
            messages.add_message(request, messages.ERROR, "*Username (e-mail) does not exist")
            return redirect('/')
        else:
            user.select_one_user_by_email(email)
            if username.password != password:
                messages.add_message(request, messages.ERROR,"*Password does not match username")
                return redirect('/')
            else:
                request.session['first_name'] = username.first_name
                request.session['email'] = username.email
                return redirect('/books')

def books(request):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        reviews = Review()
        books = Book()
        recent_reviews = reviews.select_all_reviews().order_by('-id')[:3]
        filtered_reviews = reviews.select_only_books()
        remaining_reviews = books.select_all_books()
        username = request.session['first_name'] 
        context = {
            'name': username,
            'reviews': recent_reviews,
            'remaining_reviews': remaining_reviews,
            'filtered': filtered_reviews,
        }
        return render(request,'books.html',context)

def add_book(request):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        book = Book()
        rating = range(1,6)
        book_list = book.select_distinct_authors()
        context = {
            'results': book_list,
            'rating': rating
        }
        return render(request,'add_book.html',context)

def book_process(request):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    title = str(request.POST['title'])
    author = str(request.POST['new_author'])
    review = str(request.POST['review'])
    book = Book()
    try:
        author_select = str(request.POST['author_select'])
    except:
        author_select = False
    try:
        rating = int(request.POST['rating'])
    except:
        rating = False
    print author_select
    isvalid = True
    if len(title) <1:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*Please include a book title")
    if book.select_one_book_by_name(title) is True:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*A book with the same name has already been added")
    if len(author) <1 and author_select is False:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*Please choose one author")
    if len(author) >1 and author_select is not False:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*Please choose just one author in one field")
    if len(review)<1:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*Please write a review for this book")
    if rating is False:
        isvalid = False
        messages.add_message(request, messages.ERROR, "*Please rate the book")
    if isvalid == False:
        return redirect('/books/add')
    else:
        register_user = Book()
        if len(author) < 1:
            author = author_select
        email_input = request.session['email']
        user = User()
        review_class = Review()
        book.add_book(title,author)
        book_id = int(book.get_last_book().id)
        review_class.add_review(review,rating,user.select_one_user_by_email(email_input),book.get_last_book())                  
        return redirect('/books/'+str(book_id))
        

def book_profile(request,id):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    else:
        rating = range(1,6)
        book_id = int(id)
        book = Book()
        reviews = Review()
        user = User()
        book_reviews = reviews.select_filter_by_book(book_id)
        chosen_book = book.select_one_book(book_id) 
        context = {'book_results': chosen_book,
                    'review_results': book_reviews,
                    'ratings': rating,
        }
        return render(request,'book_reviews.html',context)
    
def add_review_process(request):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    email_input = request.session['email']
    review = str(request.POST['review'])
    book_id = int(request.POST['book_id'])
    is_valid=True
    try:
        new_rating = request.POST['rating']
    except:
        messages.add_message(request, messages.ERROR, "*You have rate the book!")
        is_valid=False
    if len(review) < 1:
        messages.add_message(request, messages.ERROR, "*You have to write a review!")
        is_valid=False  
    user = User()
    book = Book()
    review_class = Review()
    user_id = int(user.select_one_user_by_email(email_input).id)
    if review_class.select_user_who_posted(user_id,book_id) is True:        
        messages.add_message(request, messages.ERROR, "*You have already reviewed this book!")
        is_valid = False
    if is_valid == False:
        return redirect('/books/'+str(book_id))         
    else:     
        review_class.add_review(review,new_rating,user.select_one_user_by_email(email_input),book.select_one_book(book_id))  
        return redirect('/books/'+str(book_id))

def user_page(request,id):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    user_id = int(id)
    user = User()
    user_selected = user.select_one_user_by_id(user_id)
    review = Review()
    reviewed_books = review.select_filter_by_user(user_id)
    total_reviewed = review.select_filter_by_user(user_id).count()
    context = {
        'user': user_selected,
        'book': reviewed_books,
        'total': total_reviewed
    }
    return render(request,'user_profile.html',context)

def clear(request):
    if 'first_name' not in request.session and 'email' not in request.session:
        messages.add_message(request, messages.ERROR,"*You have to be logged in first!")
        return redirect('/')
    request.session.clear()
    return redirect('/')