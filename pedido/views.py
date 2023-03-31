from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import path

# Create your views here.
def hello(Request):
    return HttpResponse("gnrreasPEDIDO")

def pedido(Request):
    return render(Request,'pedido.html')

