#!/bin/sh
pipenv install -r requirements.txt
pipenv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
