from django.conf.urls import patterns,url

from polls import views
from django.contrib import admin
admin.autodiscover()
import polls.views

urlpatterns = [
    url(r'^$', polls.views.index, name='index'),
            url(r'^tiposDeServicios/$',polls.views.servicios, name='tiposDeServicios')

]