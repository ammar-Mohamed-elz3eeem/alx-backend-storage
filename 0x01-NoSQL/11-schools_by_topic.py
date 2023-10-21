#!/usr/bin/env python3
"""script to insert in collection
"""


def schools_by_topic(mongo_collection, topic):
    """insert document into collection given as input

    Args:
        mongo_collection (Collection): mongo collection to insert in it

    Returns:
        str: newely inserted item id
    """
    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})
