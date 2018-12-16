from config.settings.base import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

import django_heroku
django_heroku.settings(locals())

ALLOWED_HOSTS = ['*']
