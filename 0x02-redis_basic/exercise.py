#!/usr/bin/env python3
"""
Cache class implimentation
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize the Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """
        Generate a key and store input data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

    