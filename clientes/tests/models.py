from django.test import TestCase

from clientes.models import Cliente
from clientes.tests.factories import ClienteFactory


class ClienteTestCase(TestCase):
    
    cliente = None
    
    def setUp(self):
        self.cliente = ClienteFactory(password='123456')
        
    def test_crear_nueva_cuenta_cliente(self):
        self.assertEqual(self.cliente, Cliente.objects.get(ci = self.cliente.ci))
    
    def test_verificar_contrasena(self):
        self.assertTrue(self.cliente.verificar_contrasena('123456'))