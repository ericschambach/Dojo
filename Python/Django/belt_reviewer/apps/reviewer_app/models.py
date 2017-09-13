# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import localtime, now


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_user(self,first_name_input,last_name_input,email_input,password_input):
        self.first_name_input=first_name_input
        self.last_name_input=last_name_input
        self.email_input=email_input
        self.password_input=password_input
        User.objects.create(first_name=first_name_input,last_name=last_name_input,email=email_input,password=password_input)
    def select_all_users(self):
        return User.objects.all()
    def select_one_user_by_email(self,email_input):
        self.email_input = email_input
        try: 
            User.objects.get(email=self.email_input)
        except:
            return False
        return User.objects.get(email=self.email_input)
    def select_one_user_by_id(self,id_input):
        self.id_input=id_input
        return User.objects.get(id=id_input)
    def match_password(self,email_input,password_input):
        self.email_input = email_input
        self.password_input = password_input
        user = User.objects.get(email=self.email_input)
        return user
    def get_last_User(self):
        return User.objects.last()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_book(self,title_input,author_input):
        self.title_input=title_input
        self.author_input=author_input
        Book.objects.create(title=self.title_input,author=self.author_input)
    def select_all_books(self):
        return Book.objects.all()
    def select_one_book(self,id_input):
        self.id_input = id_input
        return Book.objects.get(id=self.id_input)
    def select_one_book_by_name(self,title_input):
        self.title_input = title_input
        try:
            Book.objects.values_list('title',flat=True).distinct().get(title=self.title_input)
        except:
            return False
        return True
    def get_last_book(self):
        return Book.objects.last()
    def select_distinct_authors(self):
        return Book.objects.values_list('author', flat=True).distinct().order_by('author')    

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User,related_name="reviews_left")
    book = models.ForeignKey(Book,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_review(self,review_input,rating_input,user_input,book_input):
        self.review_input=review_input
        self.rating_input=rating_input
        self.user_input = user_input
        self.book_input = book_input
        Review.objects.create(review=self.review_input,rating=self.rating_input,user=self.user_input,book=self.book_input)
    def select_all_reviews(self):
        return Review.objects.all()
    def select_only_books(self):
        return Review.objects.values_list('book', flat=True).order_by('-id')[:3]
    def select_filter_by_book(self,book_input):
        self.book_input = book_input
        return Review.objects.filter(book=self.book_input)
    def select_filter_by_user(self,user_input):
        self.user_input = user_input
        return Review.objects.filter(user=self.user_input)
    def select_user_who_posted(self,user_input,book_input):
        self.user_input = user_input
        self.book_input = book_input
        if Review.objects.filter(user=self.user_input,book=self.book_input):
            return True
        else:
            return False
        
