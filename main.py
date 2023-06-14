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


@app.get('/')
def hello():
    return 'hello world'
