#!/usr/bin/env python3
"""15. Log stats - new version"""


if __name__ == '__main__':
    import pymongo
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx
    print(coll.count_documents({}), 'logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f'\tmethod {method}:', coll.count_documents({'method': method}))
    print(coll.count_documents({'method': 'GET', 'path': '/status'}), 'status check')
    print('IPs:')
    most_present = list(coll.aggregate([{'$group': {'_id': '$ip', 'occurence': {'$count': {}}}}, {'$sort': {'occurence': -1}}, {'$limit': 10}]))
    for item in most_present:
        print(f'\t{item["_id"]}: {item["occurence"]}')
