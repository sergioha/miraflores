from django.db import models

class DetallesDeOrdenActivas(models.Manager):

    def get_query_set(self):
        return super(DetallesDeOrdenActivas, self).get_query_set().filter(terminado=False)

    def por_tipo_fecha_ejecucion(self, tipo_servicio = None, fecha_ejecucion=None):
        return self.filter(servicio__tipo_servicio=tipo_servicio, fecha_ejecucion=fecha_ejecucion)
    
    def por_fecha_ejecucion(self, fecha=None):
        return self.filter(fecha_ejecucion=fecha)
    
    #def get_capacidad(self, fecha_ejecucion, tipo_servicio):
        #self.filter()
        #from django.db import connection, transaction
        #from django.utils.encoding import smart_unicode
        #import datetime
        #cursor = connection.cursor()
        #cursor.execute("select * from capacidad_en_fecha(%s, %s)",[datetime.date(2013,10,1), tipo_servicio.pk])
        #row = cursor.fetchone()
        #return row
        #self.aggregate()    