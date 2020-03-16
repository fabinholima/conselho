#from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
    

from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
from rest_framework import filters, viewsets, mixins

def AgendaHome(request):
    return render (request, "agenda/agenda.html")

