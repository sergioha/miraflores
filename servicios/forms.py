from django import forms
from django.utils import timezone

from datetime import datetime

from servicios.models import TALLAS, Servicio, Orden

class OrdenForm(forms.Form):
    cantidad = forms.IntegerField('# de Piezas', min_value=1)
    talla = forms.ChoiceField(choices=TALLAS, required=True, label='Seleccione la Talla', help_text='Si su talla es especial por favor ingrese sus observaciones.')
    fecha_entrega = forms.CharField(max_length=10, min_length=10)
    observaciones = forms.CharField(widget=forms.Textarea)

    def clean_fecha_entrega(self):
        datos = self.cleaned_data['fecha_entrega'].split('/')
        if len(datos) == 3:
            fecha = timezone.datetime(int(datos[2]), int(datos[1]), int(datos[0]), tzinfo=None)
            hoy  = timezone.now()
        else:
            raise forms.ValidationError("La fecha no tiene el formato correcto!")
        if fecha < timezone.datetime(hoy.year, hoy.month, hoy.day):
            raise forms.ValidationError("La fecha no puede ser pasada!")
        return fecha

    def __init__(self, queryset=None, *args, **kwargs):
        super(OrdenForm, self).__init__(*args, **kwargs)
        if queryset:
            self.fields['servicios'] = forms.ModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())

class CotizarForm(forms.Form):
    cantidad = forms.IntegerField('# de Piezas', min_value=1)
    talla = forms.ChoiceField(choices=TALLAS, required=True, label='Seleccione la Talla')
    
    def __init__(self, queryset=None, *args, **kwargs):
        super(CotizarForm, self).__init__(*args, **kwargs)
        if queryset:
            self.fields['servicios'] = forms.ModelMultipleChoiceField(queryset=queryset, widget=forms.CheckboxSelectMultiple())
