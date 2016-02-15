from __future__ import unicode_literals

from django.contrib.auth.forms import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.forms import ModelForm


class tiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=1000)

class trabajador (models.Model):
   nombre = models.CharField(max_length=1000)
   apellidos = models.CharField(max_length=1000)
   aniosExperiencia = models.IntegerField()
   tiposDeServicio = models.ForeignKey(tiposDeServicio,null=True)
   telefono = models.CharField(max_length=1000)
   correo = models.CharField(max_length=1000)
   imagen = models.CharField(max_length=1000,default='')
   usuario = models.CharField(max_length=1000,default='')
   contrasenia = models.CharField(max_length=1000,default='')


class comentario (models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(trabajador,null=True)

class TrabajadorForm (ModelForm):

   nombre = forms.CharField(max_length=50)
   apellidos = forms.CharField(max_length=50)
   aniosExperiencia = forms.IntegerField()
   telefono = forms.CharField(max_length=50)
   correo = forms.CharField(max_length=50)
   imagen = forms.CharField(max_length=50)
   usuario = forms.CharField(max_length=50)
   contrasenia = forms.CharField(widget = forms.PasswordInput())
   contrasenia2 = forms.CharField(widget = forms.PasswordInput())

   class Meta:
     model = User
     fields = ['nombre','apellidos','aniosExperiencia','telefono','correo','imagen','usuario','contrasenia','contrasenia2']


def clean_userName(self):
    usuario = self.cleaned_data(['usuario'])
    if usuario.objects.filter(usuario=usuario):
        raise forms.ValidationError('Usuario ya registrado')
    return usuario

def clean_email(self):
    correo= self.cleaned_data(['correo'])
    if correo.objects.filter(correo=correo):
        raise forms.ValidationError('correo ya registrado')
    return correo

def clean_password2(self):
    contrasenia = self.cleaned_data(['contrasenia'])
    contrasenia2 = self.cleaned_data(['contrasenia2'])
    if contrasenia!=contrasenia2:
            raise forms.ValidationError('contrasenias no coinciden ya registrado')
    return contrasenia2