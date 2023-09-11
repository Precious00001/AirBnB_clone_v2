#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.

from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path

env.hosts = ['54.160.119.87', '100.26.53.47']


def do_deploy(archive_path):
    """
        return the archive path if archive has generated correctly.
    """
    if os.path.exists(archive_path) is False:
        return False
    NameOfArch = archive_path.split('/')[1]
    arch_name_nex = NameOfArch.split(".")[0]
    rePath = "/data/web_static/releases/" + arch_name_nex
    up_path = '/tmp/' + NameOfArch
    put(archive_path, up_path)
    run('mkdir -p ' + rePath)
    run('tar -xzf /tmp/{} -C {}/'.format(NameOfArch, rePath))
    run('rm {}'.format(up_path))
    mv = 'mv ' + rePath + '/web_static/* ' + rePath + '/'
    run(mv)
    run('rm -rf ' + rePath + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + rePath + ' /data/web_static/current')
    return True
