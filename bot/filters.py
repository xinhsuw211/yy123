"""自定义过滤器"""

from telegram.ext import filters
from config import config


class CustomFilters:
    """自定义过滤器"""
    
    @staticmethod
    def is_admin():
        """检查是否为管理员"""
        def filter_func(update):
            return update.effective_user.id in [int(id) for id in config.TELEGRAM_ADMIN_IDS]
        return filters.UpdateFilter(filter_func)
    
    @staticmethod
    def is_group():
        """检查是否为群组消息"""
        return filters.ChatType.GROUP | filters.ChatType.SUPERGROUP
    
    @staticmethod
    def is_private():
        """检查是否为私聊消息"""
        return filters.ChatType.PRIVATE
