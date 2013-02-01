from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from contactanos.views import contact_form

urlpatterns = patterns('',
    url(r'^$', contact_form, name='contactanos'),
    url(r'^enviado/$', direct_to_template,
        { 'template': 'contactanos/enviado.html' },name='enviado'),
)