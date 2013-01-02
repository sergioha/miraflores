from django.shortcuts import render
from django.http import HttpResponseRedirect
from clientes.forms import ClienteRegistroForm

def registro_nuevo_cliente(request):
    if request.method == 'POST': 
        form = ClienteRegistroForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zonacliente/registro_exitoso/')
    else:
        form = ClienteRegistroForm()
    return render(request, 'clientes/comun/registro.html', {
        'form': form,
    })