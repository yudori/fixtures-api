from config.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x62r-degmcl^bf3ed5*0=ylzl3$-r8y7ym8-9j^o2=e5#iyik)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
