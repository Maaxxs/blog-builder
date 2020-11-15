#!/bin/bash

pipenv run gunicorn -c gunicorn.conf.py listener:app
