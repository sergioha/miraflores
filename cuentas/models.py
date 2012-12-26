from django.db import models
from django.contrib.auth.models import User
from cuentas.managers import ClienteManager

class Cliente(models.Model):
    TIPO_EMPRESA = (
            ('UNI', 'UNIPERSONAL'),
            ('SA', 'SOCIEDAD ANONIMA'),
            ('SC', 'SOCIEDAD COMANDITA'),
    )
    CIUDAD = (
        ('BENI','BENI'),
        ('COCHABAMBA','COCHABAMBA'),
        ('LA PAZ','LA PAZ'),
        ('ORURO', 'ORURO'),
        ('PANDO', 'PANDO'),
        ('POTOSI', 'POTOSI'),
        ('SANTA CRUZ', 'sANTA cRUZ'),
        ('SUCRE', 'SUCRE'),
        ('TARIJA', 'TARIJA'),
    )
    usuario = models.OneToOneField(User, 
                                   verbose_name = 'Usuario',
                                   related_name = 'usuario_cliente')

    ultima_actividad = models.DateTimeField('Ultima Actividad',
                                            blank = True,
                                            null = True,
                                            help_text = 'Es la ultima fecha que el cliente estuvo activo.')
    
    email_noconfirmado = models.EmailField('Direccion de Email no Confirmada',
                                           blank = True,
                                           help_text = 'Correo electronico temporal para modificar su correo electronico.')
    
    email_confirmar_cambio = models.BooleanField('Permitir Cambio de email',
                                                 default = False,
                                                 help_text = 'Activar para permitir el camnio de email')

    tipo_empresa = models.CharField('Tipo de Empresa',
                                    max_length = 3,
                                    choices = TIPO_EMPRESA,
                                    blank = False)

    servicio_requerido = models.CharField('Servicios Requeridos',
                                          max_length = 100,
                                          blank = False)

    servicio_preferencia = models.CharField('Servicios Preferidos',
                                          max_length = 25,
                                          blank = False)

    telefono = models.IntegerField('Telefono Fijo',
                                          null = False,
                                          blank = False)

    celular = models.IntegerField('No Telefono Celular',
                                          null = False,
                                          blank = False)

    direccion = models.CharField('Direccion',
                                 max_length = 150,
                                 blank = False)

    ciudad = models.CharField('Ciudad',
                              max_length = 15,
                              choices = CIUDAD,
                              blank = False)

    objects = ClienteManager()

    class Meta:
        verbose_name = 'Cuenta Cliente'
        verbose_name_plural = 'Cuentas de Clientes'

    def __unicode__(self):
        return '%s' % self.usuario

    def requerimiento_cambio_email(self, email):
        """
        Permite cambiar el email de la cuenta cliente.

        El usuario podra cambiar su email personal pero esta se almacenara
        temporalmente en un campo temporal ''email_temporal'' -- este email
        sera activado para su uso una vez el administrador de la empresa
        realize la verificacion mediante llamada telefonica para seguridad de
        la informacion que se enviara.

        :param email:
            La nueva direccion de correo electronico que el usuario desea usar.
        """

        self.email_noconfirmado = email
        self.confirmar_cambio = True
        self.save()

    def confirmar_cambio_email(self):
        pass




