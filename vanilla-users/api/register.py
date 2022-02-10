from . import *

@api.get("/auth/register")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("register.html", context = {"request":request, "style": style})