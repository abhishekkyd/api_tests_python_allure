from . import env

BASE_URL = env.get(key='BASE_URL', default="https://gorest.co.in")
VERIFY_SSL = env.get_bool(key='VERIFY_SSL', default=True)
