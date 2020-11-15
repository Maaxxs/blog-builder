#!/bin/bash

# Stop if any commands fails
set -e

cd /home/max/dev/blog/

# also fetch possible updates in the wiki repo
git pull --recurse-submodules

hugo

# Make .tar.gz backup of last version
tar -czf last_version.tar.gz /var/www/html

# Update content
rm -rf /var/www/html/*
cp /home/max/dev/blog/public/* /var/www/html/ -r



