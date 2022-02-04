from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import api as api

app = FastAPI()
app.mount("/res", StaticFiles(directory="res"), name="res")


app.include_router(api.index)
app.include_router(api.login)