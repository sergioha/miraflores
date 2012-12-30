from django.db import models
from django.utils.http import urlquote
from django.utils import timezone
from django.contrib.auth.hashers import check_password, make_password
from clientes.managers import ClienteManager

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
    ci = models.CharField('Documento Identidad', max_length=15, unique=True,
                           help_text = 'Su numero de documento lo usara para ingresar al sistema.')
    password = models.CharField('Contrasena', max_length=128)
    nombres = models.CharField('Nombres', max_length=40, blank=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True)
    email = models.EmailField('Correo Electronico', blank=True)
    telefono = models.IntegerField('Telefono Fijo', null=False, blank=False)
    celular = models.IntegerField('No Telefono Celular', null=False, blank=False)
    direccion = models.CharField('Direccion', max_length=150, blank=False)
    ciudad = models.CharField('Ciudad', max_length=15, choices=CIUDAD, blank=False)
    nombre_empresa = models.CharField('Nombre Empresa', max_length=100, blank=False,
                                      help_text='Si no tiene nombre coloque N/A por favor.')
    tipo_empresa = models.CharField('Tipo de Empresa', max_length=3, choices=TIPO_EMPRESA, blank=False)
    numero_empleados = models.IntegerField('Numero de Empleaso')
    productos = models.CharField ('Productos Fabricados', max_length=100)
    produccion = models.IntegerField('Produccion Mensual', blank=True, null=True,
                                     help_text = 'Estimado de prendas al mes que produce.')
    servicio_requerido = models.CharField('Servicios Requeridos', max_length=100, blank=False)
    servicio_preferencia = models.CharField('Servicios Preferidos', max_length=25, blank=False)
    date_joined = models.DateTimeField('Fecha Registro Cuenta', default=timezone.now)
    is_active = models.BooleanField('Cuenta activa', default=False, help_text='Solo las cuentas activas tiene acceso a la seccion de clientes.')
    
    objects = ClienteManager()

    class Meta:
        verbose_name = 'Cuenta Cliente'
        verbose_name_plural = 'Cuentas de Clientes'
        
    def __unicode__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    def set_password(self, contrasena):
        self.password = make_password(contrasena)

    def verificar_contrasena(self, contrasena):
        def setter(contrasena):
            self.set_password(contrasena)
            self.save()
        return check_password(contrasena, self.password, setter)

    def get_absolute_url(self):
        return "/cliente/%s" % urlquote(self.ci)

    def get_full_name(self):
        nombre_completo = '%s %s' % (self.nombres, self.apellidos)
        return nombre_completo.strip()
    
    def get_short_name(self):
        return self.ci
    
    def enviar_email(self, titulo, mensaje, de_email=None):
        send_email(titulo, mensaje, de_email)





