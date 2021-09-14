from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
import logging


@middleware
async def error_middleware(request: Request, handler):
    try:
        return await handler(request)
    except Exception as exc:
        print(exc)
