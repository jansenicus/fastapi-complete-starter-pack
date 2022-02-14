from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi_mail import (FastMail, MessageSchema)
from lib.mail import mailconfig, EmailSchema


api = APIRouter()


@api.post("/sendmail", include_in_schema=True)
async def send_mail(mail: EmailSchema) -> JSONResponse:

    message = MessageSchema(
        subject=mail.dict().get("subject"),
        recipients=mail.dict().get("recipients"),
        template_body=mail.dict().get("body"),
    )

    fm = FastMail(mailconfig)
    await fm.send_message(message, template_name="mail.html")
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
