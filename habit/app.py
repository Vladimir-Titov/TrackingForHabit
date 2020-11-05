from typing import Optional

import asyncpg
from aiohttp import web

from config import dsn
from habit import login, register, views_profile


class App(web.Application):
    pool: Optional[asyncpg.pool.Pool] = None

    __routes = [web.get('/login', login),
                web.post('/login', login),
                web.post('/users', register),
                web.get('/users', views_profile),
                web.get('/users/{user_id}', views_profile),
                ]

    def _setup_routes(self) -> None:
        self.add_routes(self.__routes)

    async def _init_pg(self, *args) -> None:
        self.pool = await asyncpg.create_pool(dsn)

    async def _close_pg(self, *args) -> None:
        await self.pool.close()

    def create_server(self, *args) -> None:
        self._setup_routes()
        self.on_startup.append(self._init_pg)
        self.on_shutdown.append(self._close_pg)
