import uvicorn
from fastapi import FastAPI

from src.core.config import settings
from src.core.exceptions import register_exception_handlers
from src.routers import api_router


def create_app():
    app = FastAPI(title="ProdTemplate")
    register_exception_handlers(app)
    app.include_router(api_router)
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.server_port)
