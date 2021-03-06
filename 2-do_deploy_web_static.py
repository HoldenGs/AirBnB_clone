#!/usr/bin/python3

from fabric.api import *
from time import strftime
from os import path

env.hosts = ['52.23.152.105', '52.203.4.8']
archive_path = None


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


def do_deploy(archive_path):
    """
    Deploy an archive to the webservers
    """
    if archive_path is None:
        return False

    try:
        archive = archive_path.split('/')[1]
        put(archive_path, '/tmp/')
        webfolder = archive.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(webfolder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive, webfolder))
        run('rm /tmp/{}'.format(archive))
        run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(webfolder, webfolder))
        run('rm -rf /data/web_static/current')
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(webfolder))
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(webfolder))
        return True
    except:
        return False
