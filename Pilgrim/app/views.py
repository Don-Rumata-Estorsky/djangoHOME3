from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *


def log(request):
    return render(request, 'log.html')

def home(request):
    return render(request, 'home.html')




