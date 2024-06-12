# config.py
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")

# Define otras configuraciones (Testing, Staging, Production) si es necesario