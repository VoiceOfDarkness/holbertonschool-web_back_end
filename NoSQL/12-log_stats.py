#!/usr/bin/env pyton3
"""Log stats"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Log stats"""

    print('{} logs'.format(mongo_collection.count_documents()))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))
    print('{} status check'.format(mongo_collection.count_documents({})))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)
