from django.db import models

# Create your models here.

class Pedidos(models.Model):
    numeroID=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return self.numeroID,self.fecha,self.entregado

