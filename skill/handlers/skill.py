from aiohttp.web import Request, Response, json_response
from skill.entities.skill_response import SkillResponse
from skill.entities.state import State

from skill.helpers import cells_count

from random import choice


async def handle_skill(request: Request) -> Response:
    """
    Запрос к скиллу
    """
    resp = SkillResponse(await request.json())

    if resp.is_start:
        # Если начало
        resp.answer = request.app['strings']['hello'][0]
        resp.state = State.START
    elif resp.state == State.START:
        # Парсим ответ, что хочет пользователь
        user_input_set = set(resp.get_user_input())
        if len(request.app['want-select'] & user_input_set) > 0:
            resp.answer = request.app['strings']['select'][0].format(len(request.app['paths'])) + \
                '. \n' + request.app['figures']

            resp.state = State.SELECT_FIGURE
        elif len(request.app['random'] & user_input_set) > 0:
            s = set(range(1, len(request.app['paths']) + 1)) - set(resp.passed)
            path_id = choice(list(s))
            resp.answer = request.app['strings']['selected'][0].format(
                path_id,
                request.app['paths'][path_id]['name']
            )

            resp.state = State.PREPARING
            resp.current_path = path_id
            resp.current_step = 0
        else:
            resp.answer = request.app['strings']['repeat'][0]

    elif resp.state == State.SELECT_FIGURE:
        # Если мы решили выбрать фигуру
        tokens = resp.get_user_input()
        for token in tokens:
            path_id = request.app['mapper'][token]
            if path_id is not None:
                resp.answer = request.app['strings']['selected'][0].format(
                    path_id,
                    request.app['paths'][path_id]['name']
                )
                resp.state = State.PREPARING
                resp.current_path = path_id
                resp.current_step = -1
                return json_response(resp.get_json_response(), headers=request.app['cors'])
        resp.answer = 'Просто назови число'

    elif resp.state == State.PREPARING:
        if len(request.app['next-phrases'] & set(resp.get_user_input())) > 0:
            resp.answer = request.app['strings']['prepare'][0].format(
                cells_count(request.app['paths'][resp.current_path]['margin_vertical']),
                cells_count(request.app['paths'][resp.current_path]['margin_horizontal'])
            )

            resp.state = State.DRAWING
            resp.current_step = 0
        else:
            resp.answer = choice(request.app['strings']['say-next'])

    elif resp.state == State.DRAWING:
        if len(request.app['next-phrases'] & set(resp.get_user_input())) > 0:
            if resp.current_step >= len(request.app['paths'][resp.current_path]['path']):
                resp.answer = choice(request.app['strings']['congrats'])
                resp.state = State.FINISH
                resp.passed.append(resp.current_path)

                if len(resp.passed) >= len(request.app['paths']):
                    # Если нарисованы все рисунки, то обнуляем нарисованные рисунки
                    resp.passed = [resp.current_path]

            else:
                step = resp.current_step
                s = request.app['paths'][resp.current_path]['path'][step]
                resp.answer = choice(request.app['strings']['draw']).format(
                    cells_count(s[1]),
                    s[0].value
                )
                resp.current_step = step + 1
        else:
            resp.answer = choice(request.app['strings']['say-next'])

    elif resp.state == State.FINISH:
        correct_answer = request.app['paths'][resp.current_path]['name']
        # Тут проверка, что ребёнок угадал фигуру и снова запрос на рисование рисунка
        if correct_answer in resp.get_user_input():
            resp.answer = choice(request.app['strings']['correct']).format(correct_answer)
        else:
            resp.answer = choice(request.app['strings']['wrong']).format(correct_answer)

        resp.answer += choice(request.app['strings']['what-want'])
        resp.state = State.START
        resp.current_path = None
        resp.current_step = None
    else:
        resp.answer = request.app['strings']['undefined']

    return json_response(resp.get_json_response(), headers=request.app['cors'])
