from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as user_router
from .post import router as post_router

main_router = APIRouter()

main_router.include_router(user_router, prefix="/users", tags=["users"])
main_router.include_router(post_router, prefix="/posts", tags=["posts"])
main_router.include_router(auth_router, tags=["auth"])
