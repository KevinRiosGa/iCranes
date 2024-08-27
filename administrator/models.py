from django.db import models

# Create your models here.

class Regiones(models.Model):
    nombre = models.CharField(max_length=100)

class Comunas(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Regiones, on_delete=models.CASCADE)

class UnidadMedida(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50)

class Empresas(models.Model):
    rut = models.CharField(max_length=8)
    dvRut = models.CharField(max_length=1)
    razSoc = models.CharField(max_length=150)
    nomFant = models.CharField(max_length=150)
    giro = models.CharField(max_length=150)
    codigo = models.CharField(max_length=5)
    

