from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import (index, auth, login, register, reset, mail)
from fastapi.middleware.cors import CORSMiddleware


API = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

API.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
API.mount("/res", StaticFiles(directory="res"), name="res")
API.include_router(index.api)
API.include_router(auth.api)
API.include_router(login.api)
API.include_router(register.api)
API.include_router(reset.api)
API.include_router(mail.api)



