from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('entrenamientos/', entrenamientos, name = "entrenamientos"),
    path('nutricion/', nutricion, name = "nutricion"),
    path('productos/', productos, name = "productos"),
    path('contacto/', contacto, name = "contacto"),
]