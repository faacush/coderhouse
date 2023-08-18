from django.db import models

# Create your models here.

class Entrenamientos(models.Model):
    entrenamiento = models.CharField(max_length=50)
    duracion = models.IntegerField()
    tipo = models.CharField(max_length=15)
    precio = models.BooleanField()
    descripcion = models.CharField(max_length=250)


class Nutricion(models.Model):
    plan = models.CharField(max_length=50)
    duracion = models.IntegerField()
    tipo = models.CharField(max_length=15)
    precio = models.BooleanField()
    descripcion = models.CharField(max_length=250)


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.BooleanField()
    descripcion = models.CharField(max_length=250)
