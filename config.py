import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  CSRF_ENABLED = True
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'APP_SECRET'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
