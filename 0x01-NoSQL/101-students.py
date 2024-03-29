#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    """Fetches all students from the collection sorted by average score.

    Args:
        mongo_collection: the target collection.
    Returns:
       list: the resulted list.
    """
    return list(
        mongo_collection.aggregate([
            {
                '$project': {
                    '_id': 1,
                    'name': 2,
                    'averageScore': {
                        '$avg': '$topics.score'
                    }
                }
            },
            {
                '$sort': {
                    'averageScore': -1,
                }
            }
        ])
    )
