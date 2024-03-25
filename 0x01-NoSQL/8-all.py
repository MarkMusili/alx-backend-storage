#!/usr/bin/env python3
"""
Using pymongo list all docs in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    else return an empty list
    """
    return mongo_collection.find()
