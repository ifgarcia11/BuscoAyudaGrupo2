from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from .models import trabajador
from .models import tiposDeServicio
from .models import TrabajadorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
def servicios (request):
    tiposDeServicios = tiposDeServicio.objects.all()
    context = {'tiposDeServicios':tiposDeServicios}
    return  render(request, 'tiposDeServicios.html', context)

def index(request):
    # return HttpResponse('Hello from Python!')
    trabajadores = trabajador.objects.all()
    context = {'trabajadores':trabajadores}
    return render(request, 'index.html',context)


def add_userView(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            usuario = cleaned_data.get('usuario')
            nombre = cleaned_data.get('nombre')
            apellidos = cleaned_data.get('apellidos')
            aniosExperiencia = cleaned_data.get('aniosExperiencia')
            telefono = cleaned_data.get('telefono')
            imagen = cleaned_data.get('imagen')
            correo = cleaned_data.get('correo')
            contrasenia = cleaned_data.get('contrasenia')
            contrasenia2 = cleaned_data.get('contrasenia2')

            User_Model = User.objects.create_user(username=usuario, password=contrasenia)
            User_Model.first_name=usuario
            User_Model.last_name=usuario
            User_Model.email = correo
            User_Model.save()
            return HttpResponseRedirect('/registro_exitoso')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('registro.html',args)



def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_exitoso')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('registro.html',args)

def registroExitoso(request):
    return render(request, 'registro_exitoso.html')

def login (request):
    login = {}
    login.update(csrf(request))
    return  render_to_response('login.html', login)

def auth_view (request):
    username= request.POST.get('usuario' , '')
    password= request.POST.get('contrasenia' , '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        return render(request, 'registro_exitoso.html')

