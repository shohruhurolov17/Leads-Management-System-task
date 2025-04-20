from environs import Env

env = Env()

env.read_env('.env')


EMAIL_BACKEND = env.str('EMAIL_BACKEND')
EMAIL_HOST = env.str('EMAIL_HOST') 
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')