#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my precious'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

#overriding debug class
class DevelopmentConfig(BaseConfig):
    DEBUG = True

#overriding debug class for deployment
class ProductionConfig(BaseConfig):
    DEBUG = False
