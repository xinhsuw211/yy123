"""Telegram 机器人键盘UI"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def get_main_menu() -> ReplyKeyboardMarkup:
    """获取主菜单键盘"""
    keyboard = [
        [KeyboardButton("🏆 排行榜"), KeyboardButton("🎯 竞赛")],
        [KeyboardButton("✈️ 我的飞机"), KeyboardButton("🎮 成就")],
        [KeyboardButton("📊 统计"), KeyboardButton("⚙️ 设置")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_competition_menu() -> InlineKeyboardMarkup:
    """获取竞赛菜单"""
    keyboard = [
        [InlineKeyboardButton("加入竞赛", callback_data="join_competition")],
        [InlineKeyboardButton("查看排行榜", callback_data="comp_leaderboard")],
        [InlineKeyboardButton("提交成绩", callback_data="submit_score")],
        [InlineKeyboardButton("返回", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_admin_menu() -> InlineKeyboardMarkup:
    """获取管理员菜单"""
    keyboard = [
        [InlineKeyboardButton("创建竞赛", callback_data="admin_create_comp")],
        [InlineKeyboardButton("结束竞赛", callback_data="admin_end_comp")],
        [InlineKeyboardButton("用户管理", callback_data="admin_user_mgmt")],
        [InlineKeyboardButton("系统设置", callback_data="admin_settings")],
        [InlineKeyboardButton("返回", callback_data="back_to_main")],
    ]
    return InlineKeyboardMarkup(keyboard)
