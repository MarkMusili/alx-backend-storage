#!/usr/bin/env python3
"""
Find schools with a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find school that have the same topic
    return a list of schools with the same topic
    """
    return mongo_collection.find({"topics": topic})