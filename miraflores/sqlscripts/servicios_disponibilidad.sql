create or replace view servicios_disponibilidad as
SELECT tipo.id AS tipo_servicio_id, tipo.capacidad, sum(orden.cantidad) as ocupado, (tipo.capacidad - sum(orden.cantidad)) as disponible, detalle.fecha_ejecucion
FROM servicios_detalleorden detalle, servicios_tiposervicio tipo, servicios_servicio servicio, servicios_orden orden, clientes_cliente cliente
WHERE servicio.tipo_servicio_id = tipo.id AND detalle.servicio_id = servicio.id AND detalle.orden_id = orden.id AND cliente.user_id = orden.cliente_id and detalle.terminado=False
group by tipo.id, tipo.capacidad, detalle.fecha_ejecucion
