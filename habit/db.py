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
                'RETURNING user_id;'
        password_hash = generate_password_hash(password)
        return await self.__context_manager(query, username, password_hash, email)

    async def authorized_user(self, username: str, password: str) -> asyncpg.Record:
        query = 'SELECT user_id FROM users WHERE username=$1 and password=$2;'
        password_hash = generate_password_hash(password)
        return await self.__context_manager(query, username, password_hash)

    async def view_user(self, user_id: int = None) -> asyncpg.Record:
        query = 'SELECT user_id, email, username FROM users WHERE ($1::integer IS NULL or $1=user_id);'
        return await self.__context_manager(query, user_id)
