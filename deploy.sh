#!/bin/bash

# Stop if any commands fails
set -e

cd /home/max/dev/blog
git pull
git submodule update --init

hugo

# Make .tar.gz backup of last version
# -P is --absolute-names. Gets rid of message
# "tar: Removing leading '/' from member names"
# which is printed to stderr and stops this script
tar -czPf last_version.tar.gz /var/www/html

# Update content
rm -rf /var/www/html/*
cp /home/max/dev/blog/public/* /var/www/html/ -r



