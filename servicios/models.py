from django.db import models
from django.db import DatabaseError
from django.core.exceptions import ValidationError

from clientes.models import Cliente

TALLAS = (
    (1,'Pequeno'),
    (2,'Juvenil'),
    (3,'Grande')
)

class TipoServicio(models.Model):
    titulo = models.CharField('Titulo', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    capacidad = models.PositiveIntegerField('Capacidad', help_text='Capacidad en numero de piezas por dia.')
    
    def __unicode__(self):
        return self.titulo

class Servicio(models.Model):
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre = models.CharField('nombre', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    
    def __unicode__(self):
        return self.nombre
    
    def get_precio_dolares(self, talla, tipo_cambio):
        try:
            listaprecio = self.listaprecios_set.get(servicio__id=self.id, talla=talla)
        except DatabaseError:
            return ValidationError(u'No se tiene registro del precio del servicio %s en talla %s' % (self.nombre, talla))
        if listaprecio.precio_dolares > 0.00:
            return round(float(listaprecio.precio_dolares),2)
        return round(float(listaprecio.precio_bolivianos)/tipo_cambio,2)

    def get_precio_bolivianos(self, talla, tipo_cambio):
        try:
            listaprecio = self.listaprecios_set.get(servicio__id=self.id, talla=talla)
        except DatabaseError:
            return ValidationError(u'No se tiene registro del precio del servicio %s en talla %s' % (self.nombre, talla))
        if listaprecio.precio_bolivianos > 0.0:
            return round(float(listaprecio.precio_bolivianos),2)
        return round(float(listaprecio.precio_dolares)*tipo_cambio,2)

class ListaPrecios(models.Model):
    servicio = models.ForeignKey(Servicio)
    talla = models.IntegerField('Tallas de la Prenda',choices=TALLAS)
    precio_bolivianos = models.DecimalField('Precio x unidad en Bs', max_digits=5, decimal_places=2, default=0.00)
    precio_dolares = models.DecimalField('Precio x unidad en $us', max_digits=5, decimal_places=2, default = 0.00)
    
    class Meta:
        unique_together =(('servicio'),('talla'),)
        verbose_name = 'Lista de Precios de Servicios'
        verbose_name_plural = 'Lista de Precios de Servicios'
        ordering = ['servicio','talla']

    def _unicode__(self):
        return '%s %s' % (self.servicio.nombre, self.tamano)

#class OrdenPedido(models.Model):
    #cliente = models.ForeignKey(Cliente)
    #servicios = models.ManyToManyField(trough=Cronograma)
    #fecha_registro = models.DateTimeField('Fecha de Registro',auto_now=True, editable=False)
    #cantidad = models.PositiveIntegerField('Cantidad de prendas')
    
#class Cronograma(models.Model):
    #pass