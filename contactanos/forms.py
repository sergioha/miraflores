from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
from django.contrib.sites.models import Site

attrs_dict = { 'class': 'required' }

class ContactForm(forms.Form):

    def __init__(self, data=None, files=None, request=None, *args, **kwargs):
        if request is None:
            raise TypeError("Debe pasarse como parametro 'request'")
        super(ContactForm, self).__init__(data=data, files=files, *args, **kwargs)
        self.request = request
    
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs=attrs_dict),
                           label=u'Nombre Completo')
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=200)),
                             label=u'Direccion de correo electronico')
    body = forms.CharField(widget=forms.Textarea(attrs=attrs_dict),
                              label=u'Mensaje')
    
    from_email = settings.DEFAULT_FROM_EMAIL
    
    recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]

    subject_template_name = "contactanos/form_tema.txt"
    
    template_name = 'contactanos/form.txt'

    def message(self):
        """
        Renderiza el cuerpo del mensaje a tipo string.
        
        """
        if callable(self.template_name):
            template_name = self.template_name()
        else:
            template_name = self.template_name
        return loader.render_to_string(template_name,
                                       self.get_context())
    
    def subject(self):
        """
        Renderiza el subject del mensaje a tipo string.
        
        """
        subject = loader.render_to_string(self.subject_template_name,
                                          self.get_context())
        return ''.join(subject.splitlines())
    
    def get_context(self):
        if not self.is_valid():
            raise ValueError("No puede generar Context de un formulario invalido")
        return RequestContext(self.request,
                              dict(self.cleaned_data,
                                   site=Site.objects.get_current()))
    
    def get_message_dict(self):
        if not self.is_valid():
            raise ValueError("El mensaje no puede ser enviado por que contiene errores!")
        message_dict = {}
        for message_part in ('from_email', 'message', 'recipient_list', 'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = callable(attr) and attr() or attr
        return message_dict
    
    def save(self, fail_silently=False):
        send_mail(fail_silently=fail_silently, **self.get_message_dict())