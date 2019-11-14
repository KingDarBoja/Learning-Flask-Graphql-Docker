# pylint: disable=too-few-public-methods
"""Configure our Flask enviroment variables in a Pythonic way."""

class Config():
    """Base config class to store and share enviroment variables"""
    DEBUG = False
    TESTING = False

    DB_NAME = "prod-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

class ProductionConfig(Config):
    """Production config class

    Arguments:
        Config {type} -- Config enviroment variables for prod mode.
    """

class DevelopmentConfig(Config):
    """Development config class

    Arguments:
        Config {type} -- Config enviroment variables for dev mode.
    """
    DEBUG = True

    DB_NAME = "dev-db"

class TestingConfig(Config):
    """Testing config class

    Arguments:
        Config {type} -- Config enviroment variables for testing purposes.
    """
    TESTING = True

    DB_NAME = "dev-db"
