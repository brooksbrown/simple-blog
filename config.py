import os
from datetime import timedelta

project_name = "brooksbrown.info"


class Config(object):
    DEBUG = False
    TESTING = False
    USE_X_SENDFILE = False

    # DATABASE CONFIGURATION
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_dev-k.sqlite" % project_name
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
    SECRET_KEY = "secret"  # import os; os.urandom(24)
    LOGGER_NAME = "%s_log" % project_name
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

    DEV_SERVER_HOST = "127.0.0.1"
    DEV_SERVER_PORT = 8000
    BLUEPRINTS = [
        #'blog.views.app' # or ('blog.views.app', {'url_prefix':'/blog'})
    ]  # each as (blueprint_instance, url_preffix)


class Dev(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DEV_SERVER_HOST = "0.0.0.0"
    DEV_SERVER_PORT = 8000

class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
    SQLALCHEMY_ECHO = False
