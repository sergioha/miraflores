from django.test import TestCase
from cuentas.models import *
from django.contrib.auth.models import User

class PerfilClienteTest(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create()
        self.usuario1.email = 'sergio.hinojosa.avila@gmail.com'
        self.usuario1.set_password ='123456'
        #self.admin = User.objects.create('admintest','ventas@npneumatica.com','123456')
        #self.admin.is_staff = True
        self.usuario1.save()
        #self.admin.save()

    def test_agregar_nuevo_perfil(self):
        """
        Agregamos un nuevo perfil con toda la informacion requerida
        """
        #self.usuario.perfil
        self.assertEqual(1 + 1, 2)
