from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from .models import trabajador,UserProfile
from .models import tiposDeServicio
from .models import TrabajadorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.context_processors import csrf
from .models import UserForm, UserProfileForm

# Create your views here.
def servicios (request):
    tiposDeServicios = tiposDeServicio.objects.all()
    context = {'tiposDeServicios':tiposDeServicios}
    return  render(request, 'tiposDeServicios.html', context)

def index(request):
    # return HttpResponse('Hello from Python!')
    trabajadores = UserProfile.objects.all()
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
            correo = cleaned_data.get('correo')
            contrasenia = cleaned_data.get('contrasenia')

            User_Model = User.objects.create_user(username=usuario, password=contrasenia)
            User_Model.username=usuario
            User_Model.first_name=nombre
            User_Model.last_name=apellidos
            User_Model.email =correo
            User_Model.save()
            trab = trabajador()
            trab.nombre=nombre
            trab.apellidos=apellidos
            trab.save()
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

def logout (request):
    auth.logout(request)
    return render(request, 'logout.html')

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user


            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'registro.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def detalle(request):
    return render(request, 'detalle.html')