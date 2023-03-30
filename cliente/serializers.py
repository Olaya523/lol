from .models import cliente
from rest_framework import ModelSerializer

class clienteSerializer(ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
