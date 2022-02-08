#!/bin/sh
pipenv install -r requirements.txt
pipenv run uvicorn main:API --reload --host 127.0.0.1 --port 8000
