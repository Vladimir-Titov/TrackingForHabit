import asyncpg
from aiohttp import web

from habit.auth import generate_password_hash


class Database:

    def __init__(self, request: web.Request):
        self.request = request

    async def __context_manager(self, query, *args):
        async with self.request.app.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def add_user(self, username: str, password: str, email: str) -> asyncpg.Record:
        query = 'INSERT INTO users (username, password, email) ' \
                'VALUES ($1, $2, $3) ' \
                'RETURNING users_id'
        password_hash = generate_password_hash(password)
        return await self.__context_manager(query, username, password_hash, email)

    async def check_user(self, username: str, password: str) -> asyncpg.Record:
        query = 'SELECT users_id FROM users WHERE username=$1 and password=$2'
        password_hash = generate_password_hash(password)
        return await self.__context_manager(query, username, password_hash)

    async def view_user(self, users_id: int) -> asyncpg.Record:
        query = 'SELECT * FROM users WHERE users_id=$1'
        return await self.__context_manager(query, users_id)
