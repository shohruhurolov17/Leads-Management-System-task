from environs import Env

env = Env()
env.read_env('.env')

CELERY_BROKER_URL = env.str('CELERY_BROKER_URL')
result_backend = env.str('CELERY_RESULT_BACKEND')
timezone = env.str('CELERY_TIMEZONE')
