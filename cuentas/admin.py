from django.contrib import admin
from cuentas.models import Cliente
from django.contrib.auth.models import User

class ClienteUsuarioInline(admin.TabularInline):
    model = Cliente

class ClienteAdmin(admin.ModelAdmin):
    #inlines = [ ClienteUsuarioInline,]
    date_hierarchy = 'ultima_actividad'
    #fieldsets = (
    #        ('Datos Personales'

admin.site.register(Cliente, ClienteAdmin)
