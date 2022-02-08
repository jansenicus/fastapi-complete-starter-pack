from fastapi import FastAPI
from meta import (PROJECT_NAME, PROJECT_VERSION)
from fastapi.staticfiles import StaticFiles
from api import index

API = FastAPI(title=PROJECT_NAME, version=PROJECT_VERSION)
API.mount("/static", StaticFiles(directory="res"), name="static")
API.include_router(index.api)