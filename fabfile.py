import sys
from fabric.api import settings, env, require, local, cd, lcd, hosts, sudo, run
from fabric.contrib import django

try:
    from fabsettings import WF_HOST, PROJECT_NAME, REPOSITORY, USER, PASSWORD
except ImportError:
    print "ImportError: Couldn't find fabsettings.py, it either does not exist or giving import problems (missing settings)"
    sys.exit(1)

django.project('miraflores')
env.hosts = [WF_HOST]
env.user = USER
env.password = PASSWORD
env.project = PROJECT_NAME
env.repo = REPOSITORY
env.home = "/home/%s" % USER
env.project_dir = env.home + '/webapps/' + PROJECT_NAME
env.project_dir_env = env.project_dir + '/' + PROJECT_NAME

def push():
    with settings(warn_only=False):
        local('git push origin master')

def deploy_templates():
    local("git push origin master")
    deploy_server()

def deploy_local():
    with settings(warn_only=False):
        local('python manage.py syncdb')
        local('python manage.py migrate')
        local('python manage.py run_gunicorn')

def deploy_server():
    is_repo_clean()
    server_update()

def is_local_repo_clean():
    with settings(warn_only=True):
        return local("git status 2>&1|grep 'nothing to commit' > /dev/null").succeeded

def is_repo_clean():
    with settings(warn_only=True):
        return run("git status 2>&1|grep 'nothing to commit' > /dev/null").succeeded

def server_update():
    with cd(env.project_dir_env):
        run(". ../env/bin/activate")
        run("git pull")
        #run("cp updates_server.txt requirements.txt")
        #run("pip-2.7 install requirements.txt")
        run(". ../env/bin/activate && ./manage.py syncdb")
        #run("./manage.py migrate")
        run(". apache2/bin/restart")

def server_migrate():
    with cd(env.project_dir_env):
        run("./manage.py syncdb")
        run("./manage.py migrate")

def configure_server():
    with cd(env.project_dir):
        run(". ../env/bin/activate")

def deploy_static():
    with cd(env.project_dir_env):
        run("git pull")
        run(". ../env/bin/activate && . apache2/bin/restart")
