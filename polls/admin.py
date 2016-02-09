from django.contrib import admin
from .models import tiposDeServicio,trabajador,comentario
# Register your models here.
admin.site.register(tiposDeServicio)
admin.site.register(comentario)
admin.site.register(trabajador)