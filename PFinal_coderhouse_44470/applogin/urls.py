from django.urls import path
from apptienda.views import *
from appmascotas.views import *
from applogin.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', vista_login, name="vet-login"),
    path('registro/', vista_registro, name="vet-registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="vet-logout"),
    path('perfil/', vista_perfil, name="vet-perfil"),
]