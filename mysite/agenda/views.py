from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
    
def AgendaHome(request):
    return render (request, 'Hello Word')