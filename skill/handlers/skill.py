import random

from aiohttp.web import Request, Response, json_response
from skill.entities.skill_response import SkillResponse
from skill.entities.state import State
from skill.entities.number_mapper import NumberMapper
from random import choice


async def handle_skill(request: Request) -> Response:
    """
    Запрос к скиллу
    """
    # http://localhost:7845/skill
    print(await request.text())

    mapper = NumberMapper()

    request_json = await request.json()

    resp = SkillResponse(request_json)

    if resp.is_start:
        # Если начало
        resp.answer = request.app['strings']['hello']
        resp.state = State.START
    elif resp.state == State.START:
        # Парсим ответ, что хочет пользователь
        if 'выбрать' in resp.get_user_input():
            resp.answer = 'Выбери число от 1 до {}'.format(len(request.app['paths']))
            resp.state = State.SELECT_FIGURE
        elif 'случайная' in resp.get_user_input():
            s = set(range(1, len(request.app['paths']) + 1)) - set(resp.passed)
            id = choice(list(s))
            print(id)
            resp.answer = 'Выбрана ' + str(id) + ' это ' + request.app['paths'][id]['name']

            resp.state = State.PREPARING
            resp.current_path = id
            resp.current_step = 0
        else:
            resp.answer = 'Я тебя не поняла'

    elif resp.state == State.SELECT_FIGURE:
        # Если мы решили выбрать фигуру
        tokens = resp.get_user_input()
        for token in tokens:
            if mapper[token] is not None:
                id = mapper[token]
                resp.answer = 'Выбрано ' + str(id) + request.app['paths'][id]['name'] + ' скажи "дальше", когда буш готов'

                resp.state = State.PREPARING
                resp.current_path = id
                resp.current_step = -1
                return json_response(resp.get_json_response(), headers=request.app['cors'])
        resp.answer = 'Просто скажи число'

    elif resp.state == State.PREPARING:
        if 'дальше' in resp.get_user_input():
            resp.answer = 'Отлично, теперь отступи на {} клетки вниз и на {} вправо'.format(
                request.app['paths'][resp.current_path]['margin_vertical'],
                request.app['paths'][resp.current_path]['margin_horizontal']
            )

            resp.state = State.DRAWING
            resp.current_step = 0
        else:
            resp.answer = 'Если готов, то скажи "дальше"'

    elif resp.state == State.DRAWING:
        if 'дальше' in resp.get_user_input():
            if resp.current_step >= len(request.app['paths'][resp.current_path]['path']):
                resp.answer = 'Поздравляю, ты нарисовал рисунок. Что у тебя получилось?'
                resp.state = State.FINISH
                resp.passed.append(resp.current_path)
            else:
                step = resp.current_step
                print(step)
                print(request.app['paths'][resp.current_path]['path'])
                s = request.app['paths'][resp.current_path]['path'][step]
                resp.answer = f'Нарисуй линию на {s[1]} клеток {s[0]}'
                resp.current_step = step + 1
        else:
            resp.answer = 'Если готов, то скажи "дальше"'

    elif resp.state == State.FINISH:
        resp.answer = 'Красава, ты нарисовал хрегь'
    else:
        resp.answer = 'Продолжение...'

    return json_response(resp.get_json_response(), headers=request.app['cors'])
