from fabric.api import local, with_settings

workers = [
        'worker',
        ]

try:
    with open('./env.sh') as f:
        environment = f.read()
except IOError:
    raise SystemExit("Must create env.sh first")

@with_settings(prefix=environment)
def up():
    local("buildbot start master", shell='/bin/bash')
    for worker in workers:
        local("buildbot-worker start %s" % worker, shell='/bin/bash')

def reconfig():
    local("buildbot reconfig master")

def down():
    local("buildbot stop master")
    for worker in workers:
        local("buildbot-worker stop %s" % worker)

def log():
    local("tail -f ./master/twistd.log")

