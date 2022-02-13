from fastapi_mail import ConnectionConfig
from pydantic import (EmailStr, BaseModel)
from typing import (List, Dict, Any)
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path('lib/mail.conf'))

mailconfig = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_FROM = os.getenv('MAIL_FROM'),
    MAIL_PORT = os.getenv('MAIL_PORT'),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
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
