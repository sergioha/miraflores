from django.test import TestCase
from clientes.models import Cliente

class CuentaClienteNuevoTestCase(TestCase):
    
    def setUp(self):
        """
        Inicializaremos los datos de cuentas de usuarios con rol de
        administrador y cuentas de usuario del tipo
        cliente que seran usadas en los tests.
        """
        self.user_info_1 = {'ci':'2121542',
                'contrasena' : '123456',
                'nombres': 'julio',
                'apellidos': 'medrano',
                'email' : 'julio@lavanderiamiraflores.com',
                'telefono': '4414444',
                'celular': '77777777',
                'direccion': 'lorem ipsum asimet duo',
                'ciudad': 'Cochabamba',
                'nombre_empresa' : 'las lomas',
                'tipo_empresa': 'Unipersonal',
                'numero_empleados' : 10,
                'productos' :'chamarras, jeans',
                'produccion' :1000,
                'servicio_requerido': '1',
                'servicio_preferencia': '1',}
        self.user_info_2 = {'username': 'sergio',
                       'password': '123456',
                       'email': 'sergio@lavanderiamiraflores.com'}
        self.user_info_3 = {'username': 'ronald',
                       'password': '123456',
                       'email': 'ronald@lavanderiamiraflores.com'}

    def test_crear_nuevo_cliente(self):
        """
        """
        self.cliente_1 = Cliente.objects.create(**self.user_info_1)
        self.assertEqual(self.cliente_1, Cliente.objects.get(ci = self.cliente_1.ci))

