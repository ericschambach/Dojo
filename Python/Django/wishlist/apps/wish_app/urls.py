from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login$', views.login),    
    url(r'^registration$', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^wish_items/create$', views.add_item),
    url(r'^add_to_wish$', views.add_to_wish),
    # url(r'^travels_process$', views.add_travels_process),
    # url(r'^travels_join_process$',views.join_trip),
    # url(r'^travels/destination/(?P<id>[0-9]+)$', views.destination),
    url(r'^clear$', views.clear),
]