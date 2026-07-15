"""用户服务"""

from typing import Optional
from models.user import User
from utils.logger import get_logger

logger = get_logger(__name__)


class UserService:
    """用户管理服务"""
    
    def __init__(self):
        self.users = {}  # 临时存储
    
    def create_user(self, user_id: int, username: str, first_name: str, last_name: str = None) -> User:
        """创建用户"""
        user = User(
            id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        self.users[user_id] = user
        logger.info(f"创建用户: {user.full_name} ({user_id})")
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """获取用户"""
        return self.users.get(user_id)
    
    def add_score(self, user_id: int, score: int) -> Optional[User]:
        """添加积分"""
        user = self.get_user(user_id)
        if user:
            user.total_score += score
            user.update_level()
            logger.info(f"用户 {user_id} 获得 {score} 积分，总积分: {user.total_score}")
            return user
        return None
    
    def ban_user(self, user_id: int) -> Optional[User]:
        """封禁用户"""
        user = self.get_user(user_id)
        if user:
            user.is_banned = True
            logger.warning(f"用户 {user_id} 已被封禁")
            return user
        return None
    
    def unban_user(self, user_id: int) -> Optional[User]:
        """解除封禁"""
        user = self.get_user(user_id)
        if user:
            user.is_banned = False
            logger.info(f"用户 {user_id} 已解除封禁")
            return user
        return None


# 全局服务实例
user_service = UserService()
