from aiohttp import web
from app import create_app


HOST = '0.0.0.0'
PORT = 7845

if __name__ == '__main__':
    app = create_app()
    web.run_app(app, host=HOST, port=PORT)
