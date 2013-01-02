from django.conf.urls import url, patterns

urlpatterns = patterns('',
    (r'^registro/$', 'clientes.views.registro_nuevo_cliente'),
)