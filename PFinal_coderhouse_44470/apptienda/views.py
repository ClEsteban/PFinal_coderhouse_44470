from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from apptienda.models import *

#vista de la pagina inicio
def vista_inicio(request):
    return render(request, "apptienda/inicio.html")

def vista_tienda(request):
    productos = Productos.objects.all()
    contexto = {"productos":productos}
    return render(request, "apptienda/productos.html", contexto)

def vista_about(request):
    return render(request, "apptienda/about.html")

def vista_comprar_producto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect("vet-tienda")