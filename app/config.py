import os

class BaseConfig:
  pass


class DevConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = os.environ["DEV_DB_URI"]
  DATABASE_URL = os.environ["DATABASE_URL"]
  PROD_DATABASE_URI = os.environ[""]


class ProdConfig(BaseConfig):
  DATABASE_URL = os.environ["DATABASE_URL"]
