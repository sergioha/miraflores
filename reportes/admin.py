from django.contrib import admin
from reportes.models import Cronograma, Disponibilidad, Retrasos, SinFechaEjecucion

class CronogramaAdmin(admin.ModelAdmin):
    fields = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    list_display = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    list_display_links = ('user', 'orden', 'servicio',)
    list_filter = ('fecha_ejecucion', 'user', 'tipo_servicio', 'servicio', 'terminado',)
    readonly_fields = ('user', 'orden', 'cantidad', 'talla', 'tipo_servicio', 'servicio', 'fecha_ejecucion', 'terminado',)
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = False
    save_on_top = False
    change_form_template = 'admin/cronograma_form.html'
    
    def has_add_permission(self, request):
        return False

class RetrasosAdmin(admin.ModelAdmin):
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

class SinFechaEjecucionAdmin(admin.ModelAdmin):
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
    
admin.site.register(Cronograma, CronogramaAdmin)
admin.site.register(Disponibilidad, DisponibilidadAdmin)
admin.site.register(Retrasos, RetrasosAdmin)
admin.site.register(SinFechaEjecucion, SinFechaEjecucionAdmin)