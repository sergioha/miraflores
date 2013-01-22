-- View: servicios_disponibilidad

-- DROP VIEW servicios_disponibilidad;

CREATE OR REPLACE VIEW servicios_disponibilidad AS 
 SELECT tipo.id AS tipo_servicio_id, tipo.capacidad, sum(orden.cantidad) AS ocupado, tipo.capacidad - sum(orden.cantidad) AS disponible, detalle.fecha_ejecucion
   FROM servicios_detalleorden detalle, servicios_tiposervicio tipo, servicios_servicio servicio, servicios_orden orden, clientes_cliente cliente
  WHERE servicio.tipo_servicio_id = tipo.id AND detalle.servicio_id = servicio.id AND detalle.orden_id = orden.id AND cliente.user_id = orden.cliente_id AND detalle.terminado = false AND detalle.fecha_ejecucion >= now()
  GROUP BY tipo.id, tipo.capacidad, detalle.fecha_ejecucion;

