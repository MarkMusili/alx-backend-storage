#!/usr/bin/env python3
""" Web cache module """
import requests
from typing import Callable
from redis import Redis
from functools import wraps

r = Redis()


def cache(func: Callable) -> Callable:
    """
    Decorator for get_url
    """
    @wraps(func)
    def wrapper(url):
        """
        Perform the caching
        """
        # Construct the keys for the cache and count
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        if not r.exists(count_key):
            r.set(count_key, 0)

        # Check if the URL is in the cache
        if r.exists(cache_key):
            # Increment the count
            r.incr(count_key)
            return r.get(cache_key).decode('utf-8')

        # If the URL is not in the cache, get the HTML content
        result = func(url)

        # Store the result in the cache with an expiration time of 10 seconds
        r.setex(cache_key, 10, result)

        r.incr(count_key)

        return result

    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Get a web page and return the result
    """
    response = requests.get(url)
    return response.text
