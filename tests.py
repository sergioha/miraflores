"""
python tests.py

"""
import sys
import os

os.environ["DJANGO_SETTINGS_MODULE"] = 'miraflores.settings'
from miraflores import settings

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/sergio/Desktop/miraflores/devMiraflores/miraflores/dbtest.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

settings.INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sites',
    'cuentas',
    'tests',
)
settings.TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

def main():
    from django.test.utils import get_runner
    test_runner = get_runner(settings)(interactive = True)
    failures = test_runner.run_tests(['tests',])
    sys.exit(failures)

if __name__ == '__main__':
    main()

