# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_user(self,first_name_input,last_name_input,email_input):
        self.first_name_input=first_name_input
        self.last_name_input=last_name_input
        self.email_input=email_input
        User.objects.create(first_name=first_name_input,last_name=last_name_input,email=email_input)
    def select_all_users(self):
        return User.objects.all()
    def select_one_user(self,id_input):
        self.id_input = id_input
        return User.objects.get(id=self.id_input)
        
    # def update_user(self,id_input,first_name=,lastn):
    #     self.first_name_input=first_name_input
    #     self.last_name_input=last_name_input
    #     self.email_input=email_input
    #     record = User.objects.get(id = user_id)
        
