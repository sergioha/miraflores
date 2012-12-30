from django.db import models
from django.utils.http import urlquote
from django.utils import timezone
from django.contrib.auth.hashers import check_password, make_password

class ClienteManager(models.Manager):
    def create_user(self, ci, email=None, nombres=None, apellidos=None, telefono=None, password=None, **extra_fields):
        now = timezone.now()
    #Crea una cuenta de cliente con su ci, nombres, apellidos, password y telefono. """
        if not ci:
            raise ValueError('El usuario debe registrar su documento de identidad')
        user = self.model(ci=ci, email=email, nombres=nombres, apellidos=apellidos, telefono=telefono,
                          is_active=False, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user