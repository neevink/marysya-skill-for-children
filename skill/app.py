import os
import yaml

from aiohttp import web
from handlers.options import handle_options
from handlers.skill import handle_skill
from handlers.test import handle_tests

from skill.entities.number_mapper import NumberMapper
from skill.entities.path import Direction

from middleware import error_middleware


def prepare_strings(original: list) -> dict:
    ans = {}
    for element in original:
        ans[element['name']] = element['texts']
    return ans


def prepare_paths(original: list) -> dict:
    ans = {}
    for element in original:
        path = []
        for e in element['path']:
            p = e.split()
            path.append((Direction[p[0]], int(p[1])))

        ans[int(element['id'])] = {
            'name': element['name'],
            'margin_horizontal': element['margin_horizontal'],
            'margin_vertical': element['margin_vertical'],
            'path': path,
            'id': int(element['id'])
        }
    return ans


def create_app() -> web.Application:
    app = web.Application(middlewares=[error_middleware])
    app.add_routes([
        web.options('/skill', handle_options),
        web.post('/skill', handle_skill),
        web.get('/test', handle_tests)
    ])

    app['cors'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': '*',
    }

    # Загружаем фразы, которые говорит Маруся
    strings_path = os.path.join(os.path.dirname(__file__), 'resources', 'strings.yml')
    with open(strings_path, 'r', encoding='utf8') as strings:
        app['strings'] = prepare_strings(yaml.safe_load(strings)['strings'])

    # Загружаем пути, по которым можно нарисовать рисунки
    paths_path = os.path.join(os.path.dirname(__file__), 'resources', 'paths.yml')
    with open(paths_path, 'r', encoding='utf8') as paths:
        app['paths'] = prepare_paths(yaml.safe_load(paths)['paths'])

    # Часто используемые между запросами переменные
    app['mapper'] = NumberMapper()
    app['next-phrases'] = set(app['strings']['next'])
    app['random'] = set(app['strings']['random'])
    app['want-select'] = set(app['strings']['want-select'])
    app['figures'] = ''.join(['{} - {}, '.format(e['id'], e['name']) for e in list(app['paths'].values())])

    return app


