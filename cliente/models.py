from django.db import models

# Create your models here.

class Clientes(models.Model):
    id=models.PositiveIntegerField(primary_key=True,null=False)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

    def __str__(self):
        return self.id,self.nombre,self.apellido,self.direccion,self.email,self.telefono

