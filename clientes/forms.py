from django import forms
from django.contrib.auth.models import User

from clientes.models import Cliente

attrs_dict = {'class': 'requerido'}

class ClienteRegistroForm(forms.ModelForm):
    ci = forms.RegexField(regex=r'', max_length=15, min_length=3, error_message='No se permiten caracteres especiales ni espacios en blanco.')
    nombres = forms.RegexField(regex=r'', max_length=30)
    apellidos = forms.RegexField(regex=r'', max_length=30)
    email = forms.EmailField(max_length=40)
    password1 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Contrasena')
    password2 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Repita la contrasena')

    def clean_ci(self):
        try:
            usuario = User.objects.get(username__iexact=self.cleaned_data['ci'])
        except User.DoesNotExist:
            return self.cleaned_data(self.ci)
        raise forms.ValidationError(message='El ci ya fue registrado anteriormente.')

    def clean_password2(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(message='Las contrasenas deben ser iguales.')
        return self.cleaned_data

    def save(self):
        usuario = Cliente.objects.crear_cliente(**self.cleaned_data)
        return usuario

    class Meta:
        model = Cliente
        exclude = ('user',)