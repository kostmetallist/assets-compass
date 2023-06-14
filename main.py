from fastapi import FastAPI


app = FastAPI(
    title='Assets Compass'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Roger'},
    {'id': 2, 'role': 'moderator', 'name': 'Mike'},
    {'id': 3, 'role': 'associate', 'name': 'Ferdinand'},
]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    existing = [user for user in fake_users if user['id'] == user_id][0]
    existing['name'] = new_name
    return {'status': 'OK'}


fake_trades = [
    {'id': 1, 'user_id': 3, 'currency_code': 'BTC', 'operation': 'buy', 'price': 123.45, 'amount': 42},
    {'id': 2, 'user_id': 3, 'currency_code': 'BTC', 'operation': 'sell', 'price': 125.88, 'amount': 40},
]


@app.get('/trades')
def get_trades(limit: int, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.get('/')
def hello():
    return 'hello world'
