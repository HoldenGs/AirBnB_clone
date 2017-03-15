#!/usr/bin/env bash
# Set up web servers for deployment
if [ ! -d /etc/nginx/ ]; then
    sudo apt-get install -y nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton yo!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

sudo sed -i "29i\        location /hbtn_static/ {\n                alias /data/web_static/current;\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
