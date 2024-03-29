import os
from decouple import config
from datetime import timedelta


SECRET_KEY = config('SECRET_KEY')
JWT_SECRET_KEY = config('SECRET_KEY')
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__)) #dunder method
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'db.sqlite') + '?check_same_thread=False'

supports_credentials=True
CORS_SUPPORTS_CREDENTIALS=True

JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
