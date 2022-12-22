from .models import mascotas
from django.forms import ModelForm, CharField, ImageField, TextInput, FileInput

class MascotaFormulario(ModelForm):
    nombre = CharField(widget= TextInput(attrs={"class": 'form-control'}), required=True )
    tipo = CharField(widget= TextInput(attrs={"class": 'form-control'}))
    imagen = ImageField(widget= FileInput( attrs={ "class": 'form-control'}))
    descripcion = CharField(widget=TextInput(attrs={"class": 'form-control'}))
    raza = CharField(widget= TextInput(attrs={"class": 'form-control'}))
    class Meta:
        model = mascotas
        fields = [
            'nombre',
            'tipo',
            'imagen',
            'descripcion',
            'raza'
        ]