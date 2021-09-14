from aiohttp.web import Request, Response
from aiohttp.web import json_response


async def handle_tests(request: Request) -> Response:
    """
    Тест, что работает вервис
    """
    return json_response(data={'message': 'It works!'}, headers=request.app['cors'])
