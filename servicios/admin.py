from django.contrib import admin
from servicios.models import Servicio, TipoServicio

class TipoServicioAdmin(admin.ModelAdmin):
    pass

class ServicioAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipoServicio, TipoServicioAdmin)
admin.site.register(Servicio, ServicioAdmin)
