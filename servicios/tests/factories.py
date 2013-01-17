import random
import factory

from django.utils import timezone

from servicios.models import *
from clientes.tests.factories import ClienteFactory

CAPACIDAD = 500

class TipoServicioFactory(factory.Factory):
    FACTORY_FOR = TipoServicio
    nombre = factory.Sequence(lambda n: 'Tipo de Servicio {0}'.format(n))
    capacidad = factory.Sequence(lambda n: 3*n)
    
class ServicioFactory(factory.Factory):
    FACTORY_FOR = Servicio
    tipo_servicio = factory.SubFactory(TipoServicioFactory)
    nombre = factory.Sequence(lambda n: 'Servicio{0}'.format(n))
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        lista = kwargs.pop('lista',None)
        servicio = super(ServicioFactory, cls)._prepare(create, **kwargs)
        if lista:
            ListaPreciosFactory(servicio=servicio, talla=1)
            ListaPreciosFactory(servicio=servicio, talla=2)
            ListaPreciosFactory(servicio=servicio, talla=3)
        return servicio
    
class ListaPreciosFactory(factory.Factory):
    FACTORY_FOR = ListaPrecios
    servicio = factory.SubFactory(ServicioFactory)
    talla =  random.randint(1,3)
    precio_bolivianos = round(random.uniform(0,2),2)
    
contador = 0

class OrdenFactory(factory.Factory):
    FACTORY_FOR = Orden
    cliente = factory.SubFactory(ClienteFactory)
    fecha_entrega = timezone.now()
    cantidad = random.randint(100,CAPACIDAD)
    talla = random.randint(1,TALLAS.__len__()-1)
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        detalle = kwargs.pop('detalle',None)
        orden = super(OrdenFactory, cls)._prepare(create, **kwargs)
        if detalle:
            DetalleOrdenFactory(orden=orden)
            DetalleOrdenFactory(orden=orden)
            DetalleOrdenFactory(orden=orden)
        global contador
        contador = 0
        return orden

class DetalleOrdenFactory(factory.Factory):
    FACTORY_FOR = DetalleOrden
    orden = factory.SubFactory(OrdenFactory)
    fecha_ejecucion = timezone.now()
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        global contador
        if 'servicio' in kwargs:
            detalleorden = super(DetalleOrdenFactory, cls)._prepare(create, **kwargs)
            return detalleorden
        servicio = Servicio.objects.all()[contador]
        contador+=1
        kwargs['servicio'] = servicio
        detalleorden = super(DetalleOrdenFactory, cls)._prepare(create, **kwargs)
        return detalleorden