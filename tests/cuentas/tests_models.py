from django.test import TestCase
from django.contrib.auth.models import User
from cuentas.models import *

class CuentaClienteNuevoTestCase(TestCase):
    
    def setUp(self):
        """
        Inicializaremos los datos de cuentas de usuarios con rol de
        administrador y cuentas de usuario del tipo
        cliente que seran usadas en los tests.
        """
        self.user_info_1 = {'nombre': 'julio',
                'apellidos': 'medrano',
                'direccion': 'lorem ipsum asimet duo',
                'ciudad': 'Cochabamba',
                'telefono': '4414444',
                'celular': '77777777',
                'tipo_empresa': 'Unipersonal',
                'servicio_requerido': '1',
                'servicio_preferencia': '1',}
        self.email_1 = 'julio@lavanderiamiraflores.com'
        self.user_info_2 = {'username': 'sergio',
                       'password': '123456',
                       'email': 'sergio@lavanderiamiraflores.com'}
        self.user_info_3 = {'username': 'ronald',
                       'password': '123456',
                       'email': 'ronald@lavanderiamiraflores.com'}
        self.user_info_admin = {'username': 'admin',
                           'password': '123456',
                           'email': 'admin@lavanderiamiraflores.com'}
        self.admin = User.objects.create_user(**self.user_info_admin)
        self.admin.save()

    def test_crear_nuevo_cliente(self):
        """
        """
        self.cliente_1 = Cliente.objects.create_user(email = self.email_1, password = '123456', **self.user_info_1)
        self.assertEqual(self.cliente_1.usuario_cliente, Cliente.objects.get(usuario__username = self.email_1))

