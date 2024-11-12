
from django.db import models

# Create your models here.

class Producto(models.Model):
    Id_Producto=models.CharField(primary_key=True,max_length=6)
    Precio=models.IntegerField()
    Marca=models.CharField(max_length=100)
    Calidad=models.CharField(max_length=100)
    Recibido=models.CharField(max_length=100)
    Proovedor=models.CharField(max_length=100)
    Cantidad=models.IntegerField()
    
    def __str__(self):
        return self.Marca
