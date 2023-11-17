#!/usr/bin/env python3
""" Cache module
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        inp_key = key + ":inputs"
        out_key = key + ":outputs"
        self._redis.rpush(inp_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(res))
        return res
    return wrapper


class Cache:
    """
    Cache class will be used to do operation on redis client
    """


    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
