from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appmascotas.models import *
from appmascotas.forms import *
from django.views.generic import ListView


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

def mascota_editar(request, id):
    mascota = mascotas.objects.get(id=id)

    if request.method == "POST":
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            mascota.nombre = data["nombre"]
            mascota.tipo = data["tipo"]
            mascota.raza = data["raza"]
            mascota.imagen = data["imagen"]
            mascota.descripcion = data["descripcion"]
            mascota.save()
            return redirect("vet-mascotas")
        else:
            return render(request, "mascota-editar", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = MascotaFormulario(initial={"nombre":mascota.nombre, "tipo":mascota.tipo, "raza":mascota.raza, "imagen":mascota.imagen, "descripcion":mascota.descripcion})
        return render(request, "editar_mascota.html", {"formulario": formulario, "errores": ""})
