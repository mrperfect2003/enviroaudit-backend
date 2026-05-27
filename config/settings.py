from pathlib import Path
import os
from dotenv import load_dotenv

# -----------------------------------------
# Load Environment Variables
# -----------------------------------------

load_dotenv()

# -----------------------------------------
# Base Directory
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# Security
# -----------------------------------------

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-development-secret-key"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"

ALLOWED_HOSTS = ["*"]

# -----------------------------------------
# Installed Applications
# -----------------------------------------

INSTALLED_APPS = [

    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third Party Apps
    "corsheaders",
    "rest_framework",

    # Local Apps
    "apps.organizations",
    "apps.ingestion",
    "apps.normalization",
    "apps.review",
    "apps.audit",
]

# -----------------------------------------
# Middleware
# -----------------------------------------

MIDDLEWARE = [

    # CORS Middleware
    "corsheaders.middleware.CorsMiddleware",

    # Django Middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -----------------------------------------
# URL Configuration
# -----------------------------------------

ROOT_URLCONF = "config.urls"

# -----------------------------------------
# Templates
# -----------------------------------------

TEMPLATES = [
    {
        "BACKEND":
        "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -----------------------------------------
# WSGI
# -----------------------------------------

WSGI_APPLICATION = "config.wsgi.application"

# -----------------------------------------
# Database
# -----------------------------------------

DATABASES = {
    "default": {
        "ENGINE":
        "django.db.backends.sqlite3",

        "NAME":
        BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------------------
# Password Validation
# -----------------------------------------

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },

    {
        "NAME":
        (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },

    {
        "NAME":
        (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },

    {
        "NAME":
        (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# -----------------------------------------
# Internationalization
# -----------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# -----------------------------------------
# Static Files
# -----------------------------------------

STATIC_URL = "/static/"

# -----------------------------------------
# Media Files
# -----------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------------------
# Default Auto Field
# -----------------------------------------

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)

# -----------------------------------------
# Django REST Framework
# -----------------------------------------

REST_FRAMEWORK = {

    "DEFAULT_PAGINATION_CLASS":
    "core.pagination.DefaultPagination",

    "PAGE_SIZE": 10,
}

# -----------------------------------------
# CORS Configuration
# -----------------------------------------

CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

    "https://enviroaudit.vercel.app",
]