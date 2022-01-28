from fastapi import FastAPI
from core.settings import config
from fastapi.staticfiles import StaticFiles
from apis.pages.index import index

app = FastAPI(title=config.PROJECT_NAME, version=config.PROJECT_VERSION)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index)