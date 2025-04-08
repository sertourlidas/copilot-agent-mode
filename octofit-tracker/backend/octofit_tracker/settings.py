import os
import ssl

if os.getenv('CODESPACES'):
    ssl._create_default_https_context = ssl._create_unverified_context

# Add MongoDB connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
         'ENFORCE_SCHEMA': False,  # Disable schema validation
    }
}
ROOT_URLCONF = 'octofit_tracker.urls'
# Ensure INSTALLED_APPS is defined
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

# Add additional apps
INSTALLED_APPS += [
    'corsheaders',
    'octofit_tracker',
]

# Ensure MIDDLEWARE is defined
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add CORS middleware at the top of the MIDDLEWARE list
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Allow all origins, methods, and headers
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
]


ALLOWED_HOSTS = [
    'localhost',
    'urban-journey-5g65p57jqgjfwv9.github.dev-8000'
]

SECRET_KEY = 'Z4Kkw7PgXnNx9HG2RvzarOHmO4hicLv2lMOAszY8NMLWsWWedqymEVdjZibpNlZcgMg'

# Add TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add template directories here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]