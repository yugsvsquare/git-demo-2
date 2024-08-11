

class Config:
  DEBUG = False
  TESTING = False
  DATABASE_URL = 'sqlite:///:memory:'
  LOG_LEVEL = 3
  LOG_FILE_PATH = "/home/user/logs/"
  SECRET_KEY = "dev-key"
  SECURE_COOKIES = "test-cookie"
  API_ENDPOINT = "https://dev/"

class ProductionConfig(Config):
  DATABASE_URL = 'mysql://user@localhost/foo'
  API_ENDPOINT = "https://prod/"
  LOG_LEVEL = 1
  LOG_FILE_PATH = "/home/user/prod/logs/"
  SECRET_KEY = "prod-key"
  SECURE_COOKIES = "prod-cookie"

class DevelopmentConfig(Config):
  DEBUG = True
  LOG_LEVEL = 2


class TestingConfig(Config):
  TESTING = True
  API_ENDPOINT = "https://testapi/"
  LOG_FILE_PATH = "/home/user/test/logs/"
  SECRET_KEY = "test-key"
  SECURE_COOKIES = "test-cookie"


