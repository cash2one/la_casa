import os
from the_cottage.settings import *

ALLOWED_HOSTS = ['www.arbatflat.com']

ROOT_URLCONF = 'arbatflat.urls'

WSGI_APPLICATION = 'arbatflat.wsgi.application'

STATIC_ROOT = os.environ.get('ARBATFLAT_STATIC_ROOT')

DEBUG = False

