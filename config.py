from os import environ, path
from dotenv import load_dotenv

# https://hackersandslackers.com/configure-flask-applications/

# https://www.geeksforgeeks.org/__file__-a-special-variable-in-python/
# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Base config"""

    SECRET_KEY = environ.get("SECRET_KEY")
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
