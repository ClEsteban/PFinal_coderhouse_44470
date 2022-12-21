from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from applogin.models import *
from applogin.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def vista_login(request):

    errors = ""
    

    # formulario de carga de mascotas
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("tienda-inicio")
            else:
                return render(request, "login.html", {"formulario":formulario, "errors":"credenciales invalidas"})
        else:
            return render(request, "login.html", {"formulario":formulario, "errors":"CREDENCIALES INVALIDAS"})

    formulario = AuthenticationForm()
    return render(request, "login.html", {"formulario":formulario})

def vista_registro(request):
   
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("tienda-inicio")
        else:
            return render(request, "registro.html", {"formulario":formulario, "errors":formulario.errors})
       
    formulario = UserRegisterForm()

    return render(request, "registro.html", {"formulario":formulario})

@login_required
def ver_perfil(request):
    user = request.user
    
    if request.user.is_authenticated:
        try:
            imagen_model = Avatar.objects.filter(user=request.user.id)[0]
            imagen_url = imagen_model.imagen.url
        except:
            imagen_url = ""
    contexto = {"user":user, "imagen_url":imagen_url}
    return render(request, 'perfil.html', contexto)


@login_required
def editar_perfil(request):
    
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.fist_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("tienda-inicio")
        else:
            return render(request, "editar_perfil.html", {"formulario":formulario, "errros":formulario.errors})

    else:
        formulario = UserEditForm(initial={"first_name":usuario.first_name, "last_name":usuario.last_name, "email":usuario.email})
    
    return render(request, "editar_perfil.html", {"formulario":formulario})

@login_required
def añadir_avatar(request):
        def agregar_avatar(request):
            formulario = CrearAvatarForm()
    
        if request.method == "POST":
             formulario = CrearAvatarForm(request.POST, files=request.FILES)
    
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data['imagen'],github=data['github'],descripcion=data['descripcion'])
            avatar.save()

            return redirect('vet-login')
        else:
            return render(request, 'editar_perfil.html', {'formulario': formulario, 'errors': formulario.errors })