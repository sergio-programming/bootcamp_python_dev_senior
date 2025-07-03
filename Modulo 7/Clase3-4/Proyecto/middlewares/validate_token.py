from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import requests, HTTPException, status
from fastapi.responses import JSONResponse

class ValidateTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path.startswith("/admin"):
            token = request.headers.get("Authorization")
            if token is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token requerido"
                )
        return await call_next(request)