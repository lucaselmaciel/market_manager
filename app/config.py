import os

class Config:
    # Chave secreta, usada para segurança das sessões, entre outros
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Configurações do banco de dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///market_manager.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Ativa o log de queries SQL (útil durante o desenvolvimento)

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
