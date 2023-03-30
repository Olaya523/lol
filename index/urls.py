from django.urls import path, include

from cliente import views
from pedido import views
from articulo import views
from index import views


urlpatterns = [
    path('',views.hello),
    path('index/',views.index),
]
