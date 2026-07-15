import os
from dotenv import load_dotenv
from pathlib import Path

# 加载环境变量
load_dotenv()

# ==========================================
# 基础配置
# ==========================================
BASE_DIR = Path(__file__).resolve().parent

class Config:
    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_ADMIN_IDS = os.getenv('TELEGRAM_ADMIN_IDS', '').split(',') if os.getenv('TELEGRAM_ADMIN_IDS') else []
    TELEGRAM_WEBHOOK_URL = os.getenv('TELEGRAM_WEBHOOK_URL', '')
    
    # Database
    DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/db.sqlite')
    
    # AI & Analytics
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
    ENABLE_AI_ANALYSIS = os.getenv('ENABLE_AI_ANALYSIS', 'true').lower() == 'true'
    
    # Computer Vision
    OPENCV_ENABLED = os.getenv('OPENCV_ENABLED', 'true').lower() == 'true'
    OPENCV_CONFIDENCE_THRESHOLD = float(os.getenv('OPENCV_CONFIDENCE_THRESHOLD', '0.7'))
    
    # Features
    ENABLE_NOTIFICATIONS = os.getenv('ENABLE_NOTIFICATIONS', 'true').lower() == 'true'
    ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'true').lower() == 'true'
    ENABLE_LEADERBOARD = os.getenv('ENABLE_LEADERBOARD', 'true').lower() == 'true'
    ENABLE_ACHIEVEMENTS = os.getenv('ENABLE_ACHIEVEMENTS', 'true').lower() == 'true'
    ENABLE_IMAGE_ANALYSIS = os.getenv('ENABLE_IMAGE_ANALYSIS', 'true').lower() == 'true'
    ENABLE_DATA_BACKUP = os.getenv('ENABLE_DATA_BACKUP', 'true').lower() == 'true'
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/bot.log')
    LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', '10485760'))
    LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', '5'))
    
    # Application
    APP_NAME = os.getenv('APP_NAME', 'Paper Airplane Bot')
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
    APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'development')
    DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    
    # Timezone & Localization
    DEFAULT_TIMEZONE = os.getenv('DEFAULT_TIMEZONE', 'UTC')
    DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'zh_CN')
    SUPPORTED_LANGUAGES = os.getenv('SUPPORTED_LANGUAGES', 'zh_CN,en_US,ja_JP').split(',')
    
    # API
    API_RATE_LIMIT = int(os.getenv('API_RATE_LIMIT', '100'))
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    API_RETRY_ATTEMPTS = int(os.getenv('API_RETRY_ATTEMPTS', '3'))
    
    # Backup
    BACKUP_ENABLED = os.getenv('BACKUP_ENABLED', 'true').lower() == 'true'
    BACKUP_INTERVAL_HOURS = int(os.getenv('BACKUP_INTERVAL_HOURS', '24'))
    BACKUP_DIR = os.getenv('BACKUP_DIR', 'data/backups')
    BACKUP_RETENTION_DAYS = int(os.getenv('BACKUP_RETENTION_DAYS', '30'))
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    PASSWORD_HASH_ALGORITHM = os.getenv('PASSWORD_HASH_ALGORITHM', 'bcrypt')
    
    # Notifications
    NOTIFICATION_ON_JOIN = os.getenv('NOTIFICATION_ON_JOIN', 'true').lower() == 'true'
    NOTIFICATION_ON_ACHIEVEMENT = os.getenv('NOTIFICATION_ON_ACHIEVEMENT', 'true').lower() == 'true'
    NOTIFICATION_ON_COMPETITION_START = os.getenv('NOTIFICATION_ON_COMPETITION_START', 'true').lower() == 'true'
    NOTIFICATION_ON_LEADERBOARD_UPDATE = os.getenv('NOTIFICATION_ON_LEADERBOARD_UPDATE', 'true').lower() == 'true'
    
    # Paths
    DATA_DIR = BASE_DIR / 'data'
    LOGS_DIR = BASE_DIR / 'logs'
    BACKUP_DIR_PATH = BASE_DIR / BACKUP_DIR
    
    @classmethod
    def init_directories(cls):
        """初始化必要的目录"""
        for directory in [cls.DATA_DIR, cls.LOGS_DIR, cls.BACKUP_DIR_PATH]:
            directory.mkdir(parents=True, exist_ok=True)

# 初始化配置
config = Config()
config.init_directories()
