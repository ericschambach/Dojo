from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^users$', views.user_list),
    url(r'^users/new$', views.new_user),
    url(r'^register$', views.register),
    url(r'^users/(?P<id>[0-9]+)$',views.user_information),
    url(r'^users/(?P<id>[0-9]+)/edit$',views.edit_user),
    url(r'^users/(?P<id>[0-9]+)/destroy$',views.end_user),
]