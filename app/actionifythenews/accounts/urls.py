from django.urls import path

from . import views
from django.urls import path
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]