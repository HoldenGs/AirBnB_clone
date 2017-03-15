#!/usr/bin/env bash
# Set up web servers for deployment

if [ ! -d /etc/nginx/ ]; then
    sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
webpath="/data/web_static/releases/test/"
echo "<html><head></head><body>Holberton Yo!</body></html>" | sudo tee "${webpath}/index.html" > /dev/null

sudo ln -sf "$webpath" /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo grep -q /etc/nginx/sites-enabled/default -e "hbnb_static"
result=$?
if [ "$result" -eq 1 ]; then
    sudo sed -i "29i\        location /hbnb_static/ {\n                alias /data/web_static/current/;\n        }\n" /etc/nginx/sites-available/default
fi
sudo service nginx restart
