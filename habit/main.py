from aiohttp import web
from habit.app import App


app = App()
app.create_server()
web.run_app(app)
