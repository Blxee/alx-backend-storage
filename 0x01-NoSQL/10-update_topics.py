#!/usr/bin/env python3
"""10. Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Updates all school document with new topics in a collection.

    Args:
        mongo_collection: the target collection.
        name: the name of the schools to use in filter.
        topics: the new topics that the schools shuold be updated with.
    """
    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})
