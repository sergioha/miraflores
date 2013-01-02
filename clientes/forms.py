from django.forms import ModelForm, PasswordInput
from clientes.models import Cliente

class ClienteRegistroForm(ModelForm): 
    class Meta:
        model = Cliente
        exclude = ('date_joined', 'is_active',)
        widgets = {
            'password' : PasswordInput(),
        }