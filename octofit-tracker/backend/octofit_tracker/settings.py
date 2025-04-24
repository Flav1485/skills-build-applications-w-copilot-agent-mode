# settings.py

# MongoDB configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'your_username',
            'password': 'your_password',
            'authSource': 'admin',
        },
    }
}

# CORS configuration
INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
    'tracker_app',
    'djongo',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

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
    'x-csrftoken',
]

ALLOWED_HOSTS = ['*']

# Codespace URL configuration
CODESPACE_URL = "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
