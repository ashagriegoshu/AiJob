from .base import *  # noqa: F403,F401

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# django-debug-toolbar
if 'debug_toolbar' not in INSTALLED_APPS:  # noqa: F405
    INSTALLED_APPS += ['debug_toolbar']  # noqa: F405

if 'debug_toolbar.middleware.DebugToolbarMiddleware' not in MIDDLEWARE:  # noqa: F405
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa: F405

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Stop debug toolbar from pausing every redirect
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}