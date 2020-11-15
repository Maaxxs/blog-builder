#!/bin/bash

# Run with ./run.sh prod to execute in production environment

if [[ "$1" == "prod" ]]; then
    echo "Setting env variable for production mode"
    export PROD_APP_SETTINGS=prod_config.py
fi

pipenv run gunicorn -c gunicorn.conf.py listener:app 

unset PROD_APP_SETTINGS

