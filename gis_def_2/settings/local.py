from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
local_env =open(os.path.join(BASE_DIR, '.env'))
env_list = dict()

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env_list['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CELERY_BROKER_URL = "amqp://guest@3.144.196.207:5672"