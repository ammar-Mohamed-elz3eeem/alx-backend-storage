#!/usr/bin/env python3
"""script to insert in collection
"""
from typing import Dict, Any
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: Dict[Any, Any]) -> str:
    """insert document into collection given as input

    Args:
        mongo_collection (Collection): mongo collection to insert in it

    Returns:
        str: newely inserted item id
    """
    return mongo_collection.insert_one(kwargs).inserted_id.__str__()
