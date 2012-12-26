from django.test import TestCase
from django.contrib.auth.models import User

class CuentaClienteNuevoTestCase(TestCase):
    
    def setUp(self):
        """
        Inicializaremos los datos de cuentas de usuarios con rol de
        administrador y cuentas de usuario del tipo
        cliente que seran usadas en los tests.
        """
        self.user_info_1 = {'username': 'julio',
                       'password': '123456',
                       'email': 'julio@lavanderiamiraflores.com'}
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
        self.assertEqual(self.admin, User.objects.get(username='admin'))

