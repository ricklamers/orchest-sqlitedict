### SQLite example

This pipeline implements a basic example demonstrating how to use SQLite as a backing store for a shared key, value store.

It uses SqliteDict: https://pypi.org/project/sqlitedict/. The main implementation bit is in [utils.py](utils.py).

The environment variable to customize the storage location is:

`SQLITE_STORE_PATH` default: `/data/sqlite_store.sqlite`

It supports any [pickle serializable](https://docs.python.org/3/library/pickle.html) object.

![SqliteDict pipeline](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/orchest-sqlitedict/blob/master/main.orchest)
