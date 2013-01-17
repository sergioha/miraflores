from django.conf.urls import url, patterns
from django.views.generic.simple import direct_to_template

from clientes.views import cliente_login, registro_nuevo_cliente

urlpatterns = patterns('',
    url(r'^registro/$', registro_nuevo_cliente, name='registro'),
    url(r'^ingresar/$', cliente_login, name='login'),
    url(r'^registro/completado/$', direct_to_template,
        {'template': 'clientes/registro_completado.html'},
        name='registro_completado'),
)