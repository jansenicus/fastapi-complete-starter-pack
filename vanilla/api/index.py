from . import *

@api.get("/")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("index.html", context = {"request":request, "style": style})