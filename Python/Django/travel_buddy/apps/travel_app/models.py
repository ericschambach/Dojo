# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import localtime, now
from django.forms import DateTimeField


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def add_user(self,name_input,username_input,password_input):
        self.name_input=name_input
        self.username_input=username_input
        self.password_input=password_input
        User.objects.create(name=name_input,username=username_input,password=password_input)
    def select_all_users(self):
        return User.objects.all()
    def select_one_user_by_username(self,username_input):
        self.username_input = username_input
        try: 
            User.objects.get(username=self.username_input)
        except:
            return False
        return User.objects.get(username=self.username_input)
    def select_one_user_by_id(self,id_input):
        self.id_input=id_input
        return User.objects.get(id=id_input)
    def match_password(self,username_input,password_input):
        self.username_input = username_input
        self.password_input = password_input
        user = User.objects.get(username=self.username_input)
        return user
    def get_last_User(self):
        return User.objects.last()

class Trip(models.Model):
    user = models.ForeignKey(User,related_name="Creator")
    destination = models.CharField(max_length=255)
    description = models.TextField()
    travel_date_from = models.DateTimeField(auto_now=False)
    travel_date_to = models.DateTimeField(auto_now=False)
    traveler = models.ManyToManyField(User,related_name="travelers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def create_trip(self,user_input,destination_input,descrition_input,travel_date_from_input,travel_date_to_input):
        self.user_input=user_input
        self.destination_input=destination_input
        self.descrition_input=descrition_input
        self.travel_date_from_input=travel_date_from_input
        self.travel_date_to_input=travel_date_to_input
        Trip.objects.create(user=self.user_input,destination=self.destination_input,description=self.descrition_input,travel_date_from=self.travel_date_from_input,travel_date_to=self.travel_date_to_input)
    def select_all_trips(self):
        return Trip.objects.all()
    def select_one_trip(self,id_input):
        self.id_input = id_input
        return Trip.objects.get(id=self.id_input)
    def select_one_trip_by_name(self,destination):
        self.destination = destination
        try:
            Trip.objects.values_list('destination',flat=True).distinct().get(destination=self.destination)
        except:
            return False
        return True
    def get_last_trip(self):
        return Trip.objects.last()
    def new_join_table(self,trip_input,user_input):
        self.user_input=user_input
        self.trip_input=trip_input
        trip_input.traveler.add(self.user_input)
        trip_input.save()
    def filter_other_users_in_trip(self,trip_id,user_id):
        self.user_id = user_id
        self.trip_id = trip_id
        other_travelers = Trip.objects.exclude(traveler__id=self.trip_id).exclude(traveler__id=self.user_id)
        return other_travelers
    def other_travelers_trips(self,trip_id,user_id):
        self.user_id = user_id
        self.trip_id = trip_id
        other_trips_travelers = Trip.objects.exclude(traveler__id=self.trip_id).exclude(traveler__id=self.user_id)
        return other_trips_travelers
    def filter_all_your_trips(self,user_id):
        self.user_name = user_name
        self.user_id = user_id
        your_trips = Trip.objects.filter(traveler__user=self.user_id)
        return your_trips
        

