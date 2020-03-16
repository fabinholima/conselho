
from django.contrib import admin
from django.urls import path
from escola.views import *

app_name = 'escola'

urlpatterns = [
    path('escola', EscolaHome, name="home"),
]