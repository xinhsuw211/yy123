#!/usr/bin/env python3
"""
纸飞机 Telegram 机器人主入口

Features:
- 完整的用户管理系统
- 纸飞机配置和竞赛管理
- AI 飞行分析和优化建议
- 实时排行榜和成就系统
- 图像识别和轨迹追踪
- 数据备份和恢复
"""

import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

from config import config
from utils.logger import setup_logger
from bot.handlers import (
    start_handler,
    help_handler,
    me_handler,
    leaderboard_handler,
    competitions_handler,
    achievements_handler,
    stats_handler
)

# 设置日志
logger = setup_logger(__name__)


async def error_handler(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理机器人错误"""
    logger.error(f"Update {update} caused error {context.error}")
    try:
        raise context.error
    except Exception as exc:
        logger.exception(f"Unhandled exception: {exc}")
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "发生错误。请稍后再试。😔"
            )


async def main() -> None:
    """启动机器人"""
    logger.info(f"启动 {config.APP_NAME} v{config.APP_VERSION}")
    logger.info(f"环境: {config.APP_ENVIRONMENT}")
    logger.info(f"数据库: {config.DATABASE_TYPE}")
    
    # 创建应用
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    # 添加命令处理器
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("me", me_handler))
    application.add_handler(CommandHandler("leaderboard", leaderboard_handler))
    application.add_handler(CommandHandler("competitions", competitions_handler))
    application.add_handler(CommandHandler("achievements", achievements_handler))
    application.add_handler(CommandHandler("stats", stats_handler))
    
    # 添加错误处理器
    application.add_error_handler(error_handler)
    
    # 启动机器人
    logger.info("机器人已启动，监听消息...")
    
    try:
        await application.run_polling()
    except Exception as e:
        logger.error(f"机器人启动失败: {e}")
        raise


if __name__ == "__main__":
    if not config.TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN 未配置")
        exit(1)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("机器人已停止")
    except Exception as e:
        logger.error(f"致命错误: {e}", exc_info=True)
        exit(1)
