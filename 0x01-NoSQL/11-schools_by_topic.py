#!/usr/bin/env python3
"""11. Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Retrieves list of schools which have a specific topic.

    Args:
        mongo_collection: the target collection.
        topic: the topic to filter by.
    Returns:
        list: a list of schools.
    """
    return list(mongo_collection.find({'topics': topic}))
