#!/usr/bin/env python3
""" 8. List all documents in Python """


def list_all(mongo_collection):
    """List all documents in a collection"""
    documents = mongo_collection.find()
    return list(documents) if documents else []
