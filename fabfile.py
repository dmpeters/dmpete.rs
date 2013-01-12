from fabric.api import run
from fabric.api import local
from fabric.api import task


@task
def run(target="app/run.py"):
    local("python {}".format(target))