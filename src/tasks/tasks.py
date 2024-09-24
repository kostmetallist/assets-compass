import time

from celery import Celery

from src.config import REDIS_PORT

celery = Celery('bg-tasks', broker=f'redis://localhost:{REDIS_PORT}')


@celery.task
def generate_digest(username: str):
    print(f'Starting digest generation for {username}...')
    time.sleep(2)
    print(f'Done generation for {username}!')
