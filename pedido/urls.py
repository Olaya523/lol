from django.urls import path, include

from .views import *

urlpatterns = [
    path('pedido/',pedido),
    #path('get/',getPedido),
    #path('post/',postPedido),
    #path('put/<int:id>',putPedido),
    #
]
