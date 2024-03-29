#!/usr/bin/env python3
"""
Cache class implimentation
"""
import redis
import uuid
from typing import Union, Callable


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
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        # If a conversion function is provided, apply it to the data
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        # Get data from Redis and convert it to string
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        # Get data from Redis and convert it to integer
        return self.get(key, fn=int)
