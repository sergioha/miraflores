from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages

from clientes.forms import ClienteRegistroForm, LoginForm
from clientes.models import Cliente, User

def registro_nuevo_cliente(request, success_url=None,
                           template_name='clientes/registro.html',
                           extra_context=None):
    if request.method == 'POST': 
        form = ClienteRegistroForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso!! Ahora puede ingresar usando su cuenta.')
            return redirect(reverse('ingresar'))
    else:
        form = ClienteRegistroForm()
    if extra_context is None:
        extra_context = {'titulo':'Registro Nuevo Cliente'}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response(template_name,
                              { 'form': form },
                              context_instance=context)

def cliente_login(request, extra_context=None):
    if 'user_id' in request.session:
        request.session.flush()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user_id'] = form.cleaned_data['username']
            return redirect('/zonacliente/inicio/')
    else:
        form = LoginForm()
    if extra_context is None:
        extra_context = {'titulo':'Registro Nuevo Cliente'}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response('clientes/login.html',
                              { 'form': form }, context_instance=context)

def cliente_logout(request):
    if 'user_id' in request.session:
        request.session.flush()
    return redirect(reverse('ingresar'))

def cliente_inicio(request, extra_context=None):
    if 'user_id' not in request.session:
        return redirect(reverse('ingresar'))
    user = User.objects.get(username=request.session['user_id'])
    cliente = Cliente.objects.get(user=user)
    if extra_context is None:
        extra_context = {'titulo':'Registro Nuevo Cliente'}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response('clientes/inicio.html',
                              { 'mensaje': 'Bienvenido!!',
                                'cliente': cliente, 'tipo_cambio': request.session['tipo_cambio']},
                              context_instance=context)