from django.test import TestCase
from servicios.models import TipoServicio, Servicio
from servicios.tests.factories import TipoServicioFactory, ServicioFactory
from django.db import DatabaseError

class ServiciosTestCase(TestCase):
    
    contador_tipos = 0
    tipo_servicio = None
    
    def setUp(self):
        self.tipo_servicio = TipoServicioFactory()
        self.contador_tipos+=1
    
    def test_crear_nuevo_tipo_servicio(self):
        tipo_servicio_1 = TipoServicioFactory()
        tipos = TipoServicio.objects.all()
        print 'Verifica que el numero de tipo de servicios creados este correcto'
        self.assertEqual(len(tipos),self.contador_tipos+1)#verificamos el nuevo registro contando
        print 'Verifica que el tipo de servicios creado se encuentre almacenado en la base de datos'
        self.assertIn(tipo_servicio_1, tipos, msg="El tipo de servicio no fue creado")
   
    def test_tipo_servicio_titulo_no_valido(self):
        print 'Verifica que nos lanze un error en la base de datos al crear un tipo de servicio con un titulo ya existente.'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(titulo=self.tipo_servicio.titulo)

    def test_tipo_servicio_capacidad_no_valida(self):
        print 'Verifica que nos lanze un error en la base de datos al ingresar una capacidad grande'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(capacidad=3333333333333333333333333333333333333333)
        print 'Verifica que nos lanze un error en la base de datos al ingresar una capacidad con valor negativo'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(capacidad=-300)

    def test_crear_nuevo_servicio(self):
        servicio = ServicioFactory(nombre = 'stoneado', precio_bs = 1)
        self.assertEqual(len(Servicio.objects.all()),1)

if __name__ == "__main__":
    import unittest2 as unittest
    unittest.main()