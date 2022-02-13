from . import *

@api.get("/")
async def home(request: Request):
	return html.TemplateResponse("index.html", context = {"request":request})