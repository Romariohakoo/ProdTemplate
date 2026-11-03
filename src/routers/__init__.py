from fastapi import APIRouter

from src.routers import ping

api_router = APIRouter(prefix="/api")
api_router.include_router(ping.router)
# Новые роутеры подключать здесь