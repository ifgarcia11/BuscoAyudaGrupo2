from django.shortcuts import render
from .models import trabajador
from .models import tiposDeServicio

# Create your views here.
def servicios (request):
    tiposDeServicios = tiposDeServicio.objects.all()
    context = {'tiposDeServicios':tiposDeServicios}
    return  render(request, 'polls/templates/tiposDeServicios.html', context)

def index(request):
    # return HttpResponse('Hello from Python!')
    trabajadores = trabajador.objects.all()
    context = {'trabajadores':trabajadores}
    return render(request, 'index.html',context)