from django.urls import path
from apptienda.views import *
from appmascotas.views import *

urlpatterns = [
    path('mascotas/', vista_mascotas, name="vet-mascotas"),
]