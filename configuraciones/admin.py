from django.contrib import admin
from django.utils.encoding import force_unicode
from django.http import HttpResponseRedirect
from django.utils.functional import update_wrapper

from configuraciones.models import Configuracion

class SingletonModelAdmin(admin.ModelAdmin):

    change_form_template = "configuraciones/change_form.html"
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = False
    save_on_top = False
  
    def change_view(self, request, object_id, extra_context=None):
        if object_id=='1':
            self.model.objects.get_or_create(pk=1)
        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context,
        )

admin.site.register(Configuracion, SingletonModelAdmin)
