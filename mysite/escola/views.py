from django.shortcuts import render

# Create your views here.
def EscolaHome(request):
    return render (request, "escola/escola.html")