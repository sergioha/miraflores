from django.db import models
from django.utils.http import urlquote
from django.utils import timezone
from django.contrib.auth.models import User
from clientes.managers import ClienteManager

class Cliente(models.Model):

    TIPO_EMPRESA = (
            ('UNI', 'UNIPERSONAL'),
            ('SA', 'SOCIEDAD ANONIMA'),
            ('SC', 'SOCIEDAD COMANDITA'),
            ('SRL', 'SOCIEDAD DE RESPONSABILIDAD LIMITADA'),
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
    user = models.OneToOneField(User, primary_key=True)
    telefono = models.IntegerField('Numero Telefono Fijo', null=True, blank=True)
    celular = models.IntegerField('Numero Telefono Celular', null=True, blank=True)
    direccion = models.CharField('Direccion', max_length=150)
    ciudad = models.CharField('Ciudad', max_length=15, choices=CIUDAD)
    nombre_empresa = models.CharField('Nombre Empresa', max_length=100, default='N/A',
                                      help_text='Si no tiene nombre deje en blanco la casilla.')
    tipo_empresa = models.CharField('Tipo de Empresa', max_length=3, choices=TIPO_EMPRESA)
    numero_empleados = models.IntegerField('Numero de Empleados', blank=True, null=True)
    productos = models.CharField ('Productos Fabricados', max_length=100, blank=True, null=True)
    produccion = models.IntegerField('Produccion Mensual', blank=True, null=True,
                                     help_text = 'Estimado de prendas al mes que produce.')
    servicio_requerido = models.CharField('Servicios Requeridos', max_length=100, blank=True, null=True)
    servicio_preferencia = models.CharField('Servicios Preferidos', max_length=25, blank=True, null=True)
   
    objects = ClienteManager()

    class Meta:
        verbose_name = 'Cuenta Cliente'
        verbose_name_plural = 'Cuentas de Clientes'
        
    def __unicode__(self):
        return '%s con ci: %s' % (self.get_nombre_completo(), self.user.username)

    def set_password(self, contrasena):
        self.user.set_password(contrasena)

    def verificar_contrasena(self, contrasena):
        return User.check_password(contrasena)

    def get_absolute_url(self):
        return "/cliente/%s" % urlquote(self.user.username)

    def get_nombre_completo(self):
        return self.user.get_full_name()

    @property
    def nombre_completo(self):
        return self.user.get_full_name()

    @property
    def ci(self):
        return self.user.username

    @property
    def nombres(self):
        return self.user.first_name

    @property
    def apellidos(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email




