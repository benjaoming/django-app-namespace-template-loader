"""Settings for testing apptemplates"""
DATABASES = {'default': {'NAME': 'apptemplates.db',
                         'ENGINE': 'django.db.backends.sqlite3'}}

SECRET_KEY = 'secret-key'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': ('apptemplates.Loader',
                        'django.template.loaders.app_directories.Loader')
        }
    }
]

ROOT_URLCONF = 'apptemplates.tests.urls'

INSTALLED_APPS = ('django.contrib.auth',
                  'django.contrib.admin',
                  'django.contrib.contenttypes')

SILENCED_SYSTEM_CHECKS = ['1_7.W001']
