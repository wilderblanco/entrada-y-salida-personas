from django.db import models

# Create your models here.

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo_Documento = models.CharField(max_length=30)
    Numero = models.CharField(max_length=15, unique=True)
    Nombres = models.CharField(max_length=25)
    Apellidos =	models.CharField(max_length=25)
    Lugar_Procedencia =	models.CharField(max_length=13)
    Correo = models.EmailField()	
    Telefono =	models.CharField(max_length=15)
    Fecha_Ingreso =	models.DateField(auto_now_add=True)
    Fecha_Salida =	models.DateField()
    Tipo_Vinculacion = models.CharField(max_length=16)
    Dependencia = models.CharField(max_length=35)	
    Tipo_Vehiculo = models.CharField(max_length=10)	
    Placa_Vehiculo = models.CharField(max_length=10)	
    Objeto_Visita =	models.TextField(max_length=100)
    Observacion = models.TextField(max_length=100)
