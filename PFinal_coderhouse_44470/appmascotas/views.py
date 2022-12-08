from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from apptienda.models import *

# Create your views here.
def vista_mascotas(request):
    return render(request, "cargatumascota.html")