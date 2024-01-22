#!/usr/bin/env python3
"""12. Log stats"""


if __name__ == '__main__':
    import pymongo
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx
    print(coll.count_documents({}), 'logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f'\tmethod {method}:', coll.count_documents({'method': method}))
    print(coll.count_documents({'method': 'GET', 'path': '/status'}))
