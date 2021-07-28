#!/bin/bash

# Stop if any commands fails
set -e

# update wiki repo
cd /home/max/dev/blog/content/wiki
git pull

# update main repo
cd /home/max/dev/blog
git pull

hugo

# Make .tar.gz backup of last version
# -P is --absolute-names. Gets rid of message
# "tar: Removing leading '/' from member names"
# which is printed to stderr and stops this script
tar -czPf last_version.tar.gz /var/www/html

# Update content
rm -rf /var/www/html/*
cp /home/max/dev/blog/public/* /var/www/html/ -r



