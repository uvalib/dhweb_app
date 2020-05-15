"""
Django settings for dhweb project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DH_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_STATUS") == "True"

ALLOWED_HOSTS = ["localhost", os.environ.get("ALLOWED_HOSTS")]

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}


# Application definition

INSTALLED_APPS = [
    "abstracts.apps.AbstractsConfig",
    "dal",
    "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.flatpages",
    "django.contrib.postgres",
    "django.contrib.sites",
    "django.contrib.redirects",
    "django.contrib.sitemaps",
    "crispy_forms",
    "django.contrib.humanize",
    "easy_thumbnails",
    "filer",
    "mptt",
    "markdownify",
    "debug_toolbar",
    "compressor",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
]

ROOT_URLCONF = "dhweb.urls"

SITE_ID = 1

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
            "debug": DEBUG,
        },
    }
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

WSGI_APPLICATION = "dhweb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": "postgres",
        "PORT": 5432,
    }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "memcached:11211",
        "TIMEOUT": 60 * 5,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 10},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "/vol/static_files"
LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/"

DATA_OUTPUT_PATH = "/vol/data"

DENORMALIZED_WORKS_NAME = "dh_conferences_works"

DENORMALIZED_HEADERS = [
    {"name": "work_id", "description": "Unique ID number", "required": True},
    {"name": "conference_label", "description": "Conference label", "required": True},
    {
        "name": "conference_short_title",
        "description": "Location-based short title of the conference",
        "required": False,
    },
    {
        "name": "conference_theme_title",
        "description": "Thematic conference title",
        "required": False,
    },
    {"name": "conference_year", "description": "", "required": True},
    {
        "name": "conference_organizers",
        "description": "Conference organizing groups (Separated by semicolon)",
        "required": False,
    },
    {
        "name": "conference_series",
        "description": "Conference series (separated by semicolon)",
        "required": False,
    },
    {
        "name": "conference_hosting_institutions",
        "description": "Hosting institutions (separated by a semicolon)",
        "required": False,
    },
    {"name": "conference_city", "description": "", "required": False},
    {"name": "conference_state", "description": "", "required": False},
    {"name": "conference_country", "description": "", "required": False},
    {
        "name": "conference_url",
        "description": "URL for the conference program or abstracts",
        "required": False,
    },
    {"name": "work_title", "description": "Work title"},
    {
        "name": "work_url",
        "description": "Direct URL for the work abstract if it exists",
        "required": False,
    },
    {
        "name": "work_authors",
        "description": "Named authors (separated by a semicolon)",
        "required": True,
    },
    {
        "name": "work_type",
        "description": "Type of work (e.g. keynote, multipaper session, poster",
        "required": True,
    },
    {
        "name": "parent_work_id",
        "description": "ID of a multipaper session or panel session that this work belongs to",
        "required": False,
    },
    {
        "name": "keywords",
        "description": "Author-submitted keywords (separated by a semicolon)",
        "required": False,
    },
    {
        "name": "languages",
        "description": "Language(s) of the abstract (separated by a semicolon)",
        "required": False,
    },
    {
        "name": "disciplines",
        "description": "Disciplines from ADHO controlled vocabulary (separated by a semicolon)",
        "required": False,
    },
    {
        "name": "topics",
        "description": "Topics from ADHO controlled vocabulary (separated by a semicolon)",
        "required": False,
    },
]

PUBLIC_DATA_TABLE_CONFIG = {
    "CONFIGURATION": [
        {
            "model": "Work",
            "exclude_fields": [
                "search_text",
                "full_text",
                "full_text_type",
                "full_text_license",
                "last_updated",
                "user_last_updated",
            ],
            "csv_name": "works",
        },
        {
            "model": "Author",
            "exclude_fields": [
                "appellations_index",
                "last_updated",
                "user_last_updated",
            ],
            "csv_name": "authors",
        },
        {
            "model": "Conference",
            "exclude_fields": ["editing_user"],
            "csv_name": "conferences",
            "include_string": True,
        },
        {
            "model": "Conference.organizers.through",
            "exclude_fields": [],
            "csv_name": "conference_organizer",
        },
        {
            "model": "Conference.hosting_institutions.through",
            "exclude_fields": [],
            "csv_name": "conference_hosting_institution",
        },
        {
            "model": "ConferenceSeries",
            "exclude_fields": [],
            "csv_name": "conference_series",
        },
        {
            "model": "SeriesMembership",
            "exclude_fields": [],
            "csv_name": "conference_series_membership",
        },
        {
            "model": "Organizer",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "organizers",
        },
        {
            "model": "Authorship",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "authorships",
        },
        {
            "model": "Authorship.affiliations.through",
            "exclude_fields": [],
            "csv_name": "authorship_affiliation",
        },
        {"model": "Appellation", "exclude_fields": [], "csv_name": "appellations"},
        {
            "model": "Institution",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "institutions",
        },
        {"model": "Affiliation", "exclude_fields": [], "csv_name": "affiliations"},
        {"model": "Country", "exclude_fields": [], "csv_name": "countries"},
        {"model": "Keyword", "exclude_fields": [], "csv_name": "keywords"},
        {"model": "Topic", "exclude_fields": [], "csv_name": "topics"},
        {"model": "Discipline", "exclude_fields": [], "csv_name": "disciplines"},
        {"model": "Language", "exclude_fields": [], "csv_name": "languages"},
        {"model": "WorkType", "exclude_fields": [], "csv_name": "work_types"},
    ],
    "DATA_ZIP_NAME": "dh_conferences_tables.zip",
}

PRIVATE_DATA_TABLE_CONFIG = {
    "CONFIGURATION": [
        {
            "model": "Work",
            "exclude_fields": ["search_text", "last_updated", "user_last_updated"],
            "csv_name": "works",
        },
        {
            "model": "Author",
            "exclude_fields": [
                "appellations_index",
                "last_updated",
                "user_last_updated",
            ],
            "csv_name": "authors",
        },
        {
            "model": "Conference",
            "exclude_fields": ["editing_user"],
            "csv_name": "conferences",
            "include_string": True,
        },
        {
            "model": "Conference.organizers.through",
            "exclude_fields": [],
            "csv_name": "conference_organizer",
        },
        {
            "model": "Conference.hosting_institutions.through",
            "exclude_fields": [],
            "csv_name": "conference_hosting_institution",
        },
        {
            "model": "ConferenceSeries",
            "exclude_fields": [],
            "csv_name": "conference_series",
        },
        {
            "model": "SeriesMembership",
            "exclude_fields": [],
            "csv_name": "conference_series_membership",
        },
        {
            "model": "Organizer",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "organizers",
        },
        {
            "model": "Authorship",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "authorships",
        },
        {
            "model": "Authorship.affiliations.through",
            "exclude_fields": [],
            "csv_name": "authorship_affiliation",
        },
        {"model": "Appellation", "exclude_fields": [], "csv_name": "appellations"},
        {
            "model": "Institution",
            "exclude_fields": ["last_updated", "user_last_updated"],
            "csv_name": "institutions",
        },
        {"model": "Affiliation", "exclude_fields": [], "csv_name": "affiliations"},
        {"model": "Country", "exclude_fields": [], "csv_name": "countries"},
        {"model": "Keyword", "exclude_fields": [], "csv_name": "keywords"},
        {"model": "Topic", "exclude_fields": [], "csv_name": "topics"},
        {"model": "Discipline", "exclude_fields": [], "csv_name": "disciplines"},
        {"model": "Language", "exclude_fields": [], "csv_name": "languages"},
        {"model": "WorkType", "exclude_fields": [], "csv_name": "work_types"},
        {"model": "License", "exclude_fields": [], "csv_name": "licenses"},
    ],
    "DATA_ZIP_NAME": "private_dh_conferences_tables.zip",
}

FILER_STORAGES = {
    "public": {
        "main": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": f"{STATIC_ROOT}/media",
                "base_url": f"{STATIC_URL}/media",
            },
            "UPLOAD_TO": "filer.utils.generate_filename.randomized",
            "UPLOAD_TO_PREFIX": "filer_public",
        },
        "thumbnails": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": f"{STATIC_ROOT}/media/thumbnails",
                "base_url": f"{STATIC_URL}/media/thumbnails",
            },
        },
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 262144000

FILER_CANONICAL_URL = "files/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
    "loggers": {
        "django": {"handlers": ["console"], "level": "WARNING", "propagate": False}
    },
}

# Email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 25)
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_ADDRESS")

MARKDOWNIFY_WHITELIST_TAGS = [
    "a",
    "abbr",
    "acronym",
    "b",
    "blockquote",
    "em",
    "i",
    "li",
    "ol",
    "p",
    "strong",
    "ul",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "pre",
    "code",
]

MARKDOWNIFY_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.extra",
    "markdown.extensions.toc",
]
