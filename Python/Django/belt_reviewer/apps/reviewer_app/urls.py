from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),    
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add_book),
    url(r'^book_process$', views.book_process),
    url(r'^books/(?P<id>[0-9]+)$', views.book_profile),
    url(r'^users/(?P<id>[0-9]+)$', views.user_page),
    url(r'^review_process$', views.add_review_process),
    url(r'^clear$', views.clear),
]