import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', "sqlite://")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", os.urandom(16))

    SENTRY_DSN = os.environ.get('SENTRY_DSN')
    SENTRY_RELEASE_ID = os.environ.get('SENTRY_RELEASE_ID', 'dev')
    SENTRY_ENVIRONMENT = os.environ.get('SENTRY_ENVIRONMENT', 'dev')

    CORS_ORIGINS = os.environ.get('ALLOWED_ORIGINS', "*")

    API_KEY = os.environ.get('API_KEY', None)
