#!/usr/bin/env python3
"""script to list all documents in collection
"""


def list_all(mongo_collection):
    """get all documents defined in single collection
    with collection name as input

    Args:
        mongo_collection (MongoClient.Database.Collection):
        mongo collection to get its documents

    Returns:
        List[Dict[str, str]]: all documents inside given collection
    """
    return mongo_collection.find()
