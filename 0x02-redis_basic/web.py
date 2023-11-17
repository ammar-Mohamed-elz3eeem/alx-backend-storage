#!/usr/bin/env python3
""" Cache module
"""
from typing import Union, Callable, Optional
from functools import wraps
import requests
import redis


redis = redis.Redis()


def call_history(method: Callable) -> Callable:
    """
    Decorator that wraps the get_page function
    working as a cache manager
    """
    @wraps(method)
    def wrapper(url):
        redis.incr(f"count:{url}")
        cache = redis.get(f"cached:{url}")
        if cache:
            return cache.decode()
        html = method(url)
        redis.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@call_history
def get_page(url: str) -> str:
    """
    make request to a page using request module
    """
    res = requests.get(url)
    return res.text
