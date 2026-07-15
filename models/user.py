"""用户模型"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class User:
    """用户模型"""
    
    id: int  # Telegram User ID
    username: str
    first_name: str
    last_name: Optional[str] = None
    total_flights: int = 0
    total_score: int = 0
    rank: int = 0
    level: str = "初级"  # 初级、中级、高级、专业、大师
    created_at: datetime = None
    updated_at: datetime = None
    is_banned: bool = False
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    @property
    def full_name(self) -> str:
        """获取全名"""
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name
    
    def update_level(self):
        """根据积分更新等级"""
        if self.total_score < 500:
            self.level = "初级"
        elif self.total_score < 1500:
            self.level = "中级"
        elif self.total_score < 3000:
            self.level = "高级"
        elif self.total_score < 5000:
            self.level = "专业"
        else:
            self.level = "大师"
