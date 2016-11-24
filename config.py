#default config
class BaseConfig(object):
    DEBUG = False
    #random session id generated in python
    SECRET_KEY = '\xbf\xb4\xff\x989\xa19\x06\xde@0%\xf8\x0b\x90\xe8\xa4w\xa5\xbe\x9d\xe5\x97\xb2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

#overriding debug class for development
class DevelopmentConfig(BaseConfig):
    DEBUG = True

#overriding debug class for deployment
class ProductionConfig(BaseConfig):
    DEBUG = False
