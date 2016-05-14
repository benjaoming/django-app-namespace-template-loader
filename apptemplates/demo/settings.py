"""Settings for the apptemplates demo"""
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

STATIC_URL = '/static/'

SECRET_KEY = 'secret-key'

ROOT_URLCONF = 'apptemplates.demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': ('apptemplates.Loader',
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader')
        }
    }
]

INSTALLED_APPS = (
    'apptemplates.demo.application_extension',
    'apptemplates.demo.application_appconfig.apps.ApplicationConfig',
    'apptemplates.demo.application',
)

SILENCED_SYSTEM_CHECKS = ['1_7.W001', '1_8.W001']
