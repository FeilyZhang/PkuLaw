import pymongo

'''mongodb
Read and write MongoDB.

@author: FeilyZhang
@date: 2020-11-29 21:15:27
@version: alpha 0.1
@mail: fei@feily.tech
'''
class mongodb:

    __host = ''
    __port = ''
    __mongo_client = None

    def __init__(self, host = '127.0.0.1', port = '27017'):
        self.__host = host
        self.__port = port
        self.__mongo_client = pymongo.MongoClient('mongodb://' + self.__host + ':' + self.__port)

    def insert_one(self, db, col, dat):
        self.__mongo_client[db][col].insert_one(dat)

    def insert_all(self, db, col, dat):
        self.__mongo_client[db][col].insert(dat)

    def find_all(self, db, col):
        return self.__mongo_client[db][col].find({})

    def is_exist(self, db, col, cond):
        return len(list(self.__mongo_client[db][col].find(cond))) != 0