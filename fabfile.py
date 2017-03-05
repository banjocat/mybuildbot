from fabric.api import local, env

workers = [
        'worker',
        ]

env.shell = '/bin/bash'

def env():
    local('. ./env.sh && env')

def up():
    local(". ./env.sh && buildbot start master", shell='/bin/bash')
    for worker in workers:
        local(". ./env.sh && buildbot-worker start %s" % worker, shell='/bin/bash')

def reconfig():
    local("buildbot reconfig master")

def down():
    local("buildbot stop master")
    for worker in workers:
        local("buildbot-worker stop %s" % worker)

def log():
    local("tail -f ./master/twistd.log")

def restart():
    down()
    up()


