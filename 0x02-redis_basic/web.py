#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker."""
from functools import wraps
import redis
import requests
from typing import Callable, Any


def count_access(fn: Callable) -> Callable:
    """Decorator function that adds caching for get_page"""
    _redis = redis.Redis()

    @wraps(fn)
    def wrapper(url, *args, **kwargs) -> Any:
        """idk bruh just let me go to sleep"""
        count_key = 'count:' + url
        cache_key = 'cache:' + url
        _redis.incr(count_key)
        data = _redis.get(cache_key)
        if data:
            return data.decode()
        data = fn(url, *args, **kwargs)
        _redis.set(cache_key, data)
        _redis.expire(cache_key, 10)
        return data
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Retrieves the content of an html page."""
    return requests.get(url).text
