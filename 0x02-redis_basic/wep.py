#!/usr/bin/env python3
"""
Web caching module
"""

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """Decorator wrapper for caching HTTP requests.

    This function is a decorator that wraps around a function that makes HTTP requests.
    It adds caching functionality using Redis to store and retrieve responses.

    Args:
        fn (Callable): The function to be wrapped.

    Returns:
        Callable: The wrapped function.

    """

    @wraps(fn)
    def wrapper(url):
        """Wrapper function for the decorator.

        This function is responsible for checking if the response for the given URL
        is already cached in Redis. If it is, it returns the cached response. Otherwise,
        it calls the original function to make the HTTP request, caches the response in Redis,
        and returns the response.

        Args:
            url (str): The URL to make the HTTP request to.

        Returns:
            str: The response from the HTTP request.

        """

        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """
    get page implimentatiion
    """
    response = requests.get(url)
    return response.text
