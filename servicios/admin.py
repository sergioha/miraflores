from django.contrib import admin
from servicios.models import *

class TipoServicioAdmin(admin.ModelAdmin):
    fields = ('nombre', 'capacidad', 'descripcion', 'prioridad',)
    list_display = ('nombre', 'capacidad',)
    ordering = ['prioridad']

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo_servicio',)
    list_filter = ('tipo_servicio',)
    search_fields = ('nombre',)
    ordering = ['tipo_servicio']

class ListaPreciosAdmin(admin.ModelAdmin):
    list_display = ('servicio','talla', 'precio_bolivianos', 'precio_dolares',)
    list_filter = ('servicio',)
    search_fields = ('servicio',)
    list_editable = ('precio_bolivianos', 'precio_dolares',)

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cantidad', 'talla', 'fecha_registro', 'fecha_entrega',)
    list_filter = ('cliente', 'fecha_registro', 'fecha_entrega',)
    search_fields = ('cliente',)

class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'servicio', 'fecha_ejecucion', 'prioridad', 'terminado',)
    list_filter = ('fecha_ejecucion', 'orden', 'terminado',)
    search_fields = ('servicio',)
    list_editable = ('prioridad',)

class CronogramaAdmin(admin.ModelAdmin):
    fields = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    list_display = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    list_displa_links = ('user', 'orden', 'servicio',)
    list_filter = ('fecha_ejecucion', 'user', 'tipo_servicio', 'servicio', 'terminado',)
    readonly_fields = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = False
    save_on_top = False
    change_form_template = 'admin/cronograma_form.html'
    
    def has_add_permission(self, request):
        return False

class DisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('tipo_servicio', 'capacidad', 'ocupado', 'disponible', 'fecha_ejecucion')
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = False
    save_on_top = False

    def has_add_permission(self, request):
        return False
    
admin.site.register(TipoServicio, TipoServicioAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(ListaPrecios, ListaPreciosAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(DetalleOrden, DetalleOrdenAdmin)
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(Disponibilidad, DisponibilidadAdmin)
