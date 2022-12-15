from django.urls import path
from apptienda.views import *
from appmascotas.views import *
from applogin.views import *


urlpatterns = [
    path('mascotas/', vista_mascotas, name="vet-mascotas"),
    path('mascotas/borrar/<id>', mascota_borrar, name="mascota-borrar"),
    path('mascotas/editar/<id>', mascota_editar, name="mascota-editar"), 
    path('mascotas/create', MascotaCrear.as_view(), name="mascota-create"),
    path('mascotas/update/<pk>', MascotaActualizar.as_view(), name="mascota-update"),
    path('mascotas/detail/<pk>', MascotaDetalle.as_view(), name="mascota-detail"),
    path('mascotas/list', MascotaList.as_view(), name="mascota-list"),
    path('mascotas/delete/<pk>', MascotaBorrar.as_view(), name="mascota-delete"),
    

]