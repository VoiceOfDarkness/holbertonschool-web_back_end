#!/usr/bin/env python3
"""Update a document in mongodb collection"""


def update_topics(mongo_collection, name, topics):
    """Update a document in a collection"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
