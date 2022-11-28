from tinydb import TinyDB, where
from tinydb.storages import JSONStorage
db = TinyDB('testdb.json',storage=JSONStorage)
tbl = db.table('our_table')