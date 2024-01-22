#!/usr/bin/env python3
"""9. Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection based on kwargs.

    Args:
        mongo_collection: the target collection.
    Kwargs:
        the fields of the new document.
    Returns:
        the field id.
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
