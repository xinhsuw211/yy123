"""数据验证器"""

import re
from typing import Optional


class Validators:
    """数据验证"""
    
    @staticmethod
    def is_valid_username(username: str) -> bool:
        """验证用户名"""
        if not username or not isinstance(username, str):
            return False
        return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """验证邮箱"""
        if not email or not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_valid_score(score: int) -> bool:
        """验证分数"""
        return isinstance(score, int) and score >= 0
    
    @staticmethod
    def is_valid_distance(distance: float) -> bool:
        """验证距离"""
        return isinstance(distance, (int, float)) and distance > 0
