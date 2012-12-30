from django.test import TestCase
from clientes.models import Cliente

class CuentaClienteNuevoTestCase(TestCase):
    
    def create_client(**kwargs):
        defaults = {
        "likes_cheese": True,
        "age": 32,
        "address": "3815 Brookside Dr",
        }
        defaults.update(kwargs)
        if "user" not in defaults:
            defaults["user"] = create_user()
        return Profile.objects.create(**defaults)

    def setUp(self):
        """
        Inicializaremos los datos de cuentas de usuarios con rol de
        administrador y cuentas de usuario del tipo
        cliente que seran usadas en los tests.
        """
        self.user_info_1 = {
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
        self.ci_1 = '2121542'
        self.email_1 = 'julio@lavanderiamiraflores.com'
        self.nombres_1 ='julio'
        self.apellidos_1 = 'medrano'
        self.telefono_1 = 4414444
        self.user_info_2 = {'username': 'sergio',
                       'password': '123456',
                       'email': 'sergio@lavanderiamiraflores.com'}
        self.user_info_3 = {'username': 'ronald',
                       'password': '123456',
                       'email': 'ronald@lavanderiamiraflores.com'}

    def test_crear_nuevo_cliente(self):
        """
        """
        self.cliente_1 = Cliente.objects.create_user(self.ci_1, self.email_1, self.nombres_1, self.apellidos_1, self.telefono_1, password = '123456', **self.user_info_1)
        self.assertEqual(self.cliente_1, Cliente.objects.get(ci = self.cliente_1.ci))
    
    def test_verificar_contrasena(self):
        self.cliente_1 = Cliente.objects.create_user(self.ci_1, self.email_1, self.nombres_1, self.apellidos_1, self.telefono_1, password = '123456', **self.user_info_1)
        self.assertTrue(self.cliente_1.verificar_contrasena('123456'))

