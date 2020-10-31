from aiohttp import web
from aiohttp_auth import auth

from habit.auth import Users
from habit.db import Database


async def index(request: web.Request) -> None:
    raise web.HTTPFound('/login')


async def login(request: web.Request) -> None:
    if request.method == 'POST':
        payload = Users(only=('username', 'password')).load(await request.post())
        user = await Database(request).check_user(**payload)
        if user is not None:
            await auth.remember(request, str(user[0]['users_id']).encode())
            raise web.HTTPFound(f'/users/{user[0]["users_id"]}')
        raise web.HTTPUnauthorized()


async def register(request: web.Request) -> web.json_response:
    payload = Users(only=('username', 'password', 'email')).load(await request.post())
    users_id = await Database(request).add_user(**payload)
    return web.json_response(Users().dump(users_id, many=True))


@auth.auth_required
async def views_profile(request: web.Request):
    _id = request.match_info['users_id']
    users_id = Users(only=('users_id',)).load({'users_id': _id}, partial=True)
    data = await Database(request).view_user(users_id['users_id'])
    response = Users().dump(data, many=True)
    return web.json_response(response)
