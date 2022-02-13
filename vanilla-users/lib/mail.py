from fastapi_mail import ConnectionConfig
from path import Path
from pydantic import (EmailStr, BaseModel)
from typing import (List, Dict, Any)


mailconfig = ConnectionConfig(
    MAIL_USERNAME = "superadmin@example.com",
    MAIL_PASSWORD = "SUPER_SECRET_PASSWORD",
    MAIL_FROM = "superadmin@example.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Super Administrator",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER = Path(__file__).parent.parent / 'html',

)

class EmailSchema(BaseModel):
    subject: str
    recipients: List[EmailStr]
    body: Dict[str, Any]