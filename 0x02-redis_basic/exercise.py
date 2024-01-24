#!/usr/bin/env python3
"""Main module for all mandatory tasks."""
from redis import Redis
from typing import Any
from uuid import uuid4


class Cache:
    """Cache class, a client which connects to reddis"""
    def __init__(self) -> None:
        """Constructor for Cache class."""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Stores data in redis using a key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
