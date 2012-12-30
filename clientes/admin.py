from django.contrib import admin
from clientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)