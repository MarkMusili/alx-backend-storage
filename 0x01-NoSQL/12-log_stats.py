#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB:
"""
import pymongo


if __name__ == "__main__":
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    x = db_client.logs.nginx
    count = x.count_documents({})
    print(f"{count} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = x.count_documents({"method": method})
        print(f"    method {method}: {method_count}")
    path_method = x.count_documents({"method": "GET", "path": "/status"})
    print(f"{path_method} status count")
