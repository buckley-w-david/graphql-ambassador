import enum
from flask import Flask

from graphql_ambassador import config
from graphql_ambassador.proxy import proxy

__version__ = '0.1.0'

@enum.unique
class Environment(enum.Enum):
    TESTING = enum.auto()
    DEVELOPMENT = enum.auto()
    PRODUCTION = enum.auto()

    @staticmethod
    def from_string(env: str) -> 'Environment':
        return getattr(Environment, env.upper())

CONFIGMAP = {
    Environment.TESTING: config.TestingConfig,
    Environment.DEVELOPMENT: config.DevelopmentConfig,
    Environment.PRODUCTION: config.ProductionConfig,
}

def create_app(environment: Environment) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(CONFIGMAP[environment])
    app.config.from_pyfile('application.cfg', silent=True)
    app.register_blueprint(proxy)

    return app
