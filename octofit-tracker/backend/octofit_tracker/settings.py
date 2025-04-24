# settings.py

# MongoDB configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# CORS configuration
INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
    'tracker_app',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
