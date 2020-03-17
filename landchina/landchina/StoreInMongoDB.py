import pymongo
import datetime
import requests
import re
from bs4 import BeautifulSoup
import time
import multiprocessing
import threading
import random

class MonQueue(object):
    Waiting = 1
    Processing = 2
    Complete = 3
    def __init__(self,db,collection,timeout = 300):
        self.client = pymongo.MongoClient()
        self.Client = self.client[db]
        self.db = self.Client[collection]
        self.timeout = timeout

    def __bool__(self):
        record = self.db.find_one(
            {'status': {'$ne': self.Complete}}
        )
        return True if record else False
    def push(self,url):
        try:
            self.db.insert_one({'ID': url,'status':self.Waiting})
            # print("insert successfully")
        except pymongo.errors.DuplicateKeyError as e:
        # except DuplicateKeyError as e:
            print("this url is existed.")
            pass
    def pop(self):
        # record = self.db.find_and_modify(
        #     query={'status': self.Waiting},
        #     update={'$set': {'status': self.Processing, 'timestamp': datetime.datetime.now()}}
        # )
        record = self.db.find_one(
            {'status': self.Waiting}
        )
        # print(record)
        if record:
            return record['ID']
        else:
            self.repair()
            raise KeyError
    def peek(self):
        record = self.db.find_one({'status': self.Waiting})
        if record:
            return record['_id']
    def repair(self):
        record = self.db.find_and_modify(
            query={
                'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                'status': {'$ne': self.Complete}
            },
            update={'$set': {'status': self.Waiting}}
        )
        if record:
            print('reset Url status', record['ID'])
    def complete(self,url):
        # self.db.update({'ID': url}, {'$set': {'status': self.Complete}})
        self.db.remove({'ID': url})
    def clear(self):
        self.db.drop()