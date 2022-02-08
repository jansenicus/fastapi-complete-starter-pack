from fastapi import (APIRouter, Request)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

html = Jinja2Templates(directory="html")

api = APIRouter()