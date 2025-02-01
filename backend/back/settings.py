import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")


ALLOWED_HOSTS = ["*", "localhost"]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
]


CORS_ALLOW_HEADERS = [
    "accept",
    "referer",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-sessionid",
    "x-requested-with",
    "access",
    "refresh",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
]
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "database",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "back.wsgi.application"

X_FRAME_OPTIONS = "SAMEORIGIN"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "ru"

LANGUAGES = [
    ("ky", _("Киргизский")),
    ("ru", _("Русский")),
    ("tg", _("Таджитский")),
    ("uz", _("Узбекский")),
]

TIME_ZONE = "Asia/Yekaterinburg"

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]


"""
STATIC
"""
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


"""
MEDIA SETTINGS
"""
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JAZZMIN_SETTINGS = {
    "language_chooser": True,
}

"""
TELEGRAM
"""
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

ADMIN_TG_ID = os.getenv("ADMIN_TG_ID")

API_VERSION = os.getenv("API_VERSION")


"""
REDIS SETTINGS
"""
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)


"""
CELERY SETTINGS
"""

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"


CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
