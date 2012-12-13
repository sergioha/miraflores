import os
from fabric.api import env, require, local, cd, hosts, sudo, run
from fabric.contrib import django

django.project('miraflores')

env.project_name = 'miraflores'
env.server_name= 'sergiohinojosa.webfactional.com'
env.webapps_root='/home/sergiohinojosa/webapps/'
env.project_root=os.path.join(env.webapps_root, env.project_name)


def prepare_deploy():
    local("./manage.py test")
    local("git push origin master")

def dev_git_pull():
    """
    Realiza el pull en el servidor de Desarrollo
    """
    print("obteniendo el codigo del repositorio dev")
    with cd(env.)
