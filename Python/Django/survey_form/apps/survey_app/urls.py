from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^process$',views.form_validation),
    url(r'^results$',views.form_results),
    url(r'^clear$',views.backtosurvey),
]