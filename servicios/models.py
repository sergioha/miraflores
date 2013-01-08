from django.db import models

class TipoServicio(models.Model):
    titulo = models.CharField('Titulo', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    
    def __unicode__(self):
        return self.titulo

class Servicio(models.Model):
    tipo_servicio = models.ForeignKey(TipoServicio)
    nombre = models.CharField('nombre', max_length=35, unique=True)
    descripcion = models.TextField('Descripcion')
    precio_bs = models.DecimalField('Precio x unidad en Bs', max_digits=5, decimal_places=2)
    precio_dolares = models.DecimalField('Precio x unidad en $us', max_digits=5, decimal_places=2, default = 0.00)
    
    def __unicode__(self):
        return self.nombre