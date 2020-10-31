from os import urandom

from aiohttp import web
from aiohttp_auth.auth import auth_middleware, CookieTktAuthentication

from habit.app import App

policy: CookieTktAuthentication = CookieTktAuthentication(urandom(32), 60, include_ip=True)
app = App(middlewares=[auth_middleware(policy)])
app.create_server()
web.run_app(app)
