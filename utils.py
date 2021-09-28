import os

from sqlitedict import SqliteDict


def get_shared_dict():
    sqlite_path = os.environ.get("SQLITE_STORE_PATH", "/data/sqlite_store.sqlite")
    return SqliteDict(sqlite_path, autocommit=True)


def set_store_value(key, value):
    shared_dict = get_shared_dict()
    shared_dict[key] = value
    shared_dict.close()
    

def get_store_value(key):
    shared_dict = get_shared_dict()
    value = shared_dict[key]
    shared_dict.close()
    return value
    