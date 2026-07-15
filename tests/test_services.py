"""服务测试"""

import pytest
from services.user_service import UserService
from models.user import User


def test_create_user():
    """测试创建用户"""
    service = UserService()
    user = service.create_user(
        user_id=123,
        username="testuser",
        first_name="Test"
    )
    
    assert user is not None
    assert user.id == 123
    assert user.username == "testuser"
    assert user.first_name == "Test"


def test_get_user():
    """测试获取用户"""
    service = UserService()
    service.create_user(123, "testuser", "Test")
    
    user = service.get_user(123)
    assert user is not None
    assert user.id == 123


def test_add_score():
    """测试添加积分"""
    service = UserService()
    service.create_user(123, "testuser", "Test")
    
    user = service.add_score(123, 100)
    assert user.total_score == 100


def test_ban_user():
    """测试封禁用户"""
    service = UserService()
    service.create_user(123, "testuser", "Test")
    
    user = service.ban_user(123)
    assert user.is_banned is True
