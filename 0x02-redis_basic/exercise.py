#!/usr/bin/env python3
""" Cache module
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Cache class will be used to do operation on redis client
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
