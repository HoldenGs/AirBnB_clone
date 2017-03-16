#!/usr/bin/python3

from fabric.api import *
from time import strftime
from os import path


def do_pack():
    """
    Archive the web_static folder contents in a folder called 'versions'
    """
    try:
        if not path.exists("./versions/"):
            local("mkdir versions")
        timestr = strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(timestr))
        return "versions/web_static_{}.tgz".format(timestr)
    except:
        return None
