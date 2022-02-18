from typing import Any

from pymongo import MongoClient


class Utils:

    @staticmethod
    def assemble(path: list, value: Any) -> dict:
        to_asm, i = {}, 0
        ref = to_asm
        if not path:
            return value
        for _ in path:
            i += 1
            if i == len(path):
                to_asm[_] = value
                break
            to_asm[_] = {}
            to_asm = to_asm[_]
        return ref

    @staticmethod
    def find(get_from: dict, path: list, *, default: Any = None) -> Any:
        key = path.pop(-1)
        for _ in path:
            try:
                get_from = get_from[_]
            except (KeyError, TypeError, AttributeError):
                return default
        return get_from.get(key, default)


class MongoManager:

    def __init__(self, connect_url: str, database: str):
        self.client = MongoClient(connect_url)
        self.db = self.client[database]
        self.utils = Utils

    def set(self, path: str, value: Any) -> None:
        path = [_ for _ in path.split(".") if _ != ""]
        collection = self.db[path.pop(0)]
        if not path:  # set( "collectionName" )
            result = collection.find_one({"_id": "_"}, {"_id": 1})
            if result is None:
                return collection.insert_one({"_id": "_", "_": value})
            else:
                return collection.update_one({"_id": "_"}, {"$set": {"_": value}})
        _id = path.pop(0)
        if not path:  # set( "collectionName.cardID" )
            result = collection.find_one({"_id": _id}, {"_id": 1})
            if result is None:
                return collection.insert_one({"_id": _id, "_": value})
            else:
                return collection.update_one({"_id": _id}, {"$set": {"_": value}})
        result = collection.find_one({"_id": _id}, {"_id": 1})  # set( "collectionName.cardID.DIpath" )
        if result is None:
            return collection.insert_one(
                {"_id": _id, **self.utils.assemble(path, value)})  # is there a better way for this?
        return collection.update_one({"_id": _id}, {"$set": {".".join(path): value}})

    def rem(self, path: str) -> None:
        path = [_ for _ in path.split(".") if _ != ""]
        collection = self.db[path.pop(0)]
        if not path:  # rem( "collectionName" )
            return collection.drop()
        _id = path.pop(0)
        if not path:  # rem( "collectionName.cardID" )
            return collection.delete_one({"_id": _id})
        elif len(path) == 1:
            key = path.pop(0)  # rem( "collectionName.cardID.varName" )
            return collection.update_one({"_id": _id}, {"$unset": {key: ""}})
        return collection.update_one({"_id": _id},
                                     {"$unset": {".".join(path)}})  # rem( "collectionName.cardID.DIpath" )

    def get(self, path: str, default: Any = None) -> Any:
        path = [_ for _ in path.split(".") if _ != ""]
        collection = self.db[path.pop(0)]  # set( "collectionName" )
        if not path:
            result = collection.find_one({"_id": "_"}, {"_id": 0, "_": 1})
            if result is not None:
                return result.get("_", default)
            else:
                return default
        _id = path.pop(0)  # set( "collectionName.cardID" )
        if not path:
            result = collection.find_one({"_id": _id}, {"_id": 0, "_": 1})
            if result is not None:
                return result.get("_", default)
            else:
                return default
        result = collection.find_one({"_id": _id},
                                     {"_id": 0, ".".join(path): 1})  # set( "collectionName.cardID.DIpath" )
        if result is not None:
            return self.utils.find(result, path, default=default)
        return default
