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

def deploy_templates():
    local("git push origin master")
    deploy_server()

def deploy_server():
    configure_server()
    is_repo_clean()
    server_update()
    server_migrate()
    with cd(env.project_dir):
        run(". apache2/bin/restart")

def is_local_repo_clean():
    with settings(warn_only=True):
        return local("git status 2>&1|grep 'nothing to commit' > /dev/null").succeeded

def is_repo_clean():
    with settings(warn_only=True):
        return run("git status 2>&1|grep 'nothing to commit' > /dev/null").succeeded

def server_update():
    with cd(env.project_dir_env):
        run("git pull")
        run("pip install updates_server.txt")

def server_migrate():
    with cd(env.project_dir_env):
        run("./manage.py syncdb")
        run("./manage.py migrate")

def configure_server():
    run("source ~/.bashrc")
