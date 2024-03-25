#!/usr/bin/env python3
"""
Function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update topics based on their name
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
