from aiohttp import web


async def index(request: web.Request) -> web.json_response:
    return web.json_response({'hello': 'World!!'})



