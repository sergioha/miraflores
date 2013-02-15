LOCAL_SETTINGS = True
from settings import *

DEBUG = True 
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',  
    'NAME': 'sergiohinojosa_n',           
    'USER': 'sergiohinojosa_n',           
    'PASSWORD': '6903e32e',   
    'HOST': '',               
    'PORT': '',               
    }
}
MEDIA_ROOT = '/home/sergiohinojosa/webapps/miraflores_media'
MEDIA_URL = 'http://media.airtac.pro.bo/'
ADMIN_MEDIA_URL = 'http://static.airtac.pro.bo/'
STATIC_ROOT = '/home/sergiohinojosa/webapps/miraflores_static'
STATIC_URL = 'http://static.airtac.pro.bo/'
#INSTALLED_APPS += ('south',)
TEMPLATE_DIRS = ('/home/sergiohinojosa/webapps/miraflores/miraflores/miraflores/templates/',)
STATICFILES_DIRS = (
'env/lib/python2.7/site-packages/django/contrib/admin/static/',
)
