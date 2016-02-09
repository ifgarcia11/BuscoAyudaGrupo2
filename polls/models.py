from __future__ import unicode_literals

from django.db import models

# Create your models here.
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

class comentario (models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(trabajador,null=True)
