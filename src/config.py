import os
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

DB_TEST_USER = os.environ.get('DB_TEST_USER')
DB_TEST_PASS = os.environ.get('DB_TEST_PASS')
DB_TEST_HOST = os.environ.get('DB_TEST_HOST')
DB_TEST_PORT = os.environ.get('DB_TEST_PORT')
DB_TEST_NAME = os.environ.get('DB_TEST_NAME')

JWT_SECRET = os.environ.get('JWT_SECRET')
USER_MANAGER_SECRET = os.environ.get('USER_MANAGER_SECRET')

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
