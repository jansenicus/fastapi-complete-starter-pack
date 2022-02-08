from . import *

@api.get("/login")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("login.html", context = {"request":request, "style": style})