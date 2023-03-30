from .models import pedido
from rest_framework import ModelSerializer

class pedidoSerializer(ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'
