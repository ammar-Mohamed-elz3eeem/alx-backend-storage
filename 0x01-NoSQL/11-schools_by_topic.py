#!/usr/bin/env python3
"""script to insert in collection
"""
from typing import List
from pymongo.collection import Collection
from pymongo.cursor import Cursor


def schools_by_topic(mongo_collection: Collection, topic: str) -> Cursor:
    """insert document into collection given as input

    Args:
        mongo_collection (Collection): mongo collection to insert in it

    Returns:
        str: newely inserted item id
    """
    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})
