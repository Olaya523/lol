from django.urls import path, include

from .views import *

urlpatterns = [
    path('cliente/',cliente),
    #path('get/',getCliente),
    #path('post/',postCliente),
    #path('put/<int:id>',putCliente),
]
