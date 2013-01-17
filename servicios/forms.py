from django import forms
from servicios.models import TALLAS

class OrdenForms(forms.BaseForm):
    cantidad = forms.IntegerField(min_value=1)
    talla = forms.ChoiceField(choices=TALLAS, required=True, label='Seleccione la Talla', help_text='Si su talla es especial por favor ingrese sus observaciones.')
    fecha_entrega = forms.DateField()
    observaciones = forms.Textarea()