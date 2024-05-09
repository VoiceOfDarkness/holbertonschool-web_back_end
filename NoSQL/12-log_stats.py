#!/usr/bin/env pyton3
"""Log stats"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Log stats"""
    print(f'{mongo_collection.estimatedDocumentCount()} logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.countDocuments({"method": method})
        print(f'\tmethod {method}: {count}')
    print(f'{mongo_collection.countDocuments({})} status check')


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_stats(logs_collection)
