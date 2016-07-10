import os
from the_cottage.settings import *

ALLOWED_HOSTS = ['www.naracottage.com']

ROOT_URLCONF = 'naracottage.urls'

WSGI_APPLICATION = 'naracottage.wsgi.application'

STATIC_ROOT = os.environ.get('NARACOTTAGE_STATIC_ROOT')

DEBUG = False

