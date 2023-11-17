#!/usr/bin/env python3
""" Cache module
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    Cache class will be used to do operation on redis client
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if not data:
            return None
        if not fn:
            return data
        return fn(data)

    def get_int(self, key: str) -> int:
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: str(x))
