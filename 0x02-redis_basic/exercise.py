#!/usr/bin/env python3
"""Main module for all mandatory tasks."""
from functools import wraps
from redis import Redis
from typing import Any, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator function that counts calls of Cache method calls."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator function that stores in and out of Cache method calls."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input = str(args)
        output = method(self, *input, **kwargs)
        self._redis.rpush(method.__qualname__ + ':inputs', input)
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """Prints information about history of calls of a function."""
    redis = Redis()
    calls = int(redis.get(fn.__qualname__) or 0)
    print(fn.__qualname__, 'was called', calls, 'times')
    lst = zip(
        redis.lrange(fn.__qualname__ + ':inputs', 0, calls),
        redis.lrange(fn.__qualname__ + ':outputs', 0, calls))
    for inp, out in lst:
        print(f'{fn.__qualname__}(*({inp})) -> {out}')


class Cache:
    """Cache class, a client which connects to reddis"""
    def __init__(self) -> None:
        """Constructor for Cache class."""
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Any) -> str:
        """Stores data in redis using a key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable | None = None) -> Any | None:
        """Retrieves data from redis using a key, and a convertion function."""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str | None:
        "Retrieves a string from reddis"
        return self.get(key, str)

    def get_int(self, key: str) -> int | None:
        "Retrieves a int from reddis"
        return self.get(key, int)
