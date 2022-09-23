from django.db import models

# Create your models here.

class Banco(models.Model):

    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    tipoBco = models.CharField(max_length=10)

class Empleado(models.Model):

    nombre = models.CharField(max_length=60)
    legajo = models.IntegerField()
    correo = models.EmailField()

class Servicio(models.Model):

    nombre = models.CharField(max_length=60)
    tipoServ = models.CharField(max_length=20)

class Sucursal(models.Model):

    numero = models.IntegerField()
    localidad = models.CharField(max_length=60)
    horaApertura = models.IntegerField()
    horaCierre = models.IntegerField()
