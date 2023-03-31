from django.urls import path, include

from .views import *

urlpatterns = [
    path('articulo/',articulo),
    #path('get/',getArticulo),
    #path('post/',postArticulo),
    #path('put/<int:id>',putArticulo),
    #
]
