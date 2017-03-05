from fabric.api import local

workers = [
        'worker',
        ]

def up():
    local("buildbot start master")
    for worker in workers:
        local("buildbot-worker start %s" % worker)

def down():
    local("buildbot-worker stop worker")
    for worker in workers:
        local("buildbot-worker stop %s" % worker)
