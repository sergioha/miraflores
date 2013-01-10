import factory

from clientes.models import Cliente

class ClienteFactory(factory.Factory):
    FACTORY_FOR = Cliente
    ci = factory.Sequence(lambda n: '5{0}'.format(n))
    nombres = factory.Sequence(lambda n: 'Cliente{0}'.format(n))
    apellidos = factory.Sequence(lambda n: 'Apellido{0}'.format(n))
    email = factory.Sequence(lambda n: 'clienteid{0}@gmail.com'.format(n))
    celular = 76971003
    direccion = 'lorem ipsum asimet duo'
    ciudad = 'COCHABAMBA'
    tipo_empresa = 'SA'
    is_active = True
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        cliente = super(ClienteFactory, cls)._prepare(create, **kwargs)
        if password:
            cliente.set_password(password)
            if create:
                cliente.save()
        return cliente