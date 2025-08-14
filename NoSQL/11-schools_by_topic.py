#!/usr/bin/evn python3
"""11. Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic"""
    return mongo_collection.find({"topic": topic})