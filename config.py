from os import environ, path

# https://hackersandslackers.com/configure-flask-applications/


class Config:
    """Base config"""

    HOST = (environ.get("IP", "0.0.0.0"),)
    PORT = (int(environ.get("PORT", "5000")),)


class ProdConfig(Config):
    FLASK_ENV = "production"
    TESTING = False
    DEBUG = False


class DevConfig(Config):
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True
