#!/usr/bin/env python3
""" Cache module
"""
from typing import Union, Callable, Optional
from functools import wraps
import requests
import redis


redis = redis.Redis()


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        func = method.__qualname__
        url = args[0]
        redis.incr(f"count:{url}")
        cache = redis.get(f"cached:{url}")
        if cache:
            return cache.decode()
        html = method(*args, **kwargs)
        redis.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@call_history
def get_page(url: str) -> str:
    res = requests.get(url)
    return res.text
