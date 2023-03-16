from django.shortcuts import render
from .models import *

# Create your views here.

def Ppadre(request):
    return render(request, 'Recursos/Ppadre.html')

def index(request):
    return render(request, 'Recursos/index.html')