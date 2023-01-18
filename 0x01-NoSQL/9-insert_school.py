#!/usr/bin/env python3
"""Defining a function called insert_school"""
import pymongo
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
    