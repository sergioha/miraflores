import os, sys, site
from django.core.handlers.wsgi import WSGIHandler

site.addsitedir('/home/sergiohinojosa/webapps/miraflores/env/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'miraflores.settings'
project = '/home/sergiohinojosa/webapps/miraflores/miraflores/'
workspace = os.path.dirname(project)
sys.path.append(workspace)
application = WSGIHandler()
