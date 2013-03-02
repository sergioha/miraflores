from django.db import models

class Configuracion(models.Model):
    tipo_cambio = models.FloatField('Tipo de Cambio a $us')

    class Meta:
        verbose_name = 'Configuraciones del Sistema'
        verbose_name_plural = 'Configuraciones del Sistema'

    def __unicode__(self):
        return '%s' % self.pk

    def save(self, *args, **kwargs):
        self.pk=1
        super(Configuracion, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass