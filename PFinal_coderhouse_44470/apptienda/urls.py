from django.urls import path
from apptienda.views import *
from appmascotas.views import *
from applogin.views import *


urlpatterns = [
    path('', vista_inicio, name="tienda-inicio"),
    path('tienda/', vista_tienda, name="vet-tienda"),
    path('tienda/comprar/<id>', vista_comprar_producto, name="vet-comprar"),
    path('about/', vista_about, name="vet-about"),
        
]