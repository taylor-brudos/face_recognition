from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detect/$', views.detect),
    url(r'^$', views.index),
]
