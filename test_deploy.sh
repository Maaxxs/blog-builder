#!/bin/bash

# test deploy script to test redirect of stdout and stderr

set -e 

echo "Would be building webpage"

# stderr
echo "Error Things" 1>&2

echo "done"
