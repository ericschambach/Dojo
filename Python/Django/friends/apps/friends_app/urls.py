from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^login$', views.login),    
    url(r'^registration$', views.registration),
    url(r'^friends$', views.friends),
    url(r'^make_connection$',views.make_connection),
    url(r'^remove_connection/(?P<id>[0-9]+)$',views.remove_connection),
    url(r'^user/(?P<id>[0-9]+)$', views.user),
    url(r'^clear$', views.clear),
]