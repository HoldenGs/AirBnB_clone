#!/usr/bin/env bash
# Set up web servers for deployment
if [ ! -d /etc/nginx/ ]; then
    sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton yo!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "29i\        location /hbtn_static/ {\n                alias /data/web_static/current;\n        }\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
