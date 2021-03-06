"""BuscoAyudaGrupo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
import polls.urls
urlpatterns = [
    url(r'^$', polls.views.index, name='index'),
        url(r'^tiposDeServicios/', polls.views.servicios, name='tiposDeServicios'),
    url(r'^admin/', include(admin.site.urls)),
                url(r'^registro/$',polls.views.register, name='registro'),
    url(r'^registro_exitoso/$',polls.views.registroExitoso, name='registro_exitoso'),
                    url(r'^login/$',polls.views.login, name='login'),
                        url(r'^auth/$',polls.views.auth_view),
                                 url(r'^logout/$',polls.views.logout),
                    url(r'^detalle/$',polls.views.detalle, name='detalle'),
                    url(r'^perfil/$',polls.views.perfil, name='perfil'),



]


