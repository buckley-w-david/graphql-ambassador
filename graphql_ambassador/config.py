import os

class Config():
    ENV = 'production'
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    ENV = 'production'
    PROXY_SITE = os.environ.get('AMBASSADOR_SITE')


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    PROXY_SITE = 'https://swapi.co/api/'


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    PROXY_SITE = 'http://localhost'
