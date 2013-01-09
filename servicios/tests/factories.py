import factory
from servicios.models import TipoServicio, Servicio

class TipoServicioFactory(factory.Factory):
    FACTORY_FOR = TipoServicio
    titulo = factory.Sequence(lambda n: 'Tipo de Servicio {0}'.format(n))
    capacidad = factory.Sequence(lambda n: 3*n)
    
class ServicioFactory(factory.Factory):
    FACTORY_FOR = Servicio
    tipo_servicio = factory.SubFactory(TipoServicioFactory)
    