# flake8: noqa
from .settings import *

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]
ALLOWED_HOSTS = ["backend", "localhost", "127.0.0.1", "0.0.0.0"]

MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CELERY_TASK_ALWAYS_EAGER = (
#     True
# )  # Use this to run tasks synchronously in the main thread to make debugging easier
