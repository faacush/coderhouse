from django.shortcuts import render
from .models import Entrenamientos, Nutricion


# Create your views here.
def home(request):
    return render(request, "fitness/home.html")

def entrenamientos(request):
    contexto = {'entrenamientos': Entrenamientos.objects.all() }
    return render(request, "fitness/entrenamientos.html", contexto)

def nutricion(request):
    contexto = {'nutricion': Nutricion.objects.all() }
    return render(request, "fitness/nutricion.html")

def productos(request):
    return render(request, "fitness/productos.html")

def contacto(request):
    return render(request, "fitness/contacto.html")