from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from apptienda.models import *
# from apptienda.forms import *
# Create your views here.

#vista de la pagina inicio
def vista_inicio(request):
    return render(request, "apptienda/inicio.html")

#def vista_tienda(request):
#    return render(request, "apptienda/tienda.html")

def vista_tienda(request):
    productos = Productos.objects.all()
    contexto = {"productos":productos}
    return render(request, "apptienda/productos.html", contexto)

def vista_about(request):
    return render(request, "apptienda/about.html")