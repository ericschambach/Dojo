from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  
    url(r'^main$', views.main),  
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^quotes$', views.homepage),
    url(r'^add_quote$', views.quote_process),
    url(r'^add_to_list$', views.add_to_list),
    url(r'^users/(?P<id>[0-9]+)$', views.users),
    url(r'^clear$', views.clear),
]