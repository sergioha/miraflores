from functools import wraps

from django.shortcuts import render_to_response, render, redirect
from django.core.urlresolvers import reverse

def login_cliente_required(view_func):
    """
    Decorador para verificar las vistas que el cliente logeado activo
    puede acceder en la zona cliente, en caso contrario le reenvia a
    la pagina de login cliente.
"""
    @wraps(view_func)
    def _checklogin(request, *args, **kwargs):
        if 'user_id' in request.session:
            return view_func(request, *args, **kwargs)
        return redirect(reverse('ingresar'))
    return _checklogin
