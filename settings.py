# Django settings for stinkomanlevels project.
import os

def absolute(relative_path):
    """
    make a relative path absolute
    """
    return os.path.join(os.path.dirname(__file__), relative_path)

release_mode = os.path.exists(absolute("RELEASE"))

DEBUG = not release_mode
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Andy Kelley', 'superjoe30@gmail.com'),
)

MANAGERS = ADMINS

if release_mode:
    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_ENGINE = 'mysql'           
    # Or path to database file if using sqlite3.
    DATABASE_NAME = 'superjoe_stinkoman'             
    # Not used with sqlite3.
    DATABASE_USER = 'superjoe_stinkom'
    # Not used with sqlite3.
    DATABASE_PASSWORD = 'THp3IeM7XXr5'
    # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_HOST = ''
    # Set to empty string for default. Not used with sqlite3.
    DATABASE_PORT = ''
else:
    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_ENGINE = 'sqlite3'           
    # Or path to database file if using sqlite3.
    DATABASE_NAME = absolute('db')
    # Not used with sqlite3.
    DATABASE_USER = ''             
    # Not used with sqlite3.
    DATABASE_PASSWORD = ''         
    # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_HOST = ''             
    # Set to empty string for default. Not used with sqlite3.
    DATABASE_PORT = ''             

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Phoenix'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = absolute('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if release_mode:
    MEDIA_URL = 'http://superjoesoftware.com/djangomedia/stinkomanlevels/'
else:
    MEDIA_URL = 'http://localhost:8080/django/stinkomanlevels/'


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
if release_mode:
    ADMIN_MEDIA_PREFIX= 'http://superjoesoftware.com/djangomedia/stinkomanlevels/admin/'
else:
    ADMIN_MEDIA_PREFIX = 'http://localhost:8080/django/stinkomanlevels/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&f957%02#t1ze*4$9f5*l1s0c)$7p*x1+nuo@kb4fktx$e2r9!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'stinkomanlevels.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    absolute('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'stinkomanlevels.main',
    'registration',
)

LOGIN_URL = "/login/"
AUTH_PROFILE_MODULE = 'main.Profile'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
