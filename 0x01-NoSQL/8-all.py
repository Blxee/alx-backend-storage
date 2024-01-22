#!/usr/bin/env python3
"""8. List all documents in Python"""


def list_all(mongo_collection):
    """Lists all documents in a mongodb collection.

    Args:
        mongo_collection: the target collection.

    Returns:
        list: all the documents in the collection in a list format.
    """
    return mongo_collection.find()
