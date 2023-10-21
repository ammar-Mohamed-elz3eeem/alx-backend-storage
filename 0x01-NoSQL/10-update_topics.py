#!/usr/bin/env python3
"""script to insert in collection
"""


def update_topics(mongo_collection, name: str, topics):
    """insert document into collection given as input

    Args:
        mongo_collection (Collection): mongo collection to insert in it

    Returns:
        str: newely inserted item id
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
