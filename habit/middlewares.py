from typing import Callable, Union

from aiohttp import web
from asyncpg.exceptions import UniqueViolationError
from marshmallow.exceptions import ValidationError


@web.middleware
async def exception_middleware(request: web.Request, handler: Callable) -> Union[Callable, None]:
    try:
        return await handler(request)
    except (ValidationError, ValueError, TypeError):
        raise web.HTTPBadRequest()
    except UniqueViolationError:
        raise web.HTTPBadRequest(reason='Non Unique username or email')


