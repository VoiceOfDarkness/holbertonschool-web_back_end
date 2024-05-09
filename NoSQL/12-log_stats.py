#!/usr/bin/env pyton3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Log stats"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print('{} logs'.format(logs_collection.count_documents()))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))
    print('{} status check'.format(logs_collection.count_documents({})))
