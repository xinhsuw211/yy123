"""数据格式化"""

from datetime import datetime
from typing import Any


class Formatters:
    """数据格式化器"""
    
    @staticmethod
    def format_score(score: int) -> str:
        """格式化分数"""
        if score >= 1000000:
            return f"{score / 1000000:.1f}M"
        elif score >= 1000:
            return f"{score / 1000:.1f}K"
        return str(score)
    
    @staticmethod
    def format_distance(distance: float) -> str:
        """格式化距离"""
        if distance >= 1000:
            return f"{distance / 1000:.2f} km"
        return f"{distance:.2f} m"
    
    @staticmethod
    def format_datetime(dt: datetime) -> str:
        """格式化日期时间"""
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def format_percentage(value: float) -> str:
        """格式化百分比"""
        return f"{value * 100:.1f}%"
