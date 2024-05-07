from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', showmain),
    path('login/', login, name='login'),
    path('get/', getUserData),
]
