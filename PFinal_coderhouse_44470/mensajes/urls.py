from django.urls import path
from mensajes.views import *



urlpatterns = [
    path('mensajes/', vista_contacto, name="vet-mensajes"),
    path('mensajes/create', MessajeCrear.as_view(), name="mensaje-create"),
    path('mensajes/list', MessajeList.as_view(), name="mensaje-list"),
]