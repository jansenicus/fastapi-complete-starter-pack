# Vanilla

## Vanilla FastAPI Features
- `https` enabled by default
- `HTTP/1.1` and `HTTP/2` support when using `hypercorn` server
- `HTTP/1.1` support only when using `uvicorn` server

## Enabler Package: 
 - jinja2
 - asyncio
 - uvicorn
 - uvloop
 - hypercorn[uvloop]

## Installation
```bash
pipenv install -r requirements.txt
```

## Run
```bash

pipenv run python main.py

```
or run with `uvicorn` 
```bash
cd vanilla/utils
./run-uvicorn.sh
```
or run with `hypercorn`
```bash
cd vanilla/utils
./run-hypercorn.sh
```
or run with `hypercorn` multi workers 
```bash
cd vanilla/utils
./run-hypercorn-multi.sh
```