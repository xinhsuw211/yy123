"""数据库连接和初始化"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config
from utils.logger import get_logger

logger = get_logger(__name__)

# 创建引擎
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """初始化数据库"""
    try:
        # 创建所有表
        from models.user import Base
        Base.metadata.create_all(bind=engine)
        logger.info("数据库初始化成功")
    except Exception as e:
        logger.error(f"数据库初始化失败: {e}")
        raise
