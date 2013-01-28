from django.db import models
from django.db import DatabaseError
from django.db.models import Sum
from django.core.exceptions import ValidationError

from clientes.models import Cliente

from servicios.managers import DetallesDeOrdenActivas

TALLAS = (
    (1,'Pequeno'),
    (2,'Juvenil'),
    (3,'Grande')
)

PRIORIDAD_EJECUCION = (
    (1, 'Primero en Ejecutar'),
    (2, 'Segundo en Ejecutar'),
    (3, 'Tercero en Ejecutar'),
    (4, 'Cuarto en Ejecutar'),
)

class TipoServicio(models.Model):
    nombre = models.CharField('Nombre', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    capacidad = models.PositiveIntegerField('Capacidad', help_text='Capacidad en numero de piezas por dia.')
    prioridad = models.IntegerField('Prioridad de ejecucion', choices = PRIORIDAD_EJECUCION)

    class Meta:
        verbose_name = 'Tipo de Servicios'
        verbose_name_plural = 'Tipo de Servicios'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre

class Servicio(models.Model):
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre = models.CharField('Nombre', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    
    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'
        ordering = ['tipo_servicio','nombre']

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

    def get_precio_bolivianos(self):
        if self.precio_bolivianos > 0.00:
            return self.precio_bolivianos
        #TODO convertir a dolares return self.

    def _unicode__(self):
        return '%s %s' % (self.servicio.nombre, self.tamano)

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente)
    cantidad = models.PositiveIntegerField('Cantidad de prendas')
    talla = models.IntegerField('Tallas de la Prenda',choices=TALLAS)
    fecha_entrega = models.DateField('Fecha de Entrega', null=True, blank=True, help_text='Fecha que se desea que la empresa inicie el proceso con sus prendas.')
    fecha_registro = models.DateTimeField('Fecha de Registro',auto_now=True, editable=False)
    observaciones = models.TextField(verbose_name='Observaciones:', max_length=250, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['fecha_registro','cliente']
        get_latest_by = 'fecha_registro'
        
    def __unicode__(self):
        return 'Codigo de orden: %s' % self.pk
    
    def get_detalle(self):
        return self.detalleorden_set.all()
    
    def get_lista_servicios(self):
        servicios = []
        for detalle in self.detalleorden_set.all():
            servicios.append(detalle.servicio)
        return servicios
    
class DetalleOrden(models.Model):
    PRIORIDAD = (
        (4,'Muy Alta Prioridad'),
        (3,'Alta Prioridad'),
        (2,'Prioridad Normal'),
        (1,'Prioridad Baja'),
        (0,'Sin Prioridad'),
    )
    orden = models.ForeignKey(Orden)
    servicio = models.ForeignKey(Servicio)
    prioridad = models.PositiveIntegerField('Pioridad para ejecutar el servicio', choices=PRIORIDAD, default=2)
    fecha_ejecucion = models.DateField('Fecha Ejecucion', null=True, blank=True, help_text='La fecha que se ejecutara el servicio en la empresa')
    terminado = models.BooleanField('Servicio Terminado', default = False)

    objects = models.Manager()
    noterminados = DetallesDeOrdenActivas()
    
    class Meta:
        verbose_name = 'Detalle de Orden'
        verbose_name_plural = 'Detalle de Ordenes'
        ordering = ['fecha_ejecucion','orden', 'servicio']
    
    def cantidad(self):
        return self.orden.cantidad
    
    def verificar_espacio(self):
        self.noterminados.por_tipo_fecha_ejecucion(tipo_servicio=self.servicio.tipo_servicio, fecha_ejecucion=self.fecha_ejecucion)        

    def save(self, *args, **kwargs):
        #self.fecha_ejecucion = detalle_pre_save(self)
        #kwargs['fecha_ejecucion'] = detalle_pre_save(self, created=created, **kwargs)
        super(DetalleOrden, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Orden %s servicio %s' % (self.orden.pk, self.servicio.pk)

from django.db.models.signals import pre_save

def detalle_pre_save(instance):
    if not instance.pk:
        disponible = Disponibilidad.objects.filter(disponible__gte=instance.orden.cantidad, fecha_ejecucion__gte=instance.fecha_ejecucion)
        if len(disponible):
            return disponible[0].fecha_ejecucion
        return instance.fecha_ejecucion

#pre_save.connect(detalle_pre_save, sender=DetalleOrden, weak=True)