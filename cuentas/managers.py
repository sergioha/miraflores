from django.contrib.auth.models import User, UserManager
from cuentas.utils import get_fechahora

class ClienteManager(UserManager):
    """ Funcionalidad que agregamos al modelo Cliente. """

    def create_user(self, email, password, **kwargs):
        """
        Es un metodo que crea un nuevo objeto del tipo :class: 'User' usando el correo
        electronico del cliente como nombre de usuario para el sistema.

        :param email:
            String - Es una cadena de texto que contiene el correo electronico del
            Cliente.

        :param password:
            String - Cadena de texto que contiene el password del Cliente.

        :param activo:
            Boolean - Define si la cuenta ha sido activada por el
            administrador.

        :param **kwargs:
            Lista con llaves - Contiene los demas atributos del cliente, como
            direccion, telefono, celular, etc.

        :return :class 'User' instancia que representa a la cuenta de usuario
        del cliente.

        """
        ahora = get_fechahora()

        usuario_nuevo = User.objects.create_user(email, email, password)
        usuario_nuevo.is_active = False
        usuario_nuevo.save()

        cliente = self.crear_cuenta_cliente(usuario_nuevo, **kwargs)
        return usuario_nuevo

    def crear_cuenta_cliente(self, usuario, **kwargs):
        """
        Crea una cuenta :class: 'Cliente' para el usuario 
        """
        return self.create(usuario=usuario, **kwargs)







