#!/usr/bin/env python3
""" Web cache module """
import requests
from redis import Redis
from functools import wraps

r = Redis()


def cache(func):
    @wraps(func)
    def wrapper(url):
        # Construct the keys for the cache and count
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Check if the URL is in the cache
        if r.exists(cache_key):
            # Increment the count
            r.incr(count_key)
            return r.get(cache_key).decode('utf-8')

        # If the URL is not in the cache, get the HTML content
        result = func(url)

        # Store the result in the cache with an expiration time of 10 seconds
        r.setex(cache_key, 10, result)

        # Increment the count
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
