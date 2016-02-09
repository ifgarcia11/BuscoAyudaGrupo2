from django.conf.urls import patterns,url

from polls import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
        url(r'^tiposDeServicios/$', views.servicios, name='tiposDeServicios')


]