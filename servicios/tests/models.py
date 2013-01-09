from django.utils import timezone
from django.test import TestCase
from servicios.models import TipoServicio, Servicio, ListaPrecios, TALLAS
from servicios.tests.factories import TipoServicioFactory, ServicioFactory, ListaPreciosFactory
from django.db import DatabaseError

class ServiciosTestSuite(TestCase):
    
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
            TipoServicioFactory(capacidad=3333333*33333)
        print 'Verifica que nos lanze un error en la base de datos al ingresar una capacidad con valor negativo'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(capacidad=-300)

    def test_crear_nuevo_servicio(self):
        print 'Verifica la creacion correcta de un servicio'
        servicio = ServicioFactory(nombre = 'estoneado')
        self.assertEqual(len(Servicio.objects.all()),1)
        print 'Verifica que no se cree un servicio con el nombre repetido'
        with self.assertRaises(DatabaseError):
            ServicioFactory(nombre='estoneado')

class OrdenesDePedidoTestSuite(TestCase):
    
    capacidad_lavado = 200
    servicio_estoneado_build = None
    
    def setUp(self):
        self.servicio_estoneado = ServicioFactory(nombre='estoneado', lista=True)
    
    def test_verificar_uniquetogheter_servicio_talla(self):
        servicio = ServicioFactory(lista=True)
        with self.assertRaises(DatabaseError):
            ListaPreciosFactory(servicio=servicio, talla=1)
    
    def test_verificar_servicio_precio_en_bolivianos_cambio_a_dolares(self):
        print 'Verificar el cambio a dolares de un servicio con precio en bolivianos'
        servicio = ServicioFactory()
        lista = ListaPreciosFactory(servicio=servicio, talla=1, precio_bolivianos=33.33)
        dolares = servicio.get_precio_dolares(talla=lista.talla, tipo_cambio=7.13)
        bolivianos = servicio.get_precio_bolivianos(talla=lista.talla, tipo_cambio=7.13)
        self.assertEquals(dolares,round((33.33/7.13),2))
        self.assertEquals(bolivianos,33.33)

    def test_verificar_servicio_precio_en_dolares_cambio_a_bolivianos(self):
        print 'Verificar el cambio a bolivianos de un servicio con precio en dolares'
        servicio = ServicioFactory()
        lista = ListaPreciosFactory(servicio=servicio, talla=1, precio_bolivianos=0.00, precio_dolares=0.33)
        dolares = servicio.get_precio_dolares(talla=lista.talla, tipo_cambio=7.13)
        bolivianos = servicio.get_precio_bolivianos(talla=lista.talla, tipo_cambio=7.13)
        self.assertEquals(bolivianos,round((0.33*7.13),2))
        self.assertEquals(dolares,0.33)
    
    def test_obtener_lista_de_precios_en_bs_dolares(self):
        print 'Prueba una lista de precios ingresada en bolivianos devuelve en dolares dado el tipo de cambio'
        dolares = round(float(self.servicio_estoneado.get_precio_dolares(talla=1,tipo_cambio=6.95)),2)
        bolivianos = round(float(self.servicio_estoneado.get_precio_bolivianos(talla=1,tipo_cambio=6.95)),2)
        self.assertEquals(dolares,round(bolivianos/6.95,2))
    
    def test_registrar_una_orden_de_pedido_menor_a_la_capacidad_empresa(self):
        print 'Verifica la creacion de una orden de pedido para el tipo de servicio lavado con capacidad menor a la de la empresa, entrega en 1 dia'
        #tplavado = TipoServicioFactory.build(titulo='Lavado', capacidad=self.capacidad_lavado)
        #lavado = ServicioFactory.build(tipo_servicio=tplavado)
        #op1 = OrdenPedidoFactory.build(servicio=[lavado], cantidad=self.capacidad_lavado)
        #self.assertFalse(op1.tiene_capacidad_libre(timezone.now()))


if __name__ == "__main__":
    import unittest2 as unittest
    unittest.main()