#!/usr/bin/env python3
""" Cache module
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count how many numbers function
    in cache have been called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper to return the result
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    save into redis the input and outputs that
    have been called with a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper to return the result
        """
        key = method.__qualname__
        inp_key = key + ":inputs"
        out_key = key + ":outputs"
        self._redis.rpush(inp_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(res))
        return res
    return wrapper


def replay(func: Callable):
    """
    show summary of how many times a function have been called
    with summary of inputs and outputs the function had made
    """
    r = redis.Redis()
    key = func.__qualname__
    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)
    calls = len(inputs)
    print('{} was called {} {}:'.format(key,
                                        calls,
                                        "time" if calls == 1 else "times"))
    for k, v in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(key, k.decode(), v.decode()))


class Cache:
    """
    Cache class will be used to do operation on redis client
    """

    def __init__(self) -> None:
        """initialize new instance of cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores info in redis database"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """
        get data that have been saved in redis using
        its key with formmater function
        """
        data = self._redis.get(key)
        if not data:
            return None
        if not fn:
            return data
        return fn(data)

    def get_int(self, key: str) -> int:
        """foramtter for getting int from redis"""
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> str:
        """foramtter for getting string from redis"""
        return self.get(key, lambda x: str(x))
