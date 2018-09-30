from django.urls import path

from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]