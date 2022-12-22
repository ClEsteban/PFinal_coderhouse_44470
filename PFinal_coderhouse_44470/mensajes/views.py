from django.shortcuts import render, redirect
from mensajes.models import Mensajes, Messaje
import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def vista_contacto(request):
    mensajes = Mensajes.objects.all()
    if request.method == 'POST':
        if len(dict(request.POST)) > 1:
            fecha1 = datetime.datetime.now()
            msg = Mensajes(sender=request.user,msg_content=request.POST['msg_input'],fecha=fecha1)
            msg.save()
        return redirect('tienda-contacto')
    return render(request,'mensajes.html',{'mensajes':mensajes})

class MessajeCrear(CreateView):
   model = Messaje
   success_url = "/contacto/mensajes/list"
   fields = ["mensaje"]

class MessajeList(ListView):
    model = Messaje
    template_name = "messaje_list.html"