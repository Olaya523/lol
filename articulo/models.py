from django.db import models

# Create your models here.

class Articulos(models.Model):
    id=models.PositiveIntegerField(primary_key=True,null=False)
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    seccion=models.CharField(max_length=20)
    precio=models.FloatField()

    def __str__(self):
        return self.id, self.nombre, self.descripcion, self.seccion, self.precio, 

