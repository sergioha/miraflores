from fabric.api import env, require, local, cd, lcd, hosts, sudo, run
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
env.project_dir_env = env.project_dir + PROJECT_NAME
env.settings_dir = env.project_dir + '/' + SETTINGS_SUBDIR

def deploy_templates():
    local("git push origin master")
    deploy_server()

def deploy_server():
    with cd(env.project_dir_env):
        run("git pull")
    with cd(env.project_dir):
        run(". apache/bin/restart")

