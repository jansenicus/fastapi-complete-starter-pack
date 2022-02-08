from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import (index, login, signup)

API = FastAPI()
API.mount("/res", StaticFiles(directory="res"), name="res")
API.include_router(index.api)
API.include_router(login.api)
API.include_router(signup.api)