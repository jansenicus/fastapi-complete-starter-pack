from fastapi import FastAPI
from core.config import settings
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from apis.general_pages.route_homepage import general_pages_router


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(general_pages_router)
