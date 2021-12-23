from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',          # 서비스이름
        'PORT': '3306',             # mariadb 기본값
    }
}