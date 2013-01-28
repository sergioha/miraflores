from django.db import models

from servicios.models import Orden, TipoServicio, Servicio, TALLAS
from clientes.models import Cliente

class Cronograma(models.Model):
    user = models.ForeignKey(Cliente)
    orden = models.ForeignKey(Orden)
    cantidad = models.PositiveIntegerField('Cantidad')
    talla = models.IntegerField('Talla',choices=TALLAS)
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre_tiposervicio = models.CharField('Nombre', max_length=35)
    servicio = models.ForeignKey(Servicio)
    nombre_servicio = models.CharField('Nombre', max_length=35)
    fecha_ejecucion = models.DateField('Fecha Ejecucion',help_text='La fecha que se ejecutara el servicio en la empresa')
    terminado = models.BooleanField('Terminado', default = False)
    
    def __unicode__(self):
        return 'orden:%s servicio:%s fecha ejecucion:%s' % (self.orden, self.nombre_servicio, self.fecha_ejecucion)
    
    class Meta:
        verbose_name = 'Cronograma de Ordenes'
        verbose_name_plural = 'Cronograma de Ordenes'
        db_table = 'servicios_cronograma'
        managed = False
        ordering = ['fecha_ejecucion','tipo_servicio']
        

class Disponibilidad(models.Model):
    tipo_servicio = models.ForeignKey(TipoServicio, primary_key=True)
    capacidad = models.IntegerField('Capacidad')
    ocupado = models.IntegerField('Ocupado')
    disponible = models.IntegerField('Disponible')
    fecha_ejecucion = models.DateField('Fecha Ejecucion')
    
    class Meta:
        verbose_name = 'Fechas Disponibles'
        verbose_name_plural = 'Fechas Disponibles'
        db_table = 'servicios_disponibilidad'
        managed = False
        ordering = ['fecha_ejecucion','tipo_servicio']

class Retrasos(models.Model):
    user = models.ForeignKey(Cliente)
    orden = models.ForeignKey(Orden)
    cantidad = models.PositiveIntegerField('Cantidad')
    talla = models.IntegerField('Talla',choices=TALLAS)
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre_tiposervicio = models.CharField('Nombre', max_length=35)
    servicio = models.ForeignKey(Servicio)
    nombre_servicio = models.CharField('Nombre', max_length=35)
    fecha_ejecucion = models.DateField('Fecha Ejecucion', help_text='La fecha que se ejecutara el servicio en la empresa')
    terminado = models.BooleanField('Terminado', default = False)
    
    def __unicode__(self):
        return 'orden:%s servicio:%s fecha ejecucion:%s' % (self.orden, self.nombre_servicio, self.fecha_ejecucion)
    
    class Meta:
        verbose_name = 'Ordenes Retrasados'
        verbose_name_plural = 'Ordenes Retrasados'
        db_table = 'servicios_retrasados'
        managed = False
        ordering = ['fecha_ejecucion','tipo_servicio']

class SinFechaEjecucion(models.Model):
    user = models.ForeignKey(Cliente)
    orden = models.ForeignKey(Orden)
    cantidad = models.PositiveIntegerField('Cantidad')
    talla = models.IntegerField('Talla',choices=TALLAS)
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre_tiposervicio = models.CharField('Nombre', max_length=35)
    servicio = models.ForeignKey(Servicio)
    nombre_servicio = models.CharField('Nombre', max_length=35)
    fecha_ejecucion = models.DateField('Fecha Ejecucion', help_text='La fecha que se ejecutara el servicio en la empresa')
    terminado = models.BooleanField('Terminado', default = False)
    
    def __unicode__(self):
        return 'orden:%s servicio:%s fecha ejecucion:%s' % (self.orden, self.nombre_servicio, self.fecha_ejecucion)
    
    class Meta:
        verbose_name = 'Ordenes sin Fecha de Ejecucion'
        verbose_name_plural = 'Ordenes sin Fecha de Ejecucion'
        db_table = 'servicios_sinfechaejecucion'
        managed = False
        ordering = ['fecha_ejecucion','tipo_servicio']
