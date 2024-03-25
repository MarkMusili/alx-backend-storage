#!/usr/bin/env python3
"""
Insert one document into a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert into a collection
    Returns the new _id
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
