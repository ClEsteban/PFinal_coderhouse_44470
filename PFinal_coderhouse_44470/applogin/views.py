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
def editar_perfil(request):
    
    usuario = request.user

    if request.method == "POST":
        #formulario = UserEditForm(request.POST)
        pass

    else:
        #formulario = UserEditForm(initial={"first_name", "last_name", "email"})
        pass
    
    return render(request, "editar_perfil.html")