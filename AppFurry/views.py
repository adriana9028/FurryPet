from django.shortcuts import render
from .models import *

# Create your views here.

def layout(request):
    return render(request, 'layout.html')

def index(request):
    return render(request, 'index.html')