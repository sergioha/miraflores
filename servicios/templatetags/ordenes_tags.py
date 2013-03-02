from django import template

from servicios.models import Orden, Servicio
from servicios.forms import CotizarForm

register = template.Library()

@register.inclusion_tag('servicios/ordenes.html')
def listar_ordenes(cliente):
    ordenes = cliente.ordenes
    return {'ordenes': ordenes}

@register.inclusion_tag('servicios/cotizar.html')
def cotizar():
    queryset = Servicio.objects.all()
    form = CotizarForm(queryset=queryset)
    return {'form': form}