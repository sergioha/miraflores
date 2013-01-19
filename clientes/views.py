from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from clientes.forms import ClienteRegistroForm, LoginForm

def registro_nuevo_cliente(request, success_url=None,
                           template_name='clientes/registro.html',
                           extra_context=None):
    if request.method == 'POST': 
        form = ClienteRegistroForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url or reverse('registro_completado'))
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

def cliente_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user_id'] = form.cleaned_data['username']
            return redirect('/zonacliente/inicio/')
    else:
        form = LoginForm()
    return render(request,'clientes/login.html',{'form':form})