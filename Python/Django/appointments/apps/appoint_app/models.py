# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import localtime, now
from django.forms import DateTimeField
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_user(self,name_input,email_input,password_input,birthday_input):
        self.name_input=name_input
        self.email_input=email_input
        self.password_input=password_input
        self.birthday_input=birthday_input
        User.objects.create(name=self.name_input,email=self.email_input,password=self.password_input,birthday=self.birthday_input)
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

class Appointment(models.Model):
    task = models.CharField(max_length=255)
    appointment = models.DateTimeField(auto_now=False)
    person = models.ForeignKey(User,related_name='person_with_appointment')
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def add_appointment(self,task_input,appointment_input,person_input):
        self.task_input=task_input
        self.appointment_input = appointment_input
        self.person_input = person_input
        Appointment.objects.create(task=self.task_input,appointment=self.appointment_input,person=self.person_input,status='Pending')
    def select_all_appointments(self):
        return Appointment.objects.all()
    def filter_appointments_by_logged_user(self,user_input):
        self.user_input=user_input
        return Appointment.objects.filter(person=user_input).order_by('appointment')
    def select_one_appointment(self,id_input):
        self.id_input = id_input
        return Appointment.objects.get(id=self.id_input)
    def update_appointment(self,task_input,status_input,appointment_input,app_id):
        self.task_input = task_input
        self.appointment_input = appointment_input
        self.status_input = status_input
        self.app_id = app_id
        b = Appointment.objects.get(id=self.app_id)
        b.task=self.task_input
        b.save()
        b.status=self.status_input
        b.save()
        b.appointment=self.appointment_input
        b.save()
    def delete_appointment(self,app_id):
        self.app_id = app_id
        b = Appointment.objects.get(id=self.app_id)
        b.delete()
    def todays_appointments(self,user_input,time_input):
        self.user_input = user_input
        self.time_input = time_input
        return Appointment.objects.filter(appointment=self.time_input).filter(person=user_input)
