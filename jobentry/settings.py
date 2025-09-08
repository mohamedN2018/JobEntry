import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _

# =========================
# BASE & SECURITY
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('MY_SECRET_KEY')
DEBUG = True

MAIN_DOMAIN = config('MAIN_DOMAIN', default='localhost')

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_WHITELIST = ["*"]

CSRF_TRUSTED_ORIGINS = [
    f"{MAIN_DOMAIN}",
]
# CSRF_COOKIE_DOMAIN = MAIN_DOMAIN
# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'jobentry.urls'

# =========================
# URLS & WSGI
# =========================
ROOT_URLCONF = 'jobentry.urls'

WSGI_APPLICATION = 'jobentry.wsgi.application'


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # استخدم BASE_DIR بدل os.path.join
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('ar', _('Arabic')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# =========================
# STATIC & MEDIA
# =========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/usr/src/app/static/",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     "/usr/src/app/static/",
# ]
# STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# DEFAULT SETTINGS
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# =========================
# EMAIL
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'moh24832@gmail.com'
EMAIL_HOST_PASSWORD = 'yfvmxzmccwjwukjd'
EMAIL_USE_TLS = True
EMAIL_PORT = 587  # خليه رقم مش نص

# =========================
# JAZZMIN CONFIG
# =========================
JAZZMIN_SETTINGS = {
    "site_title": "Vera Admin",
    "site_header": "Vera",
    "site_brand": "Vera",
    "site_logo": "/assets/img/logo.jpg",
    "login_logo": "/assets/img/logo.jpg",
    "login_logo_dark": "/assets/img/logo.jpg",
    "site_logo_classes": "img-circle",
    "site_icon": "/assets/img/logo.jpg",
    "welcome_sign": "Welcome to the Vera",
    "copyright": "Vera",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "books"},
    ],

    "usermenu_links": [
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": False,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": True,
}
