from django.db import models
from django.utils.http import urlquote
from django.utils import timezone
from django.contrib.auth.models import User

class ClienteManager(models.Manager):
    
    def crear_cliente(self, **kwargs):
        user = User.objects.create_user(username=kwargs['ci'], email=kwargs['email'], password=kwargs['password1'])
        user.last_name = kwargs['nombres']
        user.first_name = kwargs['apellidos']
        user.is_active = False
        user.save()
        self.create(user=user, telefono=kwargs['telefono'], celular=kwargs['celular'],
                    direccion=kwargs['direccion'], ciudad=kwargs['ciudad'],
                    nombre_empresa=kwargs['nombre_empresa'], tipo_empresa=kwargs['tipo_empresa'],
                    numero_empleados=kwargs['numero_empleados'], productos=kwargs['productos'],
                    produccion=kwargs['produccion'], servicio_requerido=kwargs['servicio_requerido'],
                    servicio_preferencia=kwargs['servicio_preferencia'])
        return user