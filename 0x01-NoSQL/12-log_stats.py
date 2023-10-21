#!/usr/bin/env python3
"""script to insert in collection
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, collection
                                       .count_documents({
                                         "method": method})))
    print("{} status check".format(collection.count_documents
                                   ({"method": "GET", "path": "/status"})))
