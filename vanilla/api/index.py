from . import *

index = APIRouter()

@index.get("/")
async def home(request: Request, style: str = 'default'):
	return templates.TemplateResponse("index.html", context = {"request":request, "style": style})