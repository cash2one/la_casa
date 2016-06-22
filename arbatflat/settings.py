import os
from the_cottage.settings import *

ALLOWED_HOSTS = ['test.arbatflat.com', 'www.test.arbatflat.com']

ROOT_URLCONF = 'arbatflat.urls'

WSGI_APPLICATION = 'arbatflat.wsgi.application'

STATIC_ROOT = os.environ.get('ARBATFLAT_STATIC_ROOT')
