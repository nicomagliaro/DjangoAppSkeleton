from django import forms
from django.contrib.auth.models import User
#from django.forms.utils import ErrorList

"""
class DivErrorList(ErrorList):

        Esta clase sobrescribe el modulo ErrorList de los formularios de Django para pasarle un valor customizado
    def __str__(self):              # __unicode__ on Python 2
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="alert alert-danger" role="alert">%s</div>' % (e for e in self)"""

class ContactForm(forms.Form):
    Email   = forms.EmailField(widget=forms.TextInput())
    Titulo  = forms.CharField(widget=forms.TextInput())
    Texto   = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
    email    = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
    password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya existe')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya registrado')

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('Password no coinciden')
