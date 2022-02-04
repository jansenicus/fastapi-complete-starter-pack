from . import *

login = APIRouter()

@login.get("/login")
async def home(request: Request, style: str = 'default'):
	return templates.TemplateResponse("login.html", context = {"request":request, "style": style})