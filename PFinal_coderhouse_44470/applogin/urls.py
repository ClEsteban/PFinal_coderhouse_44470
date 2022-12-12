from django.urls import path
from apptienda.views import *
from appmascotas.views import *
from applogin.views import *


urlpatterns = [
    path('', vista_login, name="vet-login"),

]