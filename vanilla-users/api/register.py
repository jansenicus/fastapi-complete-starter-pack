from . import *

@api.get("/auth/register")
async def home(request: Request):
	return html.TemplateResponse("register.html", context = {"request":request})