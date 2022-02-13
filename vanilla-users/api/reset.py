from . import *

@api.get("/auth/reset-password")
async def home(request: Request):
	return html.TemplateResponse("reset.html", context = {"request":request})