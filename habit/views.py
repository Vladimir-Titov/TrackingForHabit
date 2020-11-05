from aiohttp import web

from habit.auth import Users, Habit
from habit.db import Database


async def login(request: web.Request) -> None:
    if request.method == 'POST':
        payload = Users(only=('username', 'password')).load(await request.post())
        user = await Database(request).authorized_user(**payload)
        if not user:
            raise web.HTTPUnauthorized()
        return web.HTTPFound(f'users/{user[0]["user_id"]}')


async def register(request: web.Request) -> web.json_response:
    payload = Users(only=('username', 'password', 'email')).load(await request.post())
    users_id = await Database(request).add_user(**payload)
    return web.json_response(Users().dump(users_id, many=True))


async def views_profile(request: web.Request) -> web.json_response:
    _id = request.match_info.get('user_id', None)
    if _id is None:
        data = await Database(request).view_user(user_id=_id)
    else:
        user_id = Users(only=('user_id',)).load({'user_id': _id}, partial=True)
        data = await Database(request).view_user(user_id['user_id'])
    response = Users().dump(data, many=True)
    return web.json_response(response)



