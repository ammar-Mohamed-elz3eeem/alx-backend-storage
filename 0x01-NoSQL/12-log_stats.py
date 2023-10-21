#!/usr/bin/env python3
"""script to insert in collection
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("method {}: {}".format(method,
                                     collection.count_documents({
                                         "method": method})))
