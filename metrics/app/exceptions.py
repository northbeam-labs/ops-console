from fastapi import Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    def __init__(self, status: int, detail: str):
        self.status, self.detail = status, detail


async def app_error_handler(_: Request, exc: AppError):
    return JSONResponse(status_code=exc.status, content={"detail": exc.detail})
