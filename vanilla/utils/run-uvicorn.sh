#!/bin/sh
cd ..
pipenv run uvicorn app:API --reload --host 127.0.0.1 --port 8000 --ssl-keyfile=certs/key.pem --ssl-certfile=certs/cert.pem