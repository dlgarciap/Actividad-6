from django import forms
from .models import Student, Publisher, Authorizer, Publication
from django.contrib.auth.models import User


# ----- FORMULARIOS PRINCIPALES -----
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'student_id': 'Carnet',
            'email': 'Correo electrónico',
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }


class AuthorizerForm(forms.ModelForm):
    class Meta:
        model = Authorizer
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'date', 'author']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'date': 'Fecha de publicación',
            'author': 'Autor',
        }


# ----- REGISTRO DE USUARIO -----
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password': 'Contraseña'
        }
        help_texts = { 
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
