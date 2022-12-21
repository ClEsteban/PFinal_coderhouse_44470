from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField


class LoginForm(forms.ModelForm):
    username = CharField(label="Usuario", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        exclude = ["password1", "password2"]


class CrearAvatarForm(forms.Form):
    imagen = forms.ImageField()
    descripcion = forms.CharField()
