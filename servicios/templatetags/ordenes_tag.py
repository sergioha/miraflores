from django import template

from servicios.models import Orden

register = template.Library()

@register.inclusion_tag('servicios/ordenes.html')
def listar_ordenes(cliente):
    ordenes = cliente.ordenes
    return {'ordenes': ordenes}

