from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', showmain),
    path('log_key/', posted, name='posted'),
]
