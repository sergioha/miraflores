﻿-- View: servicios_cronograma

-- DROP VIEW servicios_cronograma;

CREATE OR REPLACE VIEW servicios_cronograma AS 
    SELECT detalle.id, cliente.user_id, orden.id AS orden_id, orden.cantidad, orden.talla, tipo.id AS tipo_servicio_id, tipo.nombre AS nombre_tiposervicio, servicio.id AS servicio_id, servicio.nombre AS nombre_servicio, detalle.fecha_ejecucion, detalle.terminado FROM servicios_detalleorden detalle, servicios_tiposervicio tipo, servicios_servicio servicio, servicios_orden orden, clientes_cliente cliente
    WHERE ((((servicio.tipo_servicio_id = tipo.id) AND (detalle.servicio_id = servicio.id)) AND (detalle.orden_id = orden.id)) AND (cliente.user_id = orden.cliente_id)) AND detalle.fecha_ejecucion >= now();

