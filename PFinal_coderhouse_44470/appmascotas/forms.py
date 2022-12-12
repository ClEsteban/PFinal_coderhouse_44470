from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(min_length=3,max_length=50)
    tipo = forms.CharField(min_length=3,max_length=50)
    # imagen = forms.ImageField(upload_to='Imagenes/',null= True)
    descripcion = forms.TextInput()
    raza = forms.CharField(min_length=3,max_length=50)