# FILE: /fastapi-jwt-app/fastapi-jwt-app/app/auth/__init__.py
from fastapi import APIRouter

router = APIRouter()

from .routers import router as auth_router

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])