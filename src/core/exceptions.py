from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    async def http_error_handler(request: Request, exc: HTTPException) -> JSONResponse:
        """Формат тела ошибки. TODO поменять под требования олимпиады"""

        return JSONResponse(status_code=exc.status_code, content={"reason": exc.detail})
