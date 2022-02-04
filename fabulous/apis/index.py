from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="dynamic")

index = APIRouter()


@index.get("/")
async def home(request: Request, style: str = 'default'):
	return templates.TemplateResponse("index.html", context = {"request":request, "style": style})


@index.get("/login")
async def home(request: Request, style: str = 'default'):
	return templates.TemplateResponse("login.html", context = {"request":request, "style": style})