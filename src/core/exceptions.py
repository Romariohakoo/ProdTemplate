from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


def register_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_error_handler(request, exc):
        """Формат тела ошибки. TODO поменять под требования олимпиады"""

        return JSONResponse(status_code=exc.status_code, content={"reason": exc.detail})
