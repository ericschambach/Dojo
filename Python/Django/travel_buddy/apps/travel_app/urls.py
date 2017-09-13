from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login$', views.login),    
    url(r'^registration$', views.registration),
    url(r'^travels$', views.travels),
    url(r'^travels/add$', views.add_travels),
    url(r'^travels_process$', views.add_travels_process),
    url(r'^travels_join_process$',views.join_trip),
    url(r'^travels/destination/(?P<id>[0-9]+)$', views.destination),
    url(r'^clear$', views.clear),
]