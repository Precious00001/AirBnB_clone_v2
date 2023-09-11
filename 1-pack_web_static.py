#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""

from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    pathToFile = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        local(" mkdir versions")
    local('tar -cvzf ' + pathToFile + ' web_static')
    if os.path.exists(pathToFile):
        return pathToFile
    return None
