"""日志配置"""

import logging
import logging.handlers
from pathlib import Path
from config import config

# 创建日志目录
config.LOGS_DIR.mkdir(parents=True, exist_ok=True)

# 日志格式
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def setup_logger(name: str) -> logging.Logger:
    """设置日志"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.LOG_LEVEL))
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, config.LOG_LEVEL))
    console_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # 文件处理器
    file_handler = logging.handlers.RotatingFileHandler(
        config.LOG_FILE,
        maxBytes=config.LOG_MAX_BYTES,
        backupCount=config.LOG_BACKUP_COUNT
    )
    file_handler.setLevel(getattr(logging, config.LOG_LEVEL))
    file_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """获取日志器"""
    return logging.getLogger(name)
