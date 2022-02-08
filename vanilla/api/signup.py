from . import *

@api.get("/signup")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("signup.html", context = {"request":request, "style": style})