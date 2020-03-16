from django.urls import path , include, re_path
from agenda.views import *

app_name='agenda'
urlpatterns = [
    path('agenda', AgendaHome, name="agenda"),
]