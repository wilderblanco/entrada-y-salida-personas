from django.db import models

def capitalize_words(text):
    """ Capitaliza la primera letra de cada palabra en el texto. """
    return ' '.join(word.capitalize() for word in text.split())

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo_Documento = models.CharField(max_length=30)
    Numero = models.CharField(max_length=15)
    Nombres = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    Lugar_Procedencia = models.CharField(max_length=13)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=15)
    Fecha_Ingreso = models.DateTimeField(auto_now_add=True)
    Fecha_Salida = models.DateTimeField(blank=True, null=True, auto_now=True)
    Tipo_Vinculacion = models.CharField(max_length=16)
    Dependencia = models.CharField(max_length=35)
    Tipo_Vehiculo = models.CharField(max_length=10)
    Placa_Vehiculo = models.CharField(max_length=10)
    Objeto_Visita = models.TextField(max_length=100)
    Observacion = models.TextField(max_length=100)
    Actualizado = models.BooleanField(default=False)  # Nuevo campo
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
            # Aplicar capitalización a los campos que lo requieren
            self.Nombres = capitalize_words(self.Nombres)
            self.Apellidos = capitalize_words(self.Apellidos)
            self.Lugar_Procedencia = capitalize_words(self.Lugar_Procedencia)
            self.Tipo_Documento = self.Tipo_Documento.capitalize()
            self.Numero = self.Numero.capitalize()
            self.Correo = self.Correo.lower()  # Normalizar a minúsculas por convención
            self.Telefono = self.Telefono.capitalize()
            self.Tipo_Vinculacion = self.Tipo_Vinculacion.capitalize()
            self.Dependencia = self.Dependencia.capitalize()
            self.Tipo_Vehiculo = self.Tipo_Vehiculo.capitalize()
            self.Placa_Vehiculo = self.Placa_Vehiculo.upper()  # Normalizar a mayúsculas por convención
            self.Objeto_Visita = self.Objeto_Visita.capitalize()
            self.Observacion = self.Observacion.capitalize()

            super().save(*args, **kwargs)
            
            
        