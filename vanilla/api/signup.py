from . import *

signup = APIRouter()

@login.get("/signup")
async def home(request: Request, style: str = 'default'):
	return templates.TemplateResponse("signup.html", context = {"request":request, "style": style})