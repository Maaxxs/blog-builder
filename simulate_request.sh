#!/bin/bash

if [[ $1 -eq "1" ]]; then
    # correct signature
    curl -H "X-Github-Event: push" -H "X-Hub-Signature-256: sha256=d66efe361e766312917abc9c03e8efa27c3bbdee6ebcf41be6c4f479afba4805" -H "Content-Type: application/json" -d '{"json": "asdf"}' http://127.0.0.1:5000/api/github/push
else 

    # incorrect signature
    curl -H "X-Github-Event: push" -H "X-Hub-Signature-256: sha256=e66efe361e766312917abc9c03e8efa27c3bbdee6ebcf41be6c4f479afba4805" -H "Content-Type: application/json" -d '{"json": "asdf"}' http://127.0.0.1:5000/api/github/push
fi
