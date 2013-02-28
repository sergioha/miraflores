from django.contrib import sessions

from configuraciones.models import Configuracion

class ConfiguracionMiddleware(object):

    def process_request(self, request):
        if request.path in ['/zonacliente/']:
            try:
                configuracion = Configuracion.objects.get(pk=1)
            except Configuracion.DoesNotExist:
                tipo_cambio = None
            tipo_cambio = configuracion.tipo_cambio
            request.session['tipo_cambio'] = tipo_cambio