import datetime

from django.utils import timezone
from django.test import TestCase
from django.db import DatabaseError

from servicios.models import *
from servicios.tests.factories import *


class ServiciosTestSuite(TestCase):
    
    contador_tipos = 0
    tipo_servicio = None
    capacidad_lavado = CAPACIDAD
    servicio_estoneado = None
    
    def setUp(self):
        self.tipo_servicio = TipoServicioFactory()
        self.contador_tipos+=2
        self.servicio_estoneado = ServicioFactory(nombre='estoneado', lista=True)
    
    def test_crear_nuevo_tipo_servicio(self):
        tipo_servicio_1 = TipoServicioFactory()
        tipos = TipoServicio.objects.all()
        print 'Verifica que el numero de tipo de servicios creados este correcto'
        contador = self.contador_tipos +1
        self.assertEqual(len(tipos),contador)#verificamos el nuevo registro contando
        print 'Verifica que el tipo de servicios creado se encuentre almacenado en la base de datos'
        self.assertIn(tipo_servicio_1, tipos, msg="El tipo de servicio no fue creado")
   
    def test_tipo_servicio_titulo_no_valido(self):
        print 'Verifica que nos lanze un error en la base de datos al crear un tipo de servicio con un titulo ya existente.'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(nombre=self.tipo_servicio.nombre)

    def test_tipo_servicio_capacidad_no_valida(self):
        print 'Verifica que nos lanze un error en la base de datos al ingresar una capacidad grande'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(capacidad=3333333*33333)
        print 'Verifica que nos lanze un error en la base de datos al ingresar una capacidad con valor negativo'
        with self.assertRaises(DatabaseError):
            TipoServicioFactory(capacidad=-300)

    def test_crear_nuevo_servicio(self):
        print 'Verifica la creacion correcta de un servicio'
        self.assertEqual(len(Servicio.objects.all()),1)
        print 'Verifica que no se cree un servicio con el nombre repetido'
        with self.assertRaises(DatabaseError):
            ServicioFactory(nombre='estoneado')

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

class OrdenesDePedidoTestSuite(TestCase):
    
    servicio_prelavado = None
    servicio_estoneado = None
    servicio_rasgado = None
    
    def setUp(self):
        self.servicio_prelavado = ServicioFactory(nombre='pre lavado', lista=True)
        self.servicio_estoneado = ServicioFactory(nombre='estoneado', lista=True)
        self.servicio_rasgado = ServicioFactory(nombre='rasgado', lista=True)
    
    def test_registrar_orden_creacion_detalle_automatico(self):
        print 'Verifica de una orden ingresada se creen las 3 instancia de DetalleOrden test de Ordenfactory'
        orden = OrdenFactory(detalle=True)
        self.assertEquals(DetalleOrden.objects.all().count(),3)

    def test_registrar_orden_sin_creacion_detalle_automatica(self):
        print 'Verifica de una orden ingresada se obtenga una lista sin instancias de DetalleOrden test de Ordenfactory'
        orden = OrdenFactory(detalle=False)
        self.assertEquals(DetalleOrden.objects.all().count(),0)

    def test_obtener_lista_detalleorden_por_ejecutar(self):
        print 'Verifica que se listen correctamente los servicios no termiandos'
        orden = OrdenFactory(detalle=True)
        self.assertEquals(DetalleOrden.noterminados.all().count(),3)
        detalle = DetalleOrden.noterminados.all()[0]
        detalle.terminado = True
        detalle.save()
        self.assertEquals(DetalleOrden.noterminados.all().count(),2)

    def test_obtener_lista_detalleorden_por_ejecutar_por_fecha(self):
        print 'dada una fecha con 2 ordenes con una se ocupa la capacidad'
        orden1 = OrdenFactory(detalle=True, cantidad = 400)
        orden2 = OrdenFactory(detalle=True, cantidad = 110)
        self.assertEquals(DetalleOrden.noterminados.por_fecha_ejecucion().count(),6)
        tipo = TipoServicio.objects.all()[0]
        capacidad = DetalleOrden.noterminados.get_capacidad(fecha_ejecucion=orden1.fecha_entrega, tipo_servicio=tipo)
        self.assertEqual(capacidad, 500)
        #detalle1 = DetalleOrdenFactory(orden= orden, servicio=self.servicio_prelavado)
        #detalle2 = DetalleOrdenFactory(orden= orden, servicio=self.servicio_estoneado)
        #detalle3 = DetalleOrdenFactory(orden= orden, servicio=self.servicio_rasgado)
        #detalle_orden = orden.get_detalle()
        #self.assertIn(detalle1,detalle_orden)
        #servicios = orden.get_lista_servicios()
        #self.assertIn(self.servicio_prelavado, servicios)
  
    def test_registrar_una_orden_de_pedido_menor_a_la_capacidad_empresa(self):
        print 'Verifica la creacion de una orden de pedido con capacidad menor a la de la empresa'
        #op1 = OrdenFactory.build(cantidad=self.capacidad_lavado)
        #op1detalle = DetalleOrdenFactory(orden=op1, servicio=servicio_1)
        #op1detalle = DetalleOrdenFactory(orden=op1, servicio=servicio_2)
        #self.assertTrue(op1.tiene_capacidad_libre(timezone.now()))