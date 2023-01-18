#!/usr/bin/env python3
"""Defining a function called schools_by_topic"""
import pymongo
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topic": topic})
    