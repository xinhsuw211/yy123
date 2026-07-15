"""机器人工具函数"""

import time
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import get_logger

logger = get_logger(__name__)


def rate_limit(max_calls: int = 10, time_window: int = 60):
    """速率限制装饰器"""
    def decorator(func):
        func._rate_limit_calls = {}
        
        @wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
            user_id = update.effective_user.id
            now = time.time()
            
            if user_id not in func._rate_limit_calls:
                func._rate_limit_calls[user_id] = []
            
            # 清除过期的调用记录
            func._rate_limit_calls[user_id] = [
                call_time for call_time in func._rate_limit_calls[user_id]
                if now - call_time < time_window
            ]
            
            # 检查是否超过限制
            if len(func._rate_limit_calls[user_id]) >= max_calls:
                await update.message.reply_text(
                    f"⏱️ 操作过于频繁，请稍后再试。"
                )
                return
            
            func._rate_limit_calls[user_id].append(now)
            return await func(update, context, *args, **kwargs)
        
        return wrapper
    return decorator


def log_command(func):
    """记录命令调用"""
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user = update.effective_user
        command = update.message.text
        logger.info(f"用户 {user.id} ({user.username}) 执行命令: {command}")
        return await func(update, context, *args, **kwargs)
    
    return wrapper
