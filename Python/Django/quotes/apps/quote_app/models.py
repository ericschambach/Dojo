# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import localtime, now


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_user(self,name_input,alias_input,email_input,password_input,birthday_input):
        self.name_input=name_input
        self.alias_input=alias_input
        self.email_input=email_input
        self.password_input=password_input
        self.birthday_input=birthday_input
        User.objects.create(name=self.name_input,alias=self.alias_input,email=self.email_input,password=self.password_input,birthday=self.birthday_input)
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

class Quote(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    creator = models.ForeignKey(User,related_name="quote_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_quote(self,text_input,author_input,creator_input):
        self.text_input=text_input
        self.author_input=author_input
        self.creator_input = creator_input
        Quote.objects.create(text=self.text_input,author=self.author_input,creator = self.creator_input)
    def select_all_quote(self):
        return Quote.objects.all()
    def select_one_quote(self,id_input):
        self.id_input = id_input
        return Quote.objects.get(id=self.id_input)
    def select_quotes_by_creator(self,creator_id):
        self.creator_id = creator_id
        quotes_by_creator = Quote.objects.filter(creator=self.creator_id)
        return quotes_by_creator

class Like(models.Model):
    creator = models.ForeignKey(User,related_name="user_who_liked")
    quote = models.ForeignKey(Quote,related_name="quote_liked")
    def create_liked_quote(self,user_id,quote_id):
        self.user_id = user_id
        self.quote_id = quote_id
        Like.objects.create(creator = self.user_id,quote=self.quote_id)
    def select_all_likes(self):
        return Like.objects.all()
    def select_likable(self,user_id,quote_id):
        self.user_id = user_id
        self.quote_id = quote_id
        selLike.objects.filter(creator = self.user_id,quote=self.quote_id)
    

    # def select_one_quote_by_tex(self,title_input):
    #     self.title_input = title_input
    #     try:
    #         Book.objects.values_list('title',flat=True).distinct().get(title=self.title_input)
    #     except:
    #         return False
    #     return True
    # def get_last_book(self):
    #     return Book.objects.last()
    # def select_distinct_authors(self):
    #     return Book.objects.values_list('author', flat=True).distinct().order_by('author')    

# class Review(models.Model):
#     review = models.TextField()
#     rating = models.IntegerField()
#     user = models.ForeignKey(User,related_name="reviews_left")
#     book = models.ForeignKey(Book,related_name='reviews')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def add_review(self,review_input,rating_input,user_input,book_input):
#         self.review_input=review_input
#         self.rating_input=rating_input
#         self.user_input = user_input
#         self.book_input = book_input
#         Review.objects.create(review=self.review_input,rating=self.rating_input,user=self.user_input,book=self.book_input)
#     def select_all_reviews(self):
#         return Review.objects.all()
#     def select_only_books(self):
#         return Review.objects.values_list('book', flat=True).order_by('-id')[:3]
#     def select_filter_by_book(self,book_input):
#         self.book_input = book_input
#         return Review.objects.filter(book=self.book_input)
#     def select_filter_by_user(self,user_input):
#         self.user_input = user_input
#         return Review.objects.filter(user=self.user_input)
#     def select_user_who_posted(self,user_input,book_input):
#         self.user_input = user_input
#         self.book_input = book_input
#         if Review.objects.filter(user=self.user_input,book=self.book_input):
#             return True
#         else:
#             return False
        
