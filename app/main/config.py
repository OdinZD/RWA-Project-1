import os
from typing import Any

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
ENV = os.environ.get('PROJECT_ENV', 'dev')


class Config:
    SECRET_KEY: str = os.getenv('SECRET_KEY', '<---secret_key--->')
    AUTH_TOKEN_EXP_TIME = 60
    DEBUG: bool = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    PRESERVE_CONTEXT_ON_EXCEPTION: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY


def get_env_var(name: str, default: Any = None) -> Any:
    return getattr(config_by_name[ENV], name, default)
