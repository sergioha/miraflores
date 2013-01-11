from django.contrib import admin
from servicios.models import *

class TipoServicioAdmin(admin.ModelAdmin):
    pass

class ServicioAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoServicio, TipoServicioAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(ListaPrecios)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
admin.site.register(Cronograma)
