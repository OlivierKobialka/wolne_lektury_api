import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@db/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = 'DEBUG'
