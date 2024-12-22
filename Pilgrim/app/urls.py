
from django.urls import path

# from app.views import create_movie

from .views import *
from . import views

urlpatterns = [
    path('log/', views.log, name='log'),
path('log/2.html', views.home, name='home'),

]


