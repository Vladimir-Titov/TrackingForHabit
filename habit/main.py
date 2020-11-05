from aiohttp import web
from habit.middlewares import exception_middleware
from habit.app import App

app = App(middlewares=[exception_middleware])

app.create_server()
web.run_app(app)
