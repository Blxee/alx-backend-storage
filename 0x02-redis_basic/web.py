#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker."""
from functools import wraps
from redis import Redis
import requests
from typing import Callable, Any


def count_access(fn: Callable) -> Callable:
    """Decorator function that adds caching for get_page"""
    redis = Redis()

    @wraps(fn)
    def wrapper(url, *args, **kwargs) -> Any:
        key = 'count:' + url
        redis.incr(key)
        redis.expire(key, 10)
        return fn(url, *args, **kwargs)
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Retrieves the content of an html page."""
    return requests.get(url).text
