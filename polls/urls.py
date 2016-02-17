from django.conf.urls import patterns,url

from polls import views
from django.contrib import admin
admin.autodiscover()
import polls.views

urlpatterns = [
    url(r'^$', polls.views.index, name='index'),
            url(r'^tiposDeServicios/$',polls.views.servicios, name='tiposDeServicios'),
                url(r'^registro/$',polls.views.register, name='registro'),
                   url(r'^registro_exitoso/$',polls.views.registroExitoso, name='registro_exitoso'),
                        url(r'^login/$',polls.views.login, name='login'),
                             url(r'^auth/$',polls.views.auth_view),
                             url(r'^logout/$',polls.views.logout),

]