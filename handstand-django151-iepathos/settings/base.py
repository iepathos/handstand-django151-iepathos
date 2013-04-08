# base settings
import os.path

from django.template.defaultfilters import slugify

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Glen Baker', 'iepathos@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'us-_!(655#qa16dzv#2gg%sxfns#w9q*-0qe41w!zw7b0f#e(5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'profiles.middleware.LazyProfileMiddleware'
)

ROOT_URLCONF = 'handstand-django151-iepathos.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

DJANGO_WYSIWYG_FLAVOR = "tinymce" 

PREREQ_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'startcbv',
    'core',
    'social_auth',
    'profiles',
    'django_extensions',
    'django_coverage',
    'tinymce',
    'django_wysiwyg',
)

PROJECT_APPS = ()

if PROJECT_APPS:
    INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS
else:
    INSTALLED_APPS = PREREQ_APPS

########## BEGIN TESTRUNNER CONFIGURATION
TEST_RUNNER = 'testrunner.OurCoverageRunner'
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$','admin',
    'migrations', 'fixtures','debug_toolbar','djkombu',
]
COVERAGE_MODULE_EXCLUDES += PREREQ_APPS
COVERAGE_REPORT_HTML_OUTPUT_DIR = "coverage"
########## END TESTRUNNER CONFIGURATION

AUTH_PROFILE_MODULE = "profiles.Profile"

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "profiles.context_processors.lazy_profile",
]

# For django-social-auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter', 'facebook',)
# Don't forget to set TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, FACEBOOK_APP_ID, FACEBOOK_API_SECRET in dev.py
LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'
SOCIAL_AUTH_USERNAME_FIXER = lambda u: slugify(u)

