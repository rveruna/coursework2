#default config
class BaseConfig(object):
    DEBUG = False
    #random session id generated in python
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

#overriding debug class for development
class DevelopmentConfig(BaseConfig):
    DEBUG = True

#overriding debug class for deployment
#class ProductionConfig(BaseConfig):
    #DEBUG = False
