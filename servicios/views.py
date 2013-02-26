from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
#from django.contrib import messages

from clientes.models import Cliente, User

from servicios.forms import OrdenForm
from servicios.models import Servicio, Orden, DetalleOrden

def registrar_orden(request, extra_context=None):
    #TODO: create a decorator
    if 'user_id' not in request.session:
        return redirect(reverse('ingresar'))
    user = User.objects.get(username=request.session['user_id'])
    cliente = Cliente.objects.get(user=user)
    if request.method == 'POST':
        form = OrdenForm(queryset=Servicio.objects.order_by('tipo_servicio__prioridad'), data=request.POST)
        if form.is_valid():
            servicios = form.cleaned_data['servicios']
            cantidad = form.cleaned_data['cantidad']
            talla = form.cleaned_data['talla']
            observaciones = form.cleaned_data['observaciones']
            orden = Orden(cliente=cliente, cantidad=cantidad, talla=talla, observaciones=observaciones)
            orden.save()
            for servicio in servicios:
                detalle = DetalleOrden(orden=orden, servicio=servicio)
                detalle.save()
            extra_context = {'mensaje':'Su Pedido fue registrado con exito!'}
            form = OrdenForm(queryset=Servicio.objects.order_by('tipo_servicio__prioridad'))
    else:
        form = OrdenForm(queryset=Servicio.objects.order_by('tipo_servicio__prioridad'))
    if extra_context is None:
        extra_context = {'titulo':'Registrar Pedido'}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response('servicios/registrar_pedido.html',
                              { 'form': form, 'cliente': cliente },
                              context_instance=context)

def detalle_orden(request, pk=None):
    if 'user_id' not in request.session:
        return redirect(reverse('ingresar'))
    user = User.objects.get(username=request.session['user_id'])
    cliente = Cliente.objects.get(user=user)
    detalles = None
    orden = None
    mensaje = None
    try:
        orden = Orden.objects.get(pk=pk, cliente=cliente)
        detalles = DetalleOrden.objects.filter(orden=orden).order_by('servicio__tipo_servicio__prioridad')
    except Orden.DoesNotExist:
        mensaje = 'Lo siento pero no se tiene registro de este proceso, por favor comunicarse con el Administrador.'
    return render_to_response('servicios/detalle_orden.html',
                              { 'cliente': cliente, 'orden':orden, 'detalles':detalles, 'mensaje':mensaje })

def listar_ordenes(request):
    if 'user_id' not in request.session:
        return redirect(reverse('ingresar'))
    user = User.objects.get(username=request.session['user_id'])
    cliente = Cliente.objects.get(user=user)
    return render_to_response('servicios/listar_ordenes.html',
                              { 'cliente': cliente })
    