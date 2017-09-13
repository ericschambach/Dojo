from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^process_money$',views.calculate_coins),
    url(r'^clear$',views.clear_coins),
]