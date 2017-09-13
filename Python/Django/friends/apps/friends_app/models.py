# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import localtime, now
from django.forms import DateTimeField
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(auto_now=False)
    friend = models.ManyToManyField('self',related_name="connection")
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
    def select_one_user_by_alias(self,alias_input):
        self.alias_input = alias_input
        try: 
            User.objects.get(alias=self.alias_input)
        except:
            return True
        return False
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
    def new_connection(self,user_input,friend_input):
        self.user_input = user_input
        self.friend_input = friend_input
        user_input.friend.add(self.friend_input)
        user_input.save()
    def get_connections(self,user_input):
        self.user_input = user_input
        return User.objects.filter(friend__alias=user_input)
    def get_nonconnections(self,user_input,user_id):
        self.user_input = user_input
        self.user_id = user_id
        return User.objects.exclude(friend__alias=user_input).exclude(id=user_id)
    def remove_connection(self,user_input,friend_input):
        self.user_input = user_input
        self.friend_input = friend_input
        user_input.friend.remove(self.friend_input)
        user_input.save()  
