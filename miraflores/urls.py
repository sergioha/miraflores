from django.conf.urls.defaults import * 
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^contactanos/', include('contactanos.urls')),
    (r'^zonacliente/', include('clientes.urls')),
    (r'^zonacliente/orden/', include('servicios.urls')),  
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
if settings.DEBUG:
    urlpatterns = patterns('',
                    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT,
                                    'show_indexes': True}),
                                        url(r'',
                                            include('django.contrib.staticfiles.urls')),
                                            ) + urlpatterns

