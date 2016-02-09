from django.shortcuts import render
from .models import trabajador
from .models import tiposDeServicio

# Create your views here.
def index (request):
    trabajadores = trabajador.objects.all()
    context = {'trabajadores':trabajadores}
    return  render(request, 'polls/templates/index.html', context)

def servicios (request):
    tiposDeServicios = tiposDeServicio.objects.all()
    context = {'tiposDeServicios':tiposDeServicios}
    return  render(request, 'polls/templates/tiposDeServicios.html', context)