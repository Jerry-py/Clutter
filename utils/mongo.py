import pymongo
import pathmagic
import config
from typing import Any

client = pymongo.MongoClient(config.mongo_url)
db = client.MongoDB


def set(path: str, value) -> None:
    path = path.split(".")
    while "" in path:
        path.remove("")

    section = db[path.pop(0)]  # set( "sectionName" )
    if path == []:
        result = section.find_one({"_id": "_default"})
        if result is None:
            return section.insert_one({"_id": "_default", "_default": value})
        else:
            return section.update_one({"_id": "_default"}, {"$set": {"_default": value}})

    _id = path.pop(0)  # set( "sectionName.cardID" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is None:
            return section.insert_one({"_id": _id, "_default": value})
        else:
            return section.update_one({"_id": _id}, {"$set": {"_default": value}})

    var_name = path.pop(0)  # set( "sectionName.cardID.varName" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is None:
            return section.insert_one({"_id": _id, var_name: value})
        else:
            return section.update_one({"_id": _id}, {"$set": {var_name: value}})

    key = path.pop(-1)  # set( "sectionName.cardID.varName.PMobject" )
    result = section.find_one({"_id": _id}, {var_name: 1})
    if result is None:
        return section.insert_one({"_id": _id, var_name: pathmagic.set({}, path, dump={key: value})})
    else:
        path.insert(0, var_name)
        return section.update_one({"_id": _id}, {"$set": {var_name: pathmagic.set(result[var_name], path, dump={key: value})}})


def rem(path: str, value) -> None:
    path, i = path.split("."), 0
    while "" in path:
        path.remove("")

    section = db[path.pop(0)]  # rem( "sectionName" )
    if path == []:
        if section in db.list_collection_names():
            return section.drop()

    _id = path.pop(0)  # rem( "sectionName.cardID" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is not None:
            return section.delete_one({"_id": _id})

    var_name = path.pop(0)  # rem( "sectionName.cardID.varName" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is not None:
            section.update_one({"_id": _id}, {"$unset": {var_name: ""}})

    # TODO add PM rem


def get(path: str = "", default=None) -> Any:
    path = path.split(".")
    while "" in path:
        path.remove("")

    section = db[path.pop(0)]  # set( "sectionName" )
    if path == []:
        result = section.find_one({"_id": "_default"})
        if result is not None:
            return result.get("_default", default)
        return default

    _id = path.pop(0)  # set( "sectionName.cardID" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is not None:
            return result.get("_default", default)
        return default

    var_name = path.pop(0)  # set( "sectionName.cardID.varName" )
    if path == []:
        result = section.find_one({"_id": _id})
        if result is not None:
            return result.get(var_name, default)
        return default

    key = path.pop(-1)  # set( "sectionName.cardID.varName.PMobject" )
    result = section.find_one({"_id": _id}, {var_name: 1})
    if result is not None:
        path.insert(0, var_name)
        return pathmagic.get(result, path, key=key, default=default)
