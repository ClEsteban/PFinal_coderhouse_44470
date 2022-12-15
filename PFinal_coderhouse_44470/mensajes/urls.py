from django.urls import path
from mensajes.views import *


urlpatterns = [
    path('mensajes/', vista_contacto, name="vet-mensajes")
]