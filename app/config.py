from distutils.debug import DEBUG
import os

class Config:
    
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class  ProdConfig:
    pass
class DevConfig(Config):
    DEBUG = True


# from distutils.log import DEBUG

# class Config: # general configuration of the parent class
#     pass
# class ProdConfig(Config):# Production  configuration child class
#     # Args:  
#     # Config: The parent configuration class with General configuration settings
#     pass
# class DevConfig(Config): # Development  configuration child class
#     # Args:
#     #   Config: The parent configuration class with General configuration settings
#     DEBUG = True



