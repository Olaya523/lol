from .models import articulo
from rest_framework import ModelSerializer

class articuloSerializer(ModelSerializer):
    class Meta:
        model = articulo
        fields = '__all__'
