from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appmascotas.models import *
from appmascotas.forms import *


def vista_mascotas(request):

    # formulario de carga de mascotas
    if request.method == "POST":
        formulario = MascotaFormulario(request.post)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Mascota = mascotas(nombre=data["nombre"], tipo=data["tipo"], raza=data["raza"], imagen=data["imagen"], descripcion=data["descripcion"])
            Mascota.save()

    # listado de mascotas:
    Mascotas = mascotas.objects.all()

    # crea formulario vacio
    formulario = MascotaFormulario()
    contexto = {"mascotas":Mascotas, "formulario":formulario}

    return render(request, "cargatumascota.html", contexto)

def mascota_borrar(request, id):
    mascota = mascotas.objects.get(id=id)
    mascota.delete()
    return redirect("vet-mascotas")
