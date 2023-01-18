#!/usr/bin/env python3
"""Create a method called list_all"""
import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    return mongo_collection.find()
    