#encoding=utf-8
from django.test import TestCase
from clientes.models import Cliente
from servicios.models import TipoServicio, Servicio

class ClienteTestCase(TestCase):
    
    ci_1 = '2121542'
    password = '132465'
    
    def _crear_cuenta_cliente(self, ci, password, **kwargs):
        defaults = {
            'nombres' : 'julio',
            'apellidos' : 'medrano',
            'email' : 'julio@lavanderiamiraflores.com',
            'telefono' : '4414444',
            'celular': '77777777',
            'direccion': 'lorem ipsum asimet duo',
            'ciudad': 'Cochabamba',
            'nombre_empresa' : 'las lomas',
            'tipo_empresa': 'Unipersonal',
            'numero_empleados' : 10,
            'productos' :'chamarras, jeans',
            'produccion' :1000,
            'servicio_requerido': '1',
            'servicio_preferencia': '1',
        }
        defaults.update(kwargs)
        #if "user" not in defaults:
        #    defaults["user"] = create_user()
        #return Profile.objects.create(**defaults)
        return Cliente.objects.create_user(ci, password, **defaults)

    def test_crear_nueva_cuenta_cliente(self):
        """
        """
        self.cliente_1 = self._crear_cuenta_cliente(self.ci_1, self.password)
        self.assertEqual(self.cliente_1, Cliente.objects.get(ci = self.cliente_1.ci))
    
    def test_verificar_contrasena(self):
        self.cliente_1 = self._crear_cuenta_cliente(self.ci_1, self.password)
        self.assertTrue(self.cliente_1.verificar_contrasena('123456'))

class ServiciosTestCase(TestCase):
    
    contador_tipos = 0
    tipo_servicio = None
    
    def setUp(self):
        self.tipo_servicio = TipoServicio()
        self.tipo_servicio.titulo='Pre Lavado'
        self.tipo_servicio.descripcion = 'El prelavado de jeans se realiza en todos los servicios es la primera etapa'
        self.tipo_servicio.save()
        self.contador_tipos+=1
    
    def test_crear_nuevo_tipo_de_servicio(self):
        tipo_servicio_1 = TipoServicio()
        tipo_servicio_1.titulo='Efectos'
        tipo_servicio_1.descripcion = 'Los efectos se realiza despues del Pre lavado'
        tipo_servicio_1.save()
        tipos = TipoServicio.objects.all()
        self.assertEqual(len(tipos),self.contador_tipos+1)#verificamos el nuevo registro contando
        self.assertIn(tipo_servicio_1, tipos, msg="El tipo de servicio no fue creado")

    def test_crear_nuevo_servicio(self):
        servicio = Servicio(tipo_servicio = self.tipo_servicio,
                            nombre = 'stoneado',
                            descripcion = 'lorem ipsum asimet duo',
                            precio_bs = 1)
        servicio.save()
        self.assertEqual(len(Servicio.objects.all()),1)

if __name__ == "__main__":
    unittest.main()