from django.conf.urls import url, patterns
from django.views.generic.simple import direct_to_template

from servicios.views import registrar_orden, listar_ordenes, detalle_orden, cotizar

urlpatterns = patterns('',
    url(r'^cotizar/$', cotizar , name='cotizar'),                   
    url(r'^registrar/$', registrar_orden , name='registrar_orden'),
    url(r'^$', listar_ordenes, name='listar_ordenes'),
    url(r'^(?P<pk>\d+)/$', detalle_orden, name='detalle_orden'),
)