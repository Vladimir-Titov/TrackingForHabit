from os import urandom
from typing import Optional

import aiohttp_auth
import asyncpg
from aiohttp import web
from aiohttp_auth.auth import CookieTktAuthentication

from config import dsn
from habit import index, login, register, views_profile


class App(web.Application):
    pool: Optional[asyncpg.pool.Pool] = None
    policy: CookieTktAuthentication = CookieTktAuthentication(urandom(32), 60, include_ip=True)

    __routes = [web.get('/', index),
                web.get('/login', login),
                web.post('/login', login),
                web.get('/register', register),
                web.post('/register', register),
                web.get('/users/{users_id}', views_profile)]

    def _setup_routes(self):
        self.add_routes(self.__routes)

    async def _init_pg(self, *args):
        self.pool = await asyncpg.create_pool(dsn)

    async def _close_pg(self, *args):
        await self.pool.close()

    def create_server(self, *args):
        aiohttp_auth.auth.setup(self, self.policy)
        self._setup_routes()
        self.on_startup.append(self._init_pg)
        self.on_shutdown.append(self._close_pg)
