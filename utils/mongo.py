from typing import Any

import pymongo

import config
from utils import dictception as di

_client = pymongo.MongoClient(config.mongo_url)
_db = _client["MongoDB"]


def set(path: str, value: Any) -> None:
    path = [_ for _ in path.split(".") if _ != ""]

    collection = _db[path.pop(0)]  # set( "collectionName" )
    if path == []:
        result = collection.find_one({"_id": "_default"}, {"_id" : 1})
        if result is None:
            return collection.insert_one({"_id": "_default", "_default": value})
        return collection.update_one({"_id": "_default"}, {"$set": {"_default": value}})

    _id = path.pop(0)  # set( "collectionName.cardID" )
    if path == []:
        result = collection.find_one({"_id": _id}, {"_id" : 1})
        if result is None:
            return collection.insert_one({"_id": _id, "_default": value})
        return collection.update_one({"_id": _id}, {"$set": {"_default": value}})

    key = path.pop(0)  # set( "collectionName.cardID.DIpath" )
    result = collection.find_one({"_id": _id}, {"_id" : 1})
    if result is None:
        return collection.insert_one({"_id": _id, key: di.assemble(path, value)})  # is there a better way for this?
    path.insert(0, key)
    return collection.update_one({"_id": _id}, {"$set": {".".join(path): value}})


def rem(path: str, value) -> None:
    path = [_ for _ in path.split(".") if _ != ""]

    collection = _db[path.pop(0)]  # rem( "collectionName" )
    if path == []:
        return collection.drop()

    _id = path.pop(0)  # rem( "collectionName.cardID" )
    if path == []:
        return collection.delete_one({"_id": _id})

    elif len(path) == 1:  # rem( "collectionName.cardID.varName")
        key = path.pop(0)
        return collection.update_one({"_id": _id}, {"$unset": {key: ""}})
    
    return collection.update_one({"_id": _id}, {"$unset": {".".join(path)}})


def get(path: str, default=None) -> Any:
    path = [_ for _ in path.split(".") if _ != ""]

    collection = _db[path.pop(0)]  # set( "collectionName" )
    if path == []:
        result = collection.find_one({"_id": "_default"}, {"_id": 0, "_default": 1})
        if result is not None:
            return result.get("_default", default)
        return default

    _id = path.pop(0)  # set( "collectionName.cardID" )
    if path == []:
        result = collection.find_one({"_id": _id}, {"_id": 0, "_default": 1})
        if result is not None:
            return result.get("_default", default)
        return default

    result = collection.find_one({"_id": _id}, {"_id": 0, ".".join(path): 1})  # set( "collectionName.cardID.DIpath" )
    if result is not None or result != {}:
        return di.find(result, path)
    return default
