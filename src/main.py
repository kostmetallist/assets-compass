from enum import Enum
from datetime import datetime
from time import sleep
from typing import List, Optional

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel, Field
from redis import asyncio as aioredis

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead
from src.operations.router import router as router_operations

APP_NAME = 'Assets Compass'


app = FastAPI(
    title=APP_NAME
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth']
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth']
)

app.include_router(router_operations)


@app.on_event('startup')
async def startup_event_handler():
    redis = aioredis.from_url('redis://localhost', encoding='utf8')
    FastAPICache.init(RedisBackend(redis), prefix=f'{APP_NAME.lower().replace(' ', '-')}-$')


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            'details': exc.errors()
        })
    )


class Rank(Enum):
    rookie = 'rookie'
    expert = 'expert'


class Degree(BaseModel):
    rank: Rank
    date_approval: datetime


class FakeUser(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[Degree]


fake_users = [
    {
        'id': 1,
        'role': 'admin',
        'name': 'Roger',
        'degree': {
            'rank': Rank.expert,
            'date_approval': datetime(year=2020, month=2, day=11),
        },
    },
    {
        'id': 2,
        'role': 'moderator',
        'name': 'Mike',
    },
    {
        'id': 3,
        'role': 'associate',
        'name': 'Ferdinand',
        'degree': {
            'rank': Rank.rookie,
            'date_approval': datetime.utcnow(),
        },
    },
]


current_user = fastapi_users.current_user()


@app.get('/users/{user_id}', response_model=List[FakeUser])
def get_user(user_id: int, cur_user: User = Depends(current_user)):
    return [user for user in fake_users if user['id'] == user_id]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str, cur_user: User = Depends(current_user)):
    existing = [user for user in fake_users if user['id'] == user_id][0]
    existing['name'] = new_name
    return {'status': 'OK'}


class Trade(BaseModel):
    id: int
    user_id: int
    currency_code: str = Field(max_length=5)
    operation: str
    price: float = Field(ge=0)
    amount: int


fake_trades = [
    {'id': 1, 'user_id': 3, 'currency_code': 'BTC', 'operation': 'buy', 'price': 123.45, 'amount': 42},
    {'id': 2, 'user_id': 3, 'currency_code': 'BTC', 'operation': 'sell', 'price': 125.88, 'amount': 40},
]


@app.get('/trades')
def get_trades(limit: int, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {
        'status': 200,
        'data': trades
    }


@app.get('/')
@cache(expire=15)
def hello():
    # Emulating long operation
    sleep(2)
    return 'hello world'
