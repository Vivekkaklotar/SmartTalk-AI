import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask Secret Key (Change in production!)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smarttalk-ai-super-secret-key-2024'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///smarttalk.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Bcrypt
    BCRYPT_LOG_ROUNDS = 12
    
    # Session Configuration
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False  # Set True in production with HTTPS
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Flask-Login
    LOGIN_MESSAGE = 'Please log in to access this page.'
    LOGIN_MESSAGE_CATEGORY = 'info'
    
    # App Settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    TESTING = os.environ.get('FLASK_TESTING', 'False').lower() == 'true'
    
    # Pagination
    CHATS_PER_PAGE = 20
    
    # AI Settings
    MAX_MESSAGE_LENGTH = 1000
    AI_RESPONSE_TIMEOUT = 10  # seconds

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///smarttalk_dev.db'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
    
    # Use PostgreSQL/MySQL in production
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    # Redis for sessions (optional)
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = 'redis://localhost:6379'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    BCRYPT_LOG_ROUNDS = 1  # Faster for tests
    WTF_CSRF_ENABLED = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}