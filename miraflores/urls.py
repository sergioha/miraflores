from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'miraflores.views.home', name='home'),
    # url(r'^miraflores/', include('miraflores.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
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

