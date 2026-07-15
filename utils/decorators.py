"""自定义装饰器"""

from functools import wraps
from typing import Callable
from utils.logger import get_logger

logger = get_logger(__name__)


def retry(max_attempts: int = 3, delay: int = 1):
    """重试装饰器"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        logger.error(f"函数 {func.__name__} 最终失败: {e}")
                        raise
                    logger.warning(f"函数 {func.__name__} 失败，{delay}秒后重试... (尝试 {attempt + 1}/{max_attempts})")
                    time.sleep(delay)
        return wrapper
    return decorator


def timer(func: Callable) -> Callable:
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logger.debug(f"函数 {func.__name__} 执行耗时: {duration:.3f}秒")
        return result
    return wrapper
