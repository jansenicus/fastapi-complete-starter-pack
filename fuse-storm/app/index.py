from fastapi import Depends, FastAPI
from .users import auth_backend, current_active_user, fastapi_users
from .db import DATABASE_URL
from .models import UserDB
from tortoise.contrib.fastapi import register_tortoise


api = FastAPI(title='FastAPI with User Management')

@api.get('/')
async def homepage():
    return "Hello world..."

api.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    prefix="/auth/jwt", 
    tags=["auth"]
)
api.include_router(
    fastapi_users.get_register_router(), 
    prefix="/auth", 
    tags=["auth"])
api.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"]
    )
api.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"]
    )
api.include_router(
    fastapi_users.get_users_router(), 
    prefix="/users", 
    tags=["users"]
    )


@api.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


register_tortoise(
    api,
    db_url=DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=True,
)
