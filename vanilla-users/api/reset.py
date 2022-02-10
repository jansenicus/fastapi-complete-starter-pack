from . import *

@api.get("/auth/reset-password")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("reset.html", context = {"request":request, "style": style})