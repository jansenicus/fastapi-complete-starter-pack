from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="api")

#------------------------
# to be edited
from .index import index
from .login import login
from .signup import signup



