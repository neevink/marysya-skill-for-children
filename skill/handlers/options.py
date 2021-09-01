from aiohttp.web import Request, Response


async def handle_options(request: Request) -> Response:
    """
    Маруся делает перед началом работы делает OPTIONS запрос,
    на который обязательно нужно ответить
    """
    return Response(status=201, headers=request.app['cors'])
