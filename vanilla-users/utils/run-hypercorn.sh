#!/bin/sh
cd ..
pipenv run hypercorn app:API --bind 0.0.0.0:8080 --reload --keyfile certs/key.pem --certfile certs/cert.pem
