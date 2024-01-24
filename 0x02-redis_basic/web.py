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
        count_key = 'count:' + url
        cache_key = 'cache:' + url
        redis.incr(count_key)
        data = redis.get(cache_key)
        if data:
            return data
        else:
            data = fn(url, *args, **kwargs)
        redis.set(cache_key, data)
        redis.expire(cache_key, 10)
        return data
    return wrapper


@count_access
def get_page(url: str) -> str:
    """Retrieves the content of an html page."""
    return requests.get(url).text
