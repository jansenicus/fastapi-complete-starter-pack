from . import *

@api.get("/auth/jwt/login")
async def home(request: Request, style: str = 'default'):
	return html.TemplateResponse("login.html", context = {"request":request})