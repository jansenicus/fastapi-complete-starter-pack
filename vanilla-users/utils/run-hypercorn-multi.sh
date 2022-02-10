#!/bin/sh
cd ..
pipenv run hypercorn app:API --workers 8 --keyfile certs/key.pem --certfile certs/cert.pem
