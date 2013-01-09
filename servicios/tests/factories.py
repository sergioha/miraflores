import random
import factory
from servicios.models import TipoServicio, Servicio, ListaPrecios, TALLAS

class TipoServicioFactory(factory.Factory):
    FACTORY_FOR = TipoServicio
    titulo = factory.Sequence(lambda n: 'Tipo de Servicio {0}'.format(n))
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
    
    
    
    