from django.contrib import admin
from django.contrib.auth.models import User

from clientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo','ciudad', 'activo', 'fecha_registro', 'fecha_ultimo_acceso',)
    list_filter = ('tipo_empresa',)
    #search_fields = ('user',)
    #ordering = ['']
    #list_editable = ('prioridad',)

admin.site.register(Cliente, ClienteAdmin)