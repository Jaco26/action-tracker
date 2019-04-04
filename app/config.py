import os

class BaseConfig:
  JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
  JWT_BLACKLIST_ENABLED = True


class DevConfig(BaseConfig):
  DATABASE_URL = os.environ["DEVELOPMENT_DATABASE_URL"]


class ProdConfig(BaseConfig):
  DATABASE_URL = os.environ["DATABASE_URL"]