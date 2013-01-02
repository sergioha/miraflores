from django.test import TestCase
from clientes.models import Cliente

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

    def setUp(self):
        """
        Inicializaremos los datos de cuentas de usuarios con rol de
        administrador y cuentas de usuario del tipo
        cliente que seran usadas en los tests.
        """
        

    def test_crear_nueva_cuenta_cliente(self):
        """
        """
        self.cliente_1 = self._crear_cuenta_cliente(self.ci_1, self.password)
        self.assertEqual(self.cliente_1, Cliente.objects.get(ci = self.cliente_1.ci))
    
    def test_verificar_contrasena(self):
        self.cliente_1 = self._crear_cuenta_cliente(self.ci_1, self.password)
        self.assertTrue(self.cliente_1.verificar_contrasena('123456'))