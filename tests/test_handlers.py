"""处理器测试"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, User as TelegramUser, Chat, Message
from telegram.ext import ContextTypes


@pytest.mark.asyncio
async def test_start_handler():
    """测试 /start 命令"""
    # 创建模拟对象
    user = TelegramUser(id=123, is_bot=False, first_name="Test")
    chat = Chat(id=123, type="private")
    message = Message(message_id=1, date=None, chat=chat, text="/start")
    update = Update(update_id=1, message=message)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    
    # 模拟 reply_text 方法
    message.reply_text = AsyncMock()
    update.message.reply_text = AsyncMock()
    
    # 导入并调用处理器
    from bot.handlers import start_handler
    await start_handler(update, context)
    
    # 验证
    assert update.message.reply_text.called


@pytest.mark.asyncio
async def test_help_handler():
    """测试 /help 命令"""
    # 创建模拟对象
    update = AsyncMock(spec=Update)
    context = AsyncMock(spec=ContextTypes.DEFAULT_TYPE)
    
    # 模拟 reply_text 方法
    update.message.reply_text = AsyncMock()
    
    # 导入并调用处理器
    from bot.handlers import help_handler
    await help_handler(update, context)
    
    # 验证
    assert update.message.reply_text.called
