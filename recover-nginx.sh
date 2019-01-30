#!/bin/sh

mkdir /var/log/nginx
touch /var/log/nginx/error.log
touch /var/log/nginx/access.log
systemctl restart nginx.service