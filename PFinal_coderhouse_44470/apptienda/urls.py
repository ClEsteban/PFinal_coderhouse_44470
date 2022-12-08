from django.urls import path
from apptienda.views import *
from appmascotas.views import *

urlpatterns = [
    path('inicio/', vista_inicio, name="tienda-inicio"),
    path('tienda/', vista_tienda, name="vet-tienda"),
    path('about/', vista_about, name="vet-about"),
    
]