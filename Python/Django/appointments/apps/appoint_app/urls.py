from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),    
    url(r'^registration$', views.registration),
    url(r'^appointments$', views.appointment),
    url(r'^add_appointment$', views.add_appointment),
    url(r'^appointments/(?P<id>[0-9]+)$', views.update),
    url(r'^update_process$', views.update_process),
    url(r'^delete_appointment$', views.delete_appointment),
    url(r'^clear$', views.clear),
]