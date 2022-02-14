from fastapi import Depends, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_max_age=3600)


api = APIRouter()

from lib.db import DATABASE_URL
from lib.models import UserDB
from lib.users import auth_backend, current_active_user, fastapi_users

api.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    prefix="/auth/jwt", tags=["auth"]
)
api.include_router(
    fastapi_users.get_register_router(), 
    prefix="/auth", tags=["auth"])

api.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_users_router(), 
    prefix="/users", tags=["users"])


@api.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


register_tortoise(
    api,
    db_url=DATABASE_URL,
    modules={"models": ["lib.models"]},
    generate_schemas=True,
)
