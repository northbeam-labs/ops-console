import time
from starlette.middleware.base import BaseHTTPMiddleware


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        resp = await call_next(request)
        resp.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}"
        return resp
