"""
main:
run-single-worker hypercorn serve API app
"""
import asyncio, signal, uvloop
from hypercorn.config import Config
from hypercorn.asyncio import serve
from app import API

config = Config()
config.bind = ["localhost:8080"]
config.use_reloader = True
config.keyfile = 'certs/key.pem'
config.certfile = 'certs/cert.pem'

if __name__ == "__main__":
    uvloop.install()
    asyncio.run(serve(API, config))