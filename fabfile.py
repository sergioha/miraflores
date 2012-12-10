from fabric.api import env, local, cd, hosts, run
from fabric.contrib import django

django.project('miraflores')


DEV_USERHOST = "sergiohinojosa@sergiohinojosa.webfactional.com"
DEV_HOMEPATH = "webapps/miraflores"

def prepare_deploy():
    local("./manage.py test")
    local("git push origin master")

def dev_git_pull():
    """
    Realiza el pull en el servidor de Desarrollo
    """
    print("obteniendo el codigo del repositorio dev")
    with cd(env.)
